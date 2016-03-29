import os
from mutiscript import BaseProcess
import urllib2

def test_func(num):
    for i in range(num):
        urllib2.urlopen('http://qq.com').read()


def test_case_1():
    b = BaseProcess(test_func, num=2000,total_count=10000)
    # c = BaseProcess(test_func, num=2)
    b.create_new_task(work_num=5)
    # c.create_new_task(work_num=10)


if __name__ == "__main__":
    test_case_1()
