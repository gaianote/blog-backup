title: 使用pyqt5的一些问题以及解决方案
author: 李云鹏
date: 2018-09-13 02:02:10
tags:
---
由于刚开始学习使用pyqt5，对于它的使用原理还不清楚，使用过程中遇到很多的坑，有些虽然解决了，但是还不清楚为什么这样可以解决。由于这个框架非常的庞大，需要长久的学习掌握，遇到的问题先记录下来，之后慢慢更新剖析其原理。

<!--more-->

### 在窗口中使用多进程/弹窗报错

```python
class Uboot(QWidget):
  ...
  def submit(self):
     uboot_test = UbootTest()
     uboot_test.start()
```
报错:

```
QThread: Destroyed while thread is still running
```

修改为:


```python
class Uboot(QWidget):
  ...
  def submit(self):
     self.uboot_test = UbootTest()
     self.uboot_test.start()
```
可以正常运行

对于窗口的显示，同理:
```
class ZeusTester(QMainWindow):
	def __init__(self):
		uboot = Uboot() # 一个widget，这样uboot窗口会显示失败
```
修改为:

```
class ZeusTester(QMainWindow):
	def __init__(self):
		self.uboot = Uboot() # 一个widget
```
uboot窗口显示成功

