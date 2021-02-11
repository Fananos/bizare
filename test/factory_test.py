from bizare.measurement_equipment.measurement_equipment_factory import Factory
from bizare.pytflog import get_logger
import logging

log = get_logger("Test")
log.setLevel(logging.DEBUG)


def test_with_support_factory():
    e = Factory.get_device("10", 10)
    assert e
    try:
        with e as a:
            pass
        assert 1 == 1
    except:
        assert 1 == 2
