
from polatis.calls.transport import Transport

class System(Transport):
    def __init__(self):
        pass

    def connect(self,host,port,user,pw):
        self.connection(host,port,user,pw)

    def productInformation(self):

        _call = ('api/data/optical-switch:product-information')
        _response = self.get(_call)

        return(_response.status_code, _response.content)

    def batteries(self):

        _call = ('api/data/polatis-switch:batteries')
        _response = self.get(_call)

        return(_response.status_code, _response.content)

