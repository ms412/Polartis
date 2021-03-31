
from polatis.calls.transport import Transport

class OPM(Transport):
    def __init__(self):
        pass

    def getOpticalPower(self,port=0):

        if port == 0:
            _call = ('api/data/optical-switch:opm-power')
        else:
            _call = ('api/data/optical-switch:opm-power'+'/'+'port='+str(port))

        _response = self.get(_call)

        return (_response.status_code, _response.content)
