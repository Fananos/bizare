import threading
from time import sleep as slp
import enum
from queue import Queue
from bizare.core.call_backs import singleton


class Events(enum.Enum):
    DONE = 0
    INT1 = 3
    INT2 = 4
    INT3 = 5
    INT4 = 6
    INT5 = 7
    INT6 = 8
    INT7 = 9
    INT8 = 10
    INT9 = 11


@singleton
class EventScheduler:
    def __init__(self):
        self.__qu = Queue()
        self.__registrations = dict()

    def add(self, enum):
        self.__qu.put(enum)

    def schedule(self):
        if not self.__qu.empty():
            e = self.__qu.get()
            e = self.__registrations.get(e)
            if e:
                e.set()
                e.clear()

    def register_event(self, event, type_of_event):
        self.__registrations.update({type_of_event: event})


class EventedTrhreadTask(threading.Thread):
    def __init__(self, name, fucn, *args, **kwargs):
        threading.Thread.__init__(self)
        self.name = name
        self.event = threading.Event()
        self._kill = True
        self._running = False

        self._task = fucn
        self._task_args = args
        self._task_kwargs = kwargs

    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id

        for id, thread in threading._active.items():
            if thread is self:
                return id

    def event_cb(self):
        return self.event

    def kill(self):
        self._kill = False

    def run(self):
        while True:
            self.event.wait()  # set->clear

            if not self._kill:
                break

            self._task(*self._task_args, **self._task_kwargs)
            slp(.1)


class CleanUp:
    def __init__(self):
        self.__threads = []

    def add_thread(self, obj):
        self.__threads.append(obj)

    def clean(self):
        for t in self.__threads:
            t.kill()

        for k in self.__threads:
            if not k.event.is_set():
                k.event.set()
            else:
                k.event.clear()
                k.event.set()

        for t in self.__threads:
            t.join()