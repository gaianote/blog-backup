---
title: python协程与异步IO
date: 2017-04-23 22:07:42
tags: python
---

## 协程

协程的用途在于IO，遇到IO就挂起，并发执行另一个任务，比如http请求，可以实现同时请求若干个网站的目的
但是很多经典库比如requests并不支持协程

### 生成器与协程

* PEP-0492 通过使用 async 关键字显式的对生成器和协程做了区分。
* 实际上，使用async显示声明协程（函数），并在函数内使用wait代替yield，一个协程变诞生了

### 生成器

* yield的功能类似于return，但是不同之处在于它返回的是生成器
* 生成器是通过一个或多个yield表达式构成的函数，每一个生成器都是一个迭代器(for循环或while循环)
* 如果一个函数包含yield关键字，这个函数就会变为一个生成器。
* 生成器并不会一次返回所有结果，而是每次遇到yield关键字后返回相应结果，并保留函数当前的运行状态，等待下一次的调用。
* 由于生成器也是一个迭代器，那么它就应该支持next方法来获取下一个值

```python
def func():
     n = 0
     print(n)
     while 1:
        print(n,'a')
        n = yield n #可以通过send函数向n赋值
        print(n,'b')

f = func()
print(f)
# 生成一个<generator object func at 0x030489F0>

f.send(None) # 启动生成器
# f.send(None)遇到yield 中断
0
0 a

f.send(1)
# n被赋值为1，循环遇到yield中断
1 b
1 a

f.send(2)
# f.send(2)，n被赋值为2，循环遇到yield中断
2 b
2 a
```

### 生产者-消费者模型

传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高

```python
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
```

执行过程分析

1. c = consumer(),生成generator
2. c.send(None)其实等价于next(c),第一次执行时其实只执行到n = yield r就停止了，然后把r的值返回给调用者。用于启动生成器
3. yield r是一个表达式，通过send(msg)被赋值，而send(msg)是有返回值的，返回值为：下一个yield r表达式的参数，即为r。
4. produce一旦生产了东西，通过c.send(n)切换到consumer执行。consumer通过yield拿到消息，处理，又通过yield把结果传回。也就是说，c.send(1) 不但会给 c 传送一个数据，它还会等着下次 yield 从 c 中返回一个数据，它是有返回值的，一去一回才算完，拿到了返回的数据(200 OK)才继续下面执行。
5. 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

## asyncio

asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持

```python
import time
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world!')
    yield from asyncio.sleep(1)
    print('Hello end!')
tasks = [hello(), hello()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

两个hello()是由同一个线程并发执行的,返回结果为

```python
# 单线程依次执行print('Hello world!')
Hello world!
Hello world!
# 执行异步操作asyncio.sleep(1)
暂停1s
# 单线程依次执行print('Hello end!')
Hello end!
Hello end!
```

## async/await

async/await是自python 3.5开始后asyncio实现的新语法

* 把@asyncio.coroutine替换为async；
* 把yield from替换为await。

```python
async def hello():
    print("Hello start!")
    r = await asyncio.sleep(1)
    print("Hello end!")
```

## aiohttp

asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。

如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。

asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。

```bash
pip install aiohttp
```


```python
import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5) # 模拟io阻塞
    return web.Response(body=b'<h1>Index</h1>',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
```


[python并发之协程](http://blog.csdn.net/dutsoft/article/details/54729480)
[python:利用asyncio进行快速抓取](http://developer.51cto.com/art/201403/434352_all.htm)
[玩转 Python 3.5 的 await/async](https://www.oschina.net/translate/playing-around-with-await-async-in-python-3-5)
[Python 3.5 协程究竟是个啥](http://www.tuicool.com/articles/V7jQbmU)