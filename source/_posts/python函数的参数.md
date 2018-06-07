---
title: python函数的参数
date: 2018-06-07 11:17:37
tags: python
---

## 必选参数

必选参数指调用时必须传入的参数，如果没有传入，python解释器会报错

声明:

```python
def power(x)：
  return x * x
```
调用:

```python
power(10)
100
```

## 默认参数

1. 定义参数时必选参数在前，默认参数在后，否则Python的解释器会报错
2. 定义默认参数时必须指向[不可变对象](http://www.blue7wings.com/python/Python-objects-mutable-vs-immutable.html),否则默认参数的值会随函数调用而变化，造成错误

声明:

```python
def power(x,y = 5):
  return x * y
```
调用:

```python
power(10)
50
power(10,10)
100
power(10,y = 10)
100
```
## 可变参数

1. 可变参数传入的是一个puple
2. 可变参数可以省略

声明:

```python
def printall(*words):
  for word in words:
    print(word)
```
调用:

```python
>>> printall('hello','world')
'hello'
'world'

>>> words = ['hello','world']
>>> printall(*words)
'hello'
'world'
```

words 与 *words: *words代表的是传入的可变参数，例如1,2,3 而words表示有传入的可变参数组成的puple，比如 (1,2,3)

```python
def printall(*words):
  print(*words)
  print(words)

>>> printall(1,2,3)
1 2 3
(1, 2, 3)
```
## 关键字参数

1. 关键字参数传入的是一个字典
2. 关键字参数可以省略

声明：

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

调用:

```python
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}

>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

## 命名关键字参数

声明：

1. 命名关键字参数可以有缺省值，从而简化调用

```python
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
```

调用:

```python
>>> person('Jack', 24, job='Engineer')
Jack 24 Beijing Engineer
```

## 参数组合

参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数