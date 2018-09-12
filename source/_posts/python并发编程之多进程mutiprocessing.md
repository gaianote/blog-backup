title: python并发编程之多进程mutiprocessing
tags:
  - python
categories: []
date: 2018-08-22 18:58:00
---
## 进程

### 进程的概念

进程是操作系统中最基本的概念。在多道程序系统出现后，为了刻画系统内部出现的动态情况，描述系统内部各道程序的活动规律引进的一个概念，所有多道程序设计操作系统都建立在进程的基础上。

**狭义定义：**程序的一个执行（运行）实例；

**广义定义：**进程是一个具有一定独立功能的程序，关于某个数据集合的一次运行活动，是系统进行资源分配和调度(执行)的基本单位，是操作系统结构的基础。在早期面向进程设计的计算机结构中，进程是程序的基本执行实体；在当代面向线程设计的计算机结构中，进程是线程的容器。

**进程的概念主要有两点：**

* **进程是一个实体。每一个进程都有它自己的地址空间。**
一般情况下，进程包括文本区域（text region）、数据区域（data region）和堆栈（stack region）。

  * 文本区域，包含程序的源指令；
  * 数据区域，包含了静态变量；
  * 堆，动态内存分区区域；
  * 栈，动态增长与收缩的段，保存本地变量；

* 进程是一个“执行中的程序”。

  程序是一个没有生命的实体，只有处理器赋予程序生命时（执行程序），它才能成为一个活动的实体，我们称其为进程。**程序是指令、数据及其组织形式的描述，进程是程序的实体。**


### 进程的基本状态

* 就绪状态: 分配了除CPU以外所有的资源，只要获得cpu即可执行
* 执行状态
* 阻塞状态: 正在执行的进程由于一些事件无法继续执行，便放弃CPU处于暂停状态。使进程的执行收到阻塞（如访问临界区）
* 挂起状态: 如发现程序有问题，希望暂时停下来，即暂停运行

**同步机制遵循的原则：空闲让进  忙则等待   有限等待  让权等待**

### 进程的通信方式

* **管道（Pipe）**

  管道可用于具有**亲缘关系进程间的通信**，允许一个进程和另一个与它有共同祖先的进程之间进行通信

* **命名管道（namedpipe）**

	命名管道克服了管道没有名字的限制，因此，除了拥有管道的功能外，它还可用于**无亲缘关系进程间的通信**。命名管道在文件系统中有对应的文件名

* **信号（Signal）**

	信号是比较复杂的通信方式，用于通知接受进程有某种事件发生，除了用于进程间通信外，进程还可以发送信号给进程本身

* **消息队列**

	消息队列是消息的链接表，包括Posix消息队列system V消息队列。有足够权限的进程可以向队列中添加消息，被赋予读权限的进程则可以读走队列中的消息。

* **共享内存**

	使得多个进程可以访问同一块内存空间，是最快的可用IPC形式。是针对其他通信机制运行效率较低而设计的。往往与其它通信机制，如信号量结合使用，来达到进程间的同步及互斥

* **内存映射（mappedmemory）**

	**内存映射允许任何多个进程间通信**，每一个使用该机制的进程通过把一个共享的文件映射到自己的进程地址空间

* **信号量（semaphore）**

	主要作为进程间以及同一进程不同线程之间的**同步手段**

* **套接口（Socket）**
	
	常见的进程间通信机制，可用于**不同机器之间的进程间通信**


### 多进程

进程可以创建子进程，子进程是完全独立运行的实体，每个子进程都拥有自己的私有系统状态和执行主线程。因为子进程是独立的，所以它可以与父进程并发执行。也就是说，父进程可以处理事件1，同时，子进程可以在后台处理事件2。

使用多个进程或线程时，操作系统负责安排它们的工作。具体做法是：给每个进程(线程)安排一个小的时间片，并在所有的任务之间快速轮询，给每个任务分配一部分可用的CPU时间。如系统同时运行10个进程，操作系统会给每个进程分配1/10的CPU时间，在10个进程之间快速轮询。在具有多个CPU的系统上，操作系统可以尽可能使用每个CPU，从而并发执行进程。

## Python与并发编程

