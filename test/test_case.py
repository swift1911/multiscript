import os
from mutiscript import BaseProcess


def test_func(num):
    os.system('curl http://www.baidu.com')


def test_case_1():
    b = BaseProcess(test_func, num=1)
    c = BaseProcess(test_func, num=2)
    b.create_new_task(work_num=3)
    c.create_new_task(work_num=10)
