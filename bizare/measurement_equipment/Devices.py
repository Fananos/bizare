from abc import ABC

from bizare.pytflog import get_logger
from bizare.exorrs import *
from bizare.interfaces.interfaces import WithSupport, InterfaceFactory


class BaseDevice(InterfaceFactory, ABC):
    def __init__(self):
        self.log = get_logger(f"Devices")


# Example device
class Example(BaseDevice, WithSupport):
    def __init__(self, *args, **kwargs):
        BaseDevice.__init__(self)
        pass

    def init(self):
        self.log.info(f"Status {Error.OK}")
        return Error.OK

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Done")

    def __del__(self):
        print("Instance deleted")
