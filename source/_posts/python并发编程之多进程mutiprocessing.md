---
title: python并发编程之多进程mutiprocessing
date: 2018-08-22 18:58:43
tags: python
---

## 一个最基本的例子

```python
from multiprocessing import Process
import time

def print_hello(name):
    time.sleep(3)
    print('hello ' + name)

def main():
    process = Process(target=print_hello, args=('001',))
    process.start()
    process.join()
    process.terminate()

if __name__ == '__main__':
    main()

```

1. Process创建一个子进程实例，接受两个参数，target表示要执行的函数，args是这个函数接受的参数
2. 实例方法`start()`用于启动子进程，`join()`用于同步进程，主程序会等待进程运行结束后进行执行，如果不使用`join()`那么进程异步执行，`terminate()`用于强制终止子进程,不能与join同时使用。

使用要点：

1. args=('001',)参数是一个tuple,所以如果是一个参数则需要以 , 结尾
2. 多进程调用要在`if __name__ == '__main__'`之下执行
