from aliyunsdkcore.request import RpcRequest


class UpdateDomainRecordRequest(RpcRequest):

    def __init__(self):
        RpcRequest.__init__(self, "Alidns", "2015-01-09", "UpdateDomainRecord")

    def set_RecordId(self, RecordId):
        self.add_query_param('RecordId', RecordId)

    def set_RR(self, RR):
        self.add_query_param('RR', RR)

    def set_Type(self, Type):
        self.add_query_param('Type', Type)

    def set_Value(self, Value):
        self.add_query_param('Value', Value)

    def set_TTL(self, TTL):
        self.add_query_param('TTL', TTL)

    def set_PriorityL(self, Priority):
        self.add_query_param('Priority', Priority)

    def set_Line(self, Line):
        self.add_query_param('Line', Line)