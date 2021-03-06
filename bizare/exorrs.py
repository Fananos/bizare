from enum import Enum


class Exrorr(Exception):
    """
    Custom Exceptions
    """
    pass


class DeviceInit(Exrorr):
    pass


class Error(Enum):
    OK = 0
    FAIL = 1000
