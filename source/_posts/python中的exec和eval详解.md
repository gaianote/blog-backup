---
title: python中的exec和eval详解
date: 2018-06-27 15:17:23
tags: python
---

## 简介

python 动态执行字符串代码片段（也可以是文件）， 一般会用到exec,eval。

## exec

exec(function[, globals[, locals]])

如果指定了`global_dic`和`local_dic`，exec便不会访问全局作用域中的变量,如果global_dic没有包含全部的所需的变量则会报错。

```python
a=10
b=20
c=20
global_dic = {'a':6,'b':8}
local_dic = {'b':9,'c':10}
exec ("global a;print(a,b,c);",global_dic,local_dic)
# 6 9 10 local_dic=> global_dic
```

## eval

eval通常用来执行一个字符串表达式，并返回表达式的值。注意的是，eval的参数不能是函数字符串等，否则会报错。而exec可以接受一个函数字符串作为参数并运行它

eval(expression[, globals[, locals]])

有三个参数，表达式字符串，globals变量作用域，locals变量作用域。 其中第二个和第三个参数是可选的。

如果忽略后面两个参数，则eval在当前作用域执行。

```python
>>> a=1
>>> eval("a+1")
2
```

## 注意

由于有时exec和eval可能会改变全局变量的值，所以在遇到时应该首先考虑其它使用方式。