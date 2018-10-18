---
title: python面向对象编程
date: 2018-05-29 18:58:35
tags: python
---

## 继承

### 理解Python中super()和__init__()方法

我试着理解super()方法.从表面上看,两个子类实现的功能都一样.我想问它们俩的区别在哪里?

```python
class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__() # 这里无需传入参数self

class ChildC(Base):
    def __init__(self):
        super().__init__() # python3中 可以用super().__init__()替换super(ChildB, self).__init__()
        print(self.name)

print ChildA(),ChildB()
```

super()的好处就是可以避免直接使用父类的名字.

### 多重继承

通过多重继承，一个子类就可以同时获得多个父类的所有功能,从而可以避免设计复杂的层级继承关系。这种设计模式称为MixIn

为了**更好地看出继承关系**，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：

```python
class Dog(Animal, RunnableMixIn, CarnivorousMixIn):
    pass
```

### 方法组合

除了多重继承，我们还可以通过方法组合的方式灵活获得一个工具类，可以需要实际需求进行选取

```python
class GameObject(object):
    def __init__(self):
        self.player = Player()
        self.friend = friend()
```