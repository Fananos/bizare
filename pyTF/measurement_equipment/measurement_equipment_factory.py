from pyTF.pytflog import get_logger
from pyTF.exorrs import *
from pyTF.measurement_equipment.Devices import *

log = get_logger("pyFT.measurement.equipment.factory")


class Factory:
    """
    Factory of measurement equipment
    """

    @staticmethod
    def get_device(ip, port):
        """
        Get device X
        """
        obj = Example(ip=ip, port=port)
        if obj.init() != Error.OK:
            raise DeviceInit

        return obj
