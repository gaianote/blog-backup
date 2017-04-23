---
title: 利用Python和win32编程范例
date: 2017-04-23 22:04:01
tags: python
---

学习pywin32之前，我们先要了解一些概念

* 句柄是一个32位整数，在windows中标记对象用，类似一个dict中的key
* 消息是windows应用的重要部分，比如给一个按钮发送BN_CLICKED,按钮就会知道自己被点击了
* 为了方面查找目标窗口的句柄，可以下载一个微软自家的Spy++

使用pip安装pywin32

```bash
pip install pypiwin32
```

快速开始

```python
import win32api
import win32con
win32api.MessageBox(win32con.NULL, 'Python 你好！', '你好', win32con.MB_OK)
```

运行以上程序你会得到一个python版本的弹窗，是不是非常简单呢

## 参考文档

[按需定制一个按键精灵](http://www.orangecube.net/articles/python-win32-example.html)
[Python在Windows下系统编程初步](http://www.linuxidc.com/Linux/2011-12/48525.htm)
