from enum import Enum


class Exrorr(Exception):
    """
    Custome Exceptions
    """
    pass


class DeviceInit(Exrorr):
    pass


class Error(Enum):
    OK = 0
    FAIL = 1000
