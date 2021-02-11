from bizare.pytflog import get_logger
from bizare.exorrs import *
from bizare.measurement_equipment.Devices import *

log = get_logger("pyFT.measurement.equipment.factory")


class Factory:
    """
    Factory of measurement equipment
    """
    # Example
    @staticmethod
    def get_device(ip, port):
        """
        Get device X
        """
        obj = Example(ip=ip, port=port)
        if obj.init() != Error.OK:
            raise DeviceInit

        return obj
