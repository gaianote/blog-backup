title: ' Python多进程锁 multiprocessing.Lock()与内存共享'
author: 李云鹏
date: 2018-09-08 07:44:08
tags:
---
## 多进程锁

当我们用多进程来读写文件的时候，一个进程是写文件，一个进程是读文件，如果两个文件同时进行，肯定是不行的，必须是文件写结束后，才可以进行读操作。因此，我们需要使用进程锁来保证，写进程完成后读进程才开始运行。

<!--more-->

```
多进程的读写操作，由于进程同时进行会造成结果混乱
p1 = multiprocessing.Process(target=write) 
p2 = multiprocessing.Process(target=read)
```

我们可以使用`multiprocessing.Lock()`生成一个锁，任何使用此锁的函数(同一个或不同)，被进程调用后，都会等待锁释放后才会被其它进程锁调用

```
lock = multiprocessing.Lock()
lock.acquire() # 获得锁
lock.release() # 释放锁
with lock:
   # 获得锁，等待运行结束后释放锁，并自动处理错误
   # 由于lock.acquire()需要手动处理错误，因此建议使用with lock
```

一个简单的示例：

```python
import multiprocessing
import time
def add(number,value,lock):
    # 获取锁，lock是multiprocessing.Lock的一个实例
    with lock:
        print("init add{0} number = {1}".format(value, number))
        for i in range(1, 6):
            number += value
            time.sleep(1)
            print("add{0} number = {1}".format(value, number))

def plus(number,value,lock):
    # 此处的lock与add中的lock是一个锁，所以会等待add的锁释放后才会运行plus锁内的代码
    with lock:
        print("init plus{0} number = {1}".format(value, number))
        for i in range(1, 6):
            number += value
            time.sleep(1)
            print("plus{0} number = {1}".format(value, number))

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    number = 0
    p1 = multiprocessing.Process(target=add,args=(number, 1, lock))
    p2 = multiprocessing.Process(target=plus,args=(number, 3, lock))
    p1.start()
    p2.start()
    print("main end")
```

输出结果：

```
main end
init add1 number = 0
add1 number = 1
add1 number = 2
add1 number = 3
add1 number = 4
add1 number = 5
init plus3 number = 0
plus3 number = 3
plus3 number = 6
plus3 number = 9
plus3 number = 12
plus3 number = 15
```
## 内存共享

我们可以使用`multiprocessing.Value('i', 0)`生成一个保存数字的Value实例，这个实例对于所有调用它的进程而言是共享的.

```python
import multiprocessing
import time
def add(number,value,lock):
    with lock:
        print("init add{0} number = {1}".format(value, number.value))
        for i in range(1, 6):
            number.value  += value
            time.sleep(1)
            print("add{0} number = {1}".format(value, number.value))

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    number = multiprocessing.Value('i', 0)
    p1 = multiprocessing.Process(target=add,args=(number, 1, lock))
    # number.value的值此时已经变为了5
    p2 = multiprocessing.Process(target=add,args=(number, 3, lock))
    p1.start()
    p2.start()
    print("main end")
```
输出:

```
main end
init add1 number = 0
add1 number = 1
add1 number = 2
add1 number = 3
add1 number = 4
add1 number = 5
init add3 number = 5
add3 number = 8
add3 number = 11
add3 number = 14
add3 number = 17
add3 number = 20
```