Python支持线程，但是Python的线程受到很多限制，因为Python解释器使用了内部的全局解释锁(GIL)，Python的执行由Python虚拟机控制，Python解释器可以运行多个线程，但是任意时刻只允许单个线程在解释器中执行，对Python虚拟机的访问由全局解释锁(GIL)控制。

**GIL保证同一个时刻仅有一个线程在解释器中执行。无论系统上有多少个CPU，Python只能在一个CPU上运行。**(使用GIL的原因，在多线程访问数据时，保证数据安全)

如果线程涉及大量的CPU操作，使用线程会降低程序的运行速度。

常见解决GIL锁的方法：使用多进程，将程序设计为大量独立的线程集合。

## multiprocessing模块

multiprocessing模块为在**子进程**中运行任务、通信、共享数据，以及执行各种形式的同步提供支持。该模块更适合在UNIX下使用。

这个模块的接口与threading模块的接口类似。**但是和线程不同，进程没有任何共享状态，因此，如果某个进程修改了数据，改动只限于该进程内，并不影响其他进程。**

(不同进程内，id(10)是不一样的，因为每个进程是相互独立的)

### Process

`Process(group=None, target=None, name=None, args=(), kwargs={})`

这个类构造了一个Process进程。表示一个运行在子进程中的任务，**应使用关键字参数来指定构造函数中的参数**。

**如果一个类继承了Process，在进行有关进程的操作前，确保调用了Process的构造函数。**

* `group` 预留参数，一直为None
* `target` 进程启动时执行的可调用对象，由run()方法调用
* `name` 进程名
* `args` target处可调用对象的参数，如果可调用对象没有参数，不用赋值
* `kwargs` target处可调用对象的关键字参数

**Process的实例p具有的属性:**

* `p.is_alive()` 如果p在运行，返回True

* `p.join([timeout])` 等待进程p运行结束。`timeout`是可选的超时期限。如果timeout为None，则认为要无限期等待

* `p.run()` 进程启动时运行的方法。默认情况下，会调用传递给Process构造函数中的target；定义进程的另一种方法是继承Process并重写run()方法

* `p.start()` 运行进程p，并调用p.run()

* `p.terminate()` 强制杀死进程。如果调用此方法，进程p将被立即终止，同时不会进行任何清理动作。如果进程p创建了自己的子进程，这些进程将会变成 **僵尸进程**,此方法要小心使用

  > If this method is used when the associated process is using a pipe or queue then the pipe or queue is liable to become corrupted and may become unusable by other process. Similarly, if the process has acquired a lock or semaphore etc. then terminating it is liable to cause other processes to deadlock.

* `p.authkey` 进程的身份验证键

* `p.daemon` 守护进程标志，布尔变量。指进程是否为后台进程。如果该进程为后台进程(daemon = True)，当创建它的Python进程终止时，后台进程将自动终止; 其中`p.daemon`的值要在使用`p.start()`启动进程之前设置,并且禁止后台进程创建子进程

   * `p.daemon = True` 主进程终止,子进程终止,
   * `p.daemon = False` 主进程终止,子进程不会终止


* `p.exitcode` 进程的整数退出码。如果进程仍在运行，值为None。如果值为-N，表示进程由信号N终止

* `p.name` 进程名

* `p.pid` 进程号

  > Note that the start(), join(), is_alive(), terminate() and exitcode methods should only be called by the process that created the process object.

#### 一个最基本的例子

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

### Queue

multiprocessing模块支持的进程间通信的方式：**管道和队列**。这两种方法都是使用**消息传递实现的。**

`Queue([size])`创建一个共享的进程队列

size为队列的最大长度，默认为无大小限制。
底层使用管道，锁和信号量实现。利用线程将队列中的数据传输到管道。

