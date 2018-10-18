title: python多线程1 启动与停止线程
author: 李云鹏
date: 2018-10-09 05:51:50
tags:
---
在windows下实现异步编程，个人认为还是使用多线程为佳，在windows下使用多进程会遇到[很多的坑](https://blog.csdn.net/qq_27292549/article/details/80753315),比如创建进程必须要在`if name == __main__`下面，因此需要重新调整软件架构，又比如有的对象不可以被pickle则不能当作参数传递，解决起来十分棘手。

## 启动线程

threading 库可以在单独的线程中执行任何的在 Python 中可以调用的对象。你可以创建一个 Thread 对象并将你要执行的对象以 target 参数的形式提供给该对象。 下面是一个简单的例子：

```python
import time
import sys
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

# Create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()
time.sleep(5)
print('main process over')
sys.exit(0)

```
输出:

```
T-minus 10
T-minus 9
T-minus 8
T-minus 7
T-minus 6
main process over
T-minus 5
T-minus 4
T-minus 3
T-minus 2
T-minus 1
```
* 当你创建好一个线程对象后，该对象并不会立即执行，除非你调用它的 start() 方法（当你调用 start() 方法时，它会调用你传递进来的函数，并把你传递进来的参数传递给该函数）。

* Python中的线程会在一个单独的系统级线程中执行（比如说一个 POSIX 线程或者一个 Windows 线程），这些线程将由操作系统来全权管理。线程一旦启动，将独立执行直到目标函数返回。

* 主线程报错或者主动终止（sys.exit(0)）都不会对子线程产生影响，子线程仍会等待程序执行完毕并退出

## join与查看线程状态

你可以查询一个线程对象的状态，看它是否还在执行：

```python
if t.is_alive():
    print('Still running')
else:
    print('Completed')
```

你也可以将一个线程加入到当前线程，并等待它终止(join的含义是将子线程合并入主线程，由异步变为同步)：

```python
import time
import sys
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

# Create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()
# join
t.join()
time.sleep(5)
print('main process over')
sys.exit(0)
```

输出:
```
T-minus 10
T-minus 9
T-minus 8
T-minus 7
T-minus 6
T-minus 5
T-minus 4
T-minus 3
T-minus 2
T-minus 1
main process over
```

## 守护进程

Python解释器直到所有线程都终止前仍保持运行。如果你希望主线程终止后，子线程自动销毁，可以使用`daemon`参数：
```python
import time
import sys
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

# Create and launch a thread
from threading import Thread
# daemon=True
t = Thread(target=countdown, args=(10,),daemon=True)
t.start()
time.sleep(5)
print('main process over')
sys.exit(0)
```

输出:
```
T-minus 10
T-minus 9
T-minus 8
T-minus 7
T-minus 6
main process over
```
后台线程无法等待，不过，这些线程会在主线程终止时自动销毁。 除了如上所示的两个操作，并没有太多可以对线程做的事情。你无法结束一个线程，无法给它发送信号，无法调整它的调度，也无法执行其他高级操作。

