---
title: python多进程
date: 2017-05-21 00:03:44
tags: python
---

## 基本使用

在 `multiprocessing` 中，每一个进程都用一个 `Process` 类来表示。首先看下它的API

```python
Process([group [, target [, name [, args [, kwargs]]]]])
```

- `target` 表示调用对象，你可以传入方法的名字
- `args` 表示被调用对象的位置参数元组，比如target是函数a，他有两个参数m，n，那么args就传入(m, n)即可
- `kwargs` 表示调用对象的字典
- `name` 是别名，相当于给这个进程取一个名字
- `group` 分组，实际上不使用

我们先用一个实例来感受一下：

```python
import multiprocessing

def process(num):
    print ('Process:', num)

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()
```

最简单的创建Process的过程如上所示，target传入函数名，args是函数的参数，是元组的形式，如果只有一个参数，那就是长度为1的元组。

然后调用`start()`方法即可启动多个进程了。

另外你还可以通过 `cpu_count()` 方法还有 `active_children()` 方法获取当前机器的 CPU 核心数量以及得到目前所有的运行的进程。

```python
import multiprocessing
import time

def process(num):
    time.sleep(num)
    print ('Process:', num)

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()

    print('CPU number:' + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print('Child process name: ' + p.name + ' id: ' + str(p.pid))

    print('Process Ended')
```

## Lock

并行输出结果会导致错位，我们可以通过Lock进行加锁

```python
from multiprocessing import Process, Lock
import time


class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
            self.lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10, 15):
        p = MyProcess(i, lock)
        p.start()
```

## Python Queue模块详解

[Python Queue模块详解](http://www.jb51.net/article/58004.htm)