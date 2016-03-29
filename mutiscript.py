import signal
import curses
import multiprocessing
from blinker import Signal
import sys
import functools


class BaseProcess(object):
    def __init__(self, new_func=None, total_count=None, *args, **kwargs):
        self.func = new_func
        self.total_count = total_count
        self.count = 0
        self.task_queue = []
        self.process_list = []
        self.process_map = {}
        self.task_map = {}
        self.args = args
        self.kwargs = kwargs
        signal.signal(signal.SIGWINCH, self.action)
        # self.window = curses.initscr()
        self.add_task_signal = Signal(1000)
        self.count_signal = Signal(1001)
        self.reg_task_signal()
        self.reg_count_sinal()

    def reg_count_sinal(self):
        if not self.total_count:
            return
        else:
            self.count_signal.connect(self.process_count)

    def reg_task_signal(self):
        self.add_task_signal.connect(self.process_func)

    def create_new_task(self, work_num=1):
        for i in range(work_num):
            self.task_queue.append((self.func, self.args, self.kwargs))
            self.add_task_signal.send()
        if self.total_count:
            for i in range(self.total_count):
                self.count_signal.send()
        self.process_map = {x: 0 for x in range(work_num)}



    def make_func(self):
        def add_count_deco(self, func):
            def wrapper(func):
                @functools.wraps(func)
                def _wrapper(*args, **kwargs):
                    func(*args, **kwargs)
                    self.count += 1
                return _wrapper

            return wrapper
        @add_count_deco(self,self.func)
        def _make_func(*args,**kwargs):
            pass
        return _make_func

    def process_func(self, sender):
        while self.task_queue != []:
            self.task_queue.pop()
            process = multiprocessing.Process(target=self.func, args=self.args, kwargs=self.kwargs)
            process.start()

    def process_count(self, sender):
        self.count += 1
        bar_length = 20
        percent = float(self.count * 1.0 / self.total_count)
        hashes = '#' * int(percent * bar_length)
        spaces = ' ' * (bar_length - len(hashes))
        multiprocessing.Process(
            target=sys.stdout.write("\rPercent: [%s] %d%%" % (hashes + spaces, percent * 100))).start()

    def action(self):
        key = self.window.getch()
        if key == ord('p'):
            pass
        if key == ord('r'):
            pass

    def start(self):
        while True:
            self.action()
