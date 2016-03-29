# multiscript

you can use this package below

```
import os
from mutiscript import BaseProcess


def test_func(num):
    os.system('curl http://www.baidu.com')


def test_case_1():
    b = BaseProcess(test_func, num=1)
    c = BaseProcess(test_func, num=2,total_count=20) ##you can use percent bar As adding total_count value equals the sum count 
    b.create_new_task(work_num=3)
    c.create_new_task(work_num=10)

if __name__=="__main__":
    test_case_1()

```
