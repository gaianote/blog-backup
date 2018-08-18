---
title: Python异常处理
date: 2018-05-25 09:39:29
tags: python
---

## try...except

```python
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()
```

## 异常处理

### 基础语法如下:

```python
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
```


### 使用raise抛出异常

使用raise会导致程序中断

```python
raise Exception("发生了一些错误，程序中断")
```

## 用户自定义异常

通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。

以下为与RuntimeError相关的实例,实例中创建了一个类，基类为RuntimeError，用于在异常触发时输出更多的信息。

在try语句块中，用户自定义的异常后执行except块语句，变量 e 是用于创建Networkerror类的实例。

```python
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
```
在你定义以上类后，你可以触发该异常，如下所示：

```python
try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e.args
    raise Networkerror("Bad hostname") # raise是用来抛出异常，不适用则不会中断程序
```
