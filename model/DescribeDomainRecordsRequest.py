from aliyunsdkcore.request import RpcRequest


class DescribeDomainRecordsRequest(RpcRequest):

    def __init__(self):
        RpcRequest.__init__(self, "Alidns", "2015-01-09", "DescribeDomainRecords")

    def set_DomainName(self, DomainName):
        self.add_query_param('DomainName', DomainName)

    def set_PageNum(self, PageNum):
            self.add_query_param('PageNum', PageNum)

    def set_PageSize(self, PageSize):
        self.add_query_param('PageSize', PageSize)

    def set_RRKeyWord(self, RRKeyWord):
        self.add_query_param('RRKeyWord', RRKeyWord)

    def set_TypeKeyWord(self, TypeKeyWord):
        self.add_query_param('TypeKeyWord', TypeKeyWord)

    def set_ValueKeyWord(self, ValueKeyWord):
        self.add_query_param('ValueKeyWord', ValueKeyWord)