[Queue](https://docs.python.org/2/library/multiprocessing.html#multiprocessing.Queue)的实例q具有以下方法。

* `q.qsize()` 返回队列中成员的数量,**但是此结果并不可靠**，因为多线程和多进程，在返回结果和使用结果之间，队列中可能添加/删除了成员。

* `q.empty()` 如果调用此方法时，q为空，返回True ,**但是此结果并不可靠**，因为多线程和多进程，在返回结果和使用结果之间，队列中可能添加/删除了成员。

* `q.full()`如果调用此方法时，q已满，返回True,**但是此结果并不可靠**，因为多线程和多进程，在返回结果和使用结果之间，队列中可能添加/删除了成员。


* `q.put(obj[, block[, timeout]])` 将obj放入队列中。如果队列已满，此方法将阻塞至队列有空间可用为止
	* `block` 控制阻塞行为，默认为True；如果设置为False，将obj放入队列时，如果没有可用空间的话，将引发Queue.Full异常;
   * `timeout`为阻塞时间，超时后将引发Queue.Full异常。默认为无限制等待。


* `q.put_nowait(obj)` 等价于q.put(obj,False)

* `q.get([block[, timeout]])` 返回q中的一个成员。如果队列为空，此方法将阻塞至队列中有成员可用为止
	* block控制阻塞行为，默认为True；如果设置为False，如果队列中没有可用成员，将引发Queue.Empty异常
	* timeout为阻塞的时间，超时后将引发Queue.Empty异常。默认为无限制等待。

* `q.get_nowait()` 等价于q.(get,False)

* `q.close()` 关闭队列，防止队列中放入更多数据。调用此方法时，后台线程将继续写入那些已入队列但尚未写入的数据，待这些数据写入完成后将马上关闭队列

  * q在被垃圾回收时将调用此方法
  * q被关闭后，`q.get()`可以正常使用; `q.put()`,`q.qsize()`,`q.empty()`,`q.full()`等操作会抛出异常

* `q.join_thread()` **此方法用于q.close()后，**等待后台线程运行完成，阻塞主线程至后台线程运行结束，保证缓冲区中的数据放入管道
调用`q.cancel_join_thread()`可禁止此行为。

* `q.cancel_join_thread()` 阻止q.join_thread()阻塞主线

重写Process的run方法，实现生产者消费者模型：

```python
import multiprocessing,time
class Consumer(multiprocessing.Process):
    def __init__(self,queue,lock):
        super().__init__()
        self.queue = queue
        self.lock = lock

    def run(self,):
        times = 5
        while True:
            time.sleep(1)
            times -= 1
            i = self.queue.get()
            print ('get = %s, %s'%(i,type(i)))

class Producer(multiprocessing.Process):
    def __init__(self,queue,lock):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.lock = lock

    def run(self,):
        times = 10
        while times:
            times -= 1
            self.queue.put(times)
            print ('put = %s'%(times))
            time.sleep(0.5)


if __name__ == "__main__":
    q = multiprocessing.Queue()
    lock = multiprocessing.Lock()

    a = Consumer(q,lock)
    a.start()

    b = Producer(q,lock)
    b.start()
```
在两个类中分别重写run方法，实现起来比较繁琐，而且人为的分离有时可能违背了面向对象编程的本意，建议在同一个类中实现多进程即可

## 在一个类中实现生成者消费者模型

```python
import multiprocessing,time
from functools import wraps

def sync(func):
    '''装饰器sync'''
    '''开启一个新的进程启动该函数从而达到异步的效果'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = multiprocessing.Process(target = func,args=args, kwargs=kwargs)
        result.start()
        return result
    return wrapper
class Readline(object):
    """在一个类内实现生产者消费者模型，使用queue进行通信"""
    def __init__(self):
        self.queue = multiprocessing.Queue()
    @sync
    def readline(self,msg):
        '''
        生产者:异步
        模拟读取信息流等需要快速获取的信息，比如串口信息，如果在获取的同时进行处理等耗时操作，可能会导致信息丢失
        '''
        print(msg)
        for i in range(10):
            time.sleep(0.5)
            print('put line :',i)
            self.queue.put(i)


    def findline(self,line):
        '''
        消费者:同步
        模拟一些耗时的操作
        '''
        while True:
            getline = self.queue.get()
            if line == getline:
                print('found:',line)
                break
if __name__ == '__main__':
   c = Readline()
   c.readline(msg = 'hellow world!')
   c.findline(3)
   c.findline(5)

```
输出结果：
```
hellow world!
put line : 0
put line : 1
put line : 2
put line : 3
found: 3
put line : 4
put line : 5
found: 5
put line : 6
put line : 7
put line : 8
put line : 9
```

## 参考资料

[Python 多进程编程 - multiprocessing模块](https://blog.csdn.net/lis_12/article/details/54564703)