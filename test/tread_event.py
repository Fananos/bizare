from bizare.core.event_basic import *


def test_event():
    sch = EventScheduler()
    tear_down = CleanUp()
    clean_event = threading.Event()
    sch.register_event(clean_event, Events.DONE)