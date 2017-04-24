---
title: python基础教程之操作文件和目录
date: 2017-04-24 10:23:13
tags: python
---

## 环境变量

在操作系统中定义的环境变量，全部保存在os.environ这个变量中

```python
os.environ
os.environ.get('PATH')
```

## 操作文件和目录

**查看当前目录的绝对路径**

```python
dir = os.path.abspath('.')
```

在当前目录操作一个新目录newdir,首先需要得到这个目录的绝对路径


```python
newdir = os.path.join(dir, 'newdir')
```

路径操作不应使用字符串拼接，而应该使用os.path模块;因为不同操作系统的路径分隔符是不同的

**创建新目录**

```python
os.mkdir(newdir)
```

**删除目录**

```python
os.rmdir(newdir)
```

**得到当前目录下所有的文件夹**

```python
[x for x in os.listdir('.') if os.path.isdir(x)]
```

**得到当前目录下所有的.py文件**

```python
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
```