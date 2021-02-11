from random import choice
import string
from bizare.interfaces.interfaces import WithSupport


class StringFormat:
    LOWER = 0x1
    UPPER = 0x2
    DIGITS = 0x4
    UPP_LOW = (LOWER | UPPER)
    UPP_DIG = (UPPER | DIGITS)
    LOW_DIG = (LOWER | DIGITS)
    ALL = (UPP_LOW | DIGITS)


class RandomString(WithSupport):
    def __init__(self, length, formations):
        self.length = length
        self.formations = formations

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def random_string_generator(self):
        if self.formations == StringFormat.DIGITS:
            pattern = string.digits
        elif self.formations == StringFormat.UPPER:
            pattern = string.ascii_uppercase
        elif self.formations == StringFormat.LOWER:
            pattern = string.ascii_lowercase
        elif self.formations == StringFormat.UPP_LOW:
            pattern = string.ascii_lowercase + string.ascii_uppercase
        elif self.formations == StringFormat.UPP_DIG:
            pattern = string.ascii_uppercase + string.digits
        elif self.formations == StringFormat.LOW_DIG:
            pattern = string.ascii_lowercase + string.digits
        elif self.formations == StringFormat.ALL:
            pattern = string.ascii_lowercase + string.ascii_uppercase + string.digits
        else:
            return None

        return "".join(choice(pattern) for _ in range(self.length))
