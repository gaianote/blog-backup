title: PyQt5学习教程3 center window
author: 李云鹏
date: 2018-09-17 06:37:24
tags:
---
为了使PyQt窗口居中，我们需要使用一些技巧：我们需要获取窗口属性，中心点并自己移动它。在程序开始时，它将位于屏幕的中心。

<!--more-->

我们将QDesktopWidget添加到导入列表中，具有：

```python
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget
```
完整示例：

```python
# 1. 得到窗口的几何形状： PyQt5.QtCore.QRect（0,0,640,480）
qtRectangle = self.frameGeometry()
# 2. 获取屏幕的中心坐标
centerPoint = QDesktopWidget().availableGeometry().center()
# 3. 将屏幕中心设置为几何形状中心
qtRectangle.moveCenter(centerPoint)
# 4. 使用move方法，将窗口左上角移动到几何形状中心左上角
self.move(qtRectangle.topLeft())
```


