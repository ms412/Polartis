
from polatis.calls.transport import Transport
import xml.etree.ElementTree as et

class Port(Transport):
    def __init__(self):
        pass

    def setPortState(self,port,STATE):
        pass

    def setPortLabel(self,port,localLabel,remoteLabel):

        _call = ('api/data/optical-switch:port-config'+ '/' + 'port=' + str(port))

        _port = et.Element("port")
        _ingress = et.SubElement(_port,"label")
        _ingress.text = str(localLabel)
        _egress = et.SubElement(_port,"peer-port")
        _egress.text = str(remoteLabel)

        _response = self.patch(_call,et.tostring(_port))

        return(_response.status_code, _response.content)
