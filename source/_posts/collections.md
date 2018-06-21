---
title: 不可不知的python模块:collections
date: 2018-06-21 14:42:31
tags: python
---

## 基本介绍

我们都知道，Python拥有一些内置的数据类型，比如str, int, list, tuple, dict等， collections模块在这些内置数据类型的基础上，提供了几个额外的数据类型：


* namedtuple(): 生成可以使用名字来访问元素内容的tuple子类
* deque: 双端队列，可以快速的从另外一侧追加和推出对象
* Counter: 计数器，主要用来计数
* OrderedDict: 有序字典
* defaultdict: 带有默认值的字典

## namedtuple()

namedtuple主要用来产生可以使用名称来访问元素的数据对象，通常用来增强代码的可读性， 在访问一些tuple类型的数据时尤其好用。


```python
from collections import namedtuple

website_info_tuple = ('Sohu', 'http://www.google.com/', '张朝阳')
# 生成namedtuple实例
Website = namedtuple('Website', ['name', 'url', 'founder'])
# 将tuple转化为符合Website定义的namedtuple
website = Website._make(website_info_tuple)

>>> website
Website(name='Sohu', url='http://www.google.com/', founder='张朝阳')
>>> website.name
'Sohu'
```
## deque()

### 构造函数

deque其实是 double-ended queue 的缩写，翻译过来就是双端队列

使用构造函数deque()可以将字符串或数组转换为deque实例

```python
from collections import deque
new_deque = deque([1, 2, 3, 4, 5])
deque([1, 2, 3, 4, 5])
new_deque = deque("12345")
deque([1, 2, 3, 4, 5])
```

使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列,当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。


```python
>>> q = deque(maxlen=3)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3], maxlen=3)
>>> q.append(4)
>>> q
deque([2, 3, 4], maxlen=3)
```
如果未传入参数maxlen，则列队长度不受限制

### 实例方法

* 从队列头部快速增加和取出对象: `deque_obj.popleft()`, `deque_obj.appendleft(value)`
* 从末尾快速增加和取出对象: `deque_obj.pop()`, `deque_obj.append(value)`
* 将队尾的对象取出放到队列开头 `deque_obj.rotate()`

是值得注意的是，list对象从队列头部快速增加和取出对象的时间复杂度是 O(n) ，也就是说随着元素数量的增加耗时呈 线性上升。而使用deque对象则是 O(1) 的复杂度，所以当你的代码有这样的需求的时候， 一定要记得使用deque。


##  Counter
计数器是一个非常常用的功能需求，collections也贴心的为你提供了这个功能。

```python
"""
下面这个例子就是使用Counter模块统计一段句子里面所有字符出现次数
"""
from collections import Counter

s = '''A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.'''.lower()

c = Counter(s)
# 获取出现频率最高的5个字符
print c.most_common(5)


# Result:
[(' ', 54), ('e', 32), ('s', 25), ('a', 24), ('t', 24)]
```

## OrderedDict
在Python中，dict这个数据结构由于hash的特性，是无序的，这在有的时候会给我们带来一些麻烦， 幸运的是，collections模块为我们提供了OrderedDict，当你要获得一个有序的字典对象时，用它就对了。

```python
from collections import OrderedDict

items = ( ('A', 1),('B', 2),('C', 3) )

regular_dict = dict(items)
ordered_dict = OrderedDict(items)

print ('Regular Dict:')
for k, v in regular_dict.items():
    print (k, v)

print ('Ordered Dict:')
for k, v in ordered_dict.items():
    print (k, v)


# Result:
Regular Dict:
A 1
C 3
B 2
Ordered Dict:
A 1
B 2
C 3
```

## defaultdict

我们都知道，在使用Python原生的数据结构dict的时候，如果用 d[key] 这样的方式访问， 当指定的key不存在时，是会抛出KeyError异常的。

但是，如果使用defaultdict，只要你传入一个**默认的工厂方法**(如果不传入仍会报错)，那么请求一个不存在的key时， 便会调用这个工厂方法使用其结果来作为这个key的默认值。

他的意义在于，可以利用工厂方法快速构建字典

```python
from collections import defaultdict

>>> default_dict = defaultdict(list)
>>> default_dict['name'].append('lee')
>>> default_dict
defaultdict(<class 'list'>, {'name': ['lee']})

>>> base_dict = {}
>>> base_dict['name'].append('lee')
KeyError: 'name'
```
