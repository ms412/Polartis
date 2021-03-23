from polatis.calls.transport import Transport
from polatis.calls.system import System
from polatis.calls.shutter import Shutter
from polatis.calls.crossconnect import CrossConnect
from polatis.calls.opm import OPM
from polatis.calls.port import Port


class Polatis(System,
              Shutter,
              CrossConnect,
              OPM,
              Port):

    def __init__(self):
        pass