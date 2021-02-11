from pyTF.pytflog import get_logger
from pyTF.exorrs import *
from pyTF.interfaces.interfaces import WithSupport


class Example(WithSupport):
    def __init__(self, *args, **kwargs):
        pass

    def init(self):
        return Error.OK

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Done")

    def __del__(self):
        print("Instance deleted")
