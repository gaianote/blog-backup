---
title: python类的继承
date: 2018-05-24 15:17:21
tags: python
---

## 概述　

面向对象编程 (OOP) 语言的一个主要功能就是“继承”。继承是指这样一种能力：它可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展。

## 类的继承

### 继承的定义

```python
class Person(object):   # 定义一个父类
 
    def talk(self):    # 父类中的方法
        print("person is talking....")  
 
 
class Chinese(Person):    # 定义一个子类， 继承Person类
 
    def walk(self):      # 在子类中定义其自身的方法
        print('is walking...')
 
c = Chinese()
c.talk()      # 调用继承的Person类的方法
c.walk()     # 调用本身的方法
 
# 输出
 
person is talking....
is walking...
```

### 构造函数的继承
　
如果我们要给实例 c 传参，我们就要使用到构造函数，那么构造函数该如何继承，同时子类中又如何定义自己的属性？

继承类的构造方法：

1. 经典类的写法： 父类名称.__init__(self,参数1，参数2，...)

2. 新式类的写法：super(子类，self).__init__(参数1，参数2，....)

```python
class Person(object):
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'
 
    def talk(self):
        print("person is talking....")
 
 
class Chinese(Person):
 
    def __init__(self, name, age, language):  # 先继承，在重构
        Person.__init__(self, name, age)  #继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
        self.language = language    # 定义类的本身属性
 
    def walk(self):
        print('is walking...')
 
 
class American(Person):
    pass
 
c = Chinese('bigberg', 22, 'Chinese')
```

如果我们只是简单的在子类Chinese中定义一个构造函数，其实就是在重构。这样子类就不能继承父类的属性了。所以我们在定义子类的构造函数时，要先继承再构造，这样我们也能获取父类的属性了。

子类构造函数基础父类构造函数过程如下：

实例化对象c ----> c 调用子类__init__()  ---- > 子类__init__()继承父类__init__()  ----- > 调用父类 __init__()


### 子类对父类方法的重写

如果我们对基类/父类的方法需要修改，可以在子类中重构该方法。如下的talk()方法　

```
class Person(object):
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'
 
    def talk(self):
        print("person is talking....")
 
class Chinese(Person):
 
    def __init__(self, name, age, language): 
        Person.__init__(self, name, age) 
        self.language = language
        print(self.name, self.age, self.weight, self.language)
 
    def talk(self):  # 子类 重构方法
        print('%s is speaking chinese' % self.name)
 
    def walk(self):
        print('is walking...')
 
c = Chinese('bigberg', 22, 'Chinese')
c.talk()
 
# 输出
bigberg 22 weight Chinese
bigberg is speaking chinese
```

## 参考资料

[python类的继承](https://www.cnblogs.com/bigberg/p/7182741.html)