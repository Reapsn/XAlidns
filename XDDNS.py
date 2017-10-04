# -*- coding: utf-8 -*-

import json
import logging
import logging.config
import time

from aliyunsdkcore.client import AcsClient

from model.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from model.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from util.DNSUtil import DNSUtil


class XDDNS:
    def __init__(self, json_config):

        self.__json_config = json_config
        self.__acsClient = self.__buildClient(self.__json_config)

    def updateDNSIp(self, RR, newIp, Type='A'):

        RecordId = self.queryDomainRecordId(RR)

        request = UpdateDomainRecordRequest()
        request.set_RecordId(RecordId)
        request.set_RR(RR)
        request.set_Type(Type)
        request.set_Value(newIp)

        return json.loads(self.__acsClient.do_action_with_exception(request))

    def describeDomainRecords(self, DomainName):

        request = DescribeDomainRecordsRequest()
        request.set_DomainName(DomainName)
        return json.loads(self.__acsClient.do_action_with_exception(request))

    def queryDomainRecordId(self, RR):

        domainRecords = self.describeDomainRecords(self.__json_config['Domain'])
        domainRecords = domainRecords["DomainRecords"]["Record"]

        for i in range(len(domainRecords)):
            if domainRecords[i]["RR"] == RR:
                return domainRecords[i]["RecordId"]

        return None

    def queryDomainRecordIp(self, RR):

        domainRecords = self.describeDomainRecords(self.__json_config['Domain'])
        domainRecords = domainRecords["DomainRecords"]["Record"]

        for i in range(len(domainRecords)):
            if domainRecords[i]["RR"] == RR:
                return domainRecords[i]["Value"]

        return None

    def __buildClient(self, json_config):

        return AcsClient(
            str(json_config['id']),
            str(json_config['secret']),
            "cn-shanghai"
        )

# @param interval 单位：秒
def watchDNS():
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger("root.xddns")

    jsonfile = open("config.json")
    json_config = json.load(jsonfile)

    xddns = XDDNS(json_config)
    util = DNSUtil()

    while (True):

        try:

            myServerFactIp = util.queryMyServerFactIpByIVCURD()
            logger.debug("myServerFactIp:" + myServerFactIp)
            dnsRecordIp = xddns.queryDomainRecordIp(json_config["RR"])
            logger.debug("dnsRecordIp:" + dnsRecordIp)
            if (myServerFactIp != dnsRecordIp):
                logger.debug(xddns.updateDNSIp(json_config["RR"], myServerFactIp))

            time.sleep(json_config["interval"])

        except Exception as e:
            logger.error('watchDNS:', e)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='xddns.log',
                        filemode='w')

    watchDNS()
