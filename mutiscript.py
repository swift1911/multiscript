import signal
import curses
import multiprocessing
from blinker import Signal


class BaseProcess(object):
    def __init__(self, new_func=None, *args, **kwargs):
        self.func = new_func
        self.task_queue = []
        self.process_list = []
        self.process_map = {}
        self.task_map = {}
        self.args = args
        self.kwargs = kwargs
        signal.signal(signal.SIGWINCH, self.action)
        self.window = curses.initscr()
        self.add_task_signal = Signal(1000)
        self.reg_signal()

    def reg_signal(self):
        self.add_task_signal.connect(self.process_func)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def create_new_task(self, work_num=1):
        for i in range(work_num):
            self.task_queue.append((self.func, self.args, self.kwargs))
            self.add_task_signal.send()
        self.process_map = {x: 0 for x in range(work_num)}

    def process_func(self, sender):
        while self.task_queue != []:
            self.task_queue.pop()
            process = multiprocessing.Process(target=self.func, args=self.args, kwargs=self.kwargs)
            self.process_list.append(process)
            process.start()

    def action(self):
        key = self.window.getch()
        if key == ord('p'):
            pass
        if key == ord('r'):
            pass

    def start(self):
        while True:
            self.action()


