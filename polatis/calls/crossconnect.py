
from polatis.calls.transport import Transport
import xml.etree.ElementTree as et

class CrossConnect(Transport):
    def __init__(self):
        pass

    def createCrossConnection(self,portA,portZ,force=False):

        _call = ('api/data/optical-switch:cross-connects')

        _cc = et.Element("pair")
        _ingress = et.SubElement(_cc,"ingress")
        _ingress.text = str(portA)
        _egress = et.SubElement(_cc,"egress")
        _egress.text = str(portZ)

        if force == False:
            _response = self.post(_call,et.tostring(_cc))
        else:
            _crossconnects = et.Element("crossconnects")
            _crossconnects.text = et.tostring(_cc)
            _response = self.put(_call,et.tostring(_crossconnects))

        return(_response.status_code, _response.content)

    def createCrossConnectionBulk(self,portA,portZ):

        _call = ('api/data/optical-switch:cross-connects')

        _cc = et.Element("cross-connects>")
        for a,z in zip(portA,portZ):
            _pair = et.SubElement(_cc,"pair")
            _ingress = et.SubElement(_pair,"ingress")
            _ingress.text = str(a)
            _egress = et.SubElement(_pair,"egress")
            _egress.text = str(z)

        response = self.patch(_call, et.tostring(_cc))

        print(et.tostring(_cc))


    def deleteCrossConnection(self,port=0):

        if port == 0:
            _call = ('api/data/optical-switch:cross-connects')
        else:
            _call = ('api/data/optical-switch:cross-connects'+'/'+'port='+str(port))

        _response = self.delete(_call)

        return(_response.status_code, _response.content)

    def getCrossConnection(self):

        _call = ('api/data/polatis-switch:cross-connects')

        _response = self.get(_call)

        return (_response.status_code, _response.content)