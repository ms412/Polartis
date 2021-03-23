
from polatis.calls.transport import Transport
import xml.etree.ElementTree as et

class Shutter(Transport):
    def __init__(self):
        pass

    def configureShutter(self,blockTime,restoreTime,cycles,port):

        _call = self.post('api/data/polatis-switch:shutter-config')

        _shutterConfig = et.Element("port")
        _portId = et.SubElement(_shutterConfig,"port-id")
        _portId.text = str(port)
        _blockTime = et.SubElement(_shutterConfig,"signal-block-time")
        _blockTime.text = str(blockTime)
        _restoreTime = et.SubElement(_shutterConfig,"signal-restore")
        _restoreTime.text = str(restoreTime)
        _cycles = et.SubElement(_shutterConfig,"cycles")
        _cycles.text = str(cycles)

        _response = self.post(_call,et.tostring(_shutterConfig))

        return(_response.status_code, _response.content)

    def startShutter(self,port):

        _call = ('api/data/polatis-switch:shutter-operation')

        _operation = et.Element("shutter-operation")
        _activate = et.SubElement(_operation,"activate")
        _activate.text = 'true'
        _port = et.SubElement(_operation,"port")
        _port.text = str(port)

        _response = self.get(_call)

        return(_response.status_code, _response.content)

    def stopShutter(self,port):

        _call = ('api/data/polatis-switch:shutter-operation')

        _operation = et.Element("shutter-operation")
        _activate = et.SubElement(_operation,"activate")
        _activate.text = 'false'
        _port = et.SubElement(_operation,"port")
        _port.text = str(port)

        _response = self.get(_call)

        return(_response.status_code, _response.content)

    def statusShutter(self,port=0):

        if port == 0:
            _call = ('api/data/polatis-switch:shutter-status')
        else:
            _call = ('api/data/polatis-switch:shutter-status' + '/' + 'port=' + str(port))
        _response = self.get(_call)

        return(_response.status_code, _response.content)