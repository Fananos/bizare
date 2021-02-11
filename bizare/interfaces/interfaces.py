from abc import ABCMeta
import abc
from bizare.pytflog import get_logger


log = get_logger("interfaces", False)


class InterfaceFactory(metaclass=ABCMeta):
    """
    Interface for factory
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'init') and
                callable(subclass.init)
                )

    @abc.abstractmethod
    def init(self):
        raise NotImplemented


class InterfaceReadWriteBuffer(metaclass=ABCMeta):
    """
    Interface read/write for buffers
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read') and
                callable(subclass.read) and
                hasattr(subclass, 'write') and
                callable(subclass.write))

    @abc.abstractmethod
    def read(self, buffer, length):
        raise NotImplemented

    @abc.abstractmethod
    def write(self, buffer, data, length):
        raise NotImplemented


class WithSupport(metaclass=ABCMeta):
    """
    Interface to handle with (Python operator)
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '__enter__') and
                callable(subclass.__enter__) and
                hasattr(subclass, '__exit__') and
                callable(subclass.__exit__))

    @abc.abstractmethod
    def __enter__(self):
        raise NotImplemented

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplemented