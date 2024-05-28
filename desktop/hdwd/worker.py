import time
from typing import Optional
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool

class WorkerSignals(QObject):
    interval_finished = Signal(object)
    interval_output = Signal(object)
    interval_error = Signal(object)

class Worker(QRunnable):

    def __init__(self, function, interval: Optional[int]=None, *args, **kwargs):
        super(Worker, self).__init__()

        self.function = function
        self.interval = interval
        self.args     = args
        self.kwargs   = kwargs
        self.signals  = WorkerSignals()
        self.alive   = True 
        self.suspended  = False
        self.remaining = 0
        self.checkpoint_interval = 0.1

        QApplication.instance().aboutToQuit.connect(self.abort)

    @Slot()
    def run(self):
        while self.alive:
            if self.remaining <= 0:
                try: 
                    result = self.function(*self.args, **self.kwargs)
                    if self.alive:
                        self.signals.interval_finished.emit(result)
                except Exception as e:
                    if self.alive:
                        self.signals.interval_error.emit(e)
                if self.interval == None:
                    break
                self.remaining = self.interval

            time.sleep(self.checkpoint_interval)
            if not self.suspended:
                self.remaining -= self.checkpoint_interval

    def abort(self) -> None: self.alive = False
    def pause(self) -> None: self.suspended = True
    def resume(self) -> None: self.suspended = False
    def invoke_run(self) -> None: self.remaining = 0
