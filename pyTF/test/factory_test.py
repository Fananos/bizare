from pyTF.measurement_equipment.measurement_equipment_factory import Factory


def test_factory():
    e = Factory.get_device("10", 10)
    assert e
    try:
        with e as a:
            pass
        assert 1 == 1
    except:
        assert 1 == 2

