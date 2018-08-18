---
title: python规范目录结构
date: 2017-04-23 22:07:42
tags: python
---

假设项目名称为Foo

```
Foo/
|-- bin/ #存放项目的一些可执行文件
|   |-- foo
|-- foo/ # 所有模块、包都应该放在此目录，程序的入口最好命名为main.py
|   |-- tests/ # 存放单元测试代码；
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |-- __init__.py
|   |-- main.py
|-- docs/ # 用于存放文档
|   |-- conf.py
|   |-- abc.rst
|-- setup.py # 来管理代码的打包、安装、部署问题
|-- requirements.txt # 存放软件依赖的外部Python包列表
|-- README # 项目说明文件
```
[python基础6--目录结构](http://www.cnblogs.com/bigberg/p/6423164.html)