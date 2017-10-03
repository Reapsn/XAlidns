import re
import urllib2


class DNSUtil:
    def queryMyServerFactIpByIp138(self):

        try:
            ip38html = urllib2.urlopen('http://1212.ip138.com/ic.asp').read().replace('\n', '').replace('\r', '')
            matchObj = re.search('([\d]{1,3}\.){3}([\d]{1,3})', ip38html, re.M | re.I)
            return matchObj.group()
        except urllib2.HTTPError as e:
            print('queryMyServerFactIpByIp138:', e)
            return None

    def queryMyServerFactIpByIVCURD(self):

        try:
            ip38html = urllib2.urlopen('http://blog.ivcurd.com/util/ip.php').read().replace('\n', '').replace('\r', '')
            return ip38html
        except urllib2.HTTPError as e:
            print('queryMyServerFactIpByIVCURD:', e)
            return None
