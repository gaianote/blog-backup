title: PyQt5学习教程12 单选按钮
author: 李云鹏
date: 2018-09-18 03:04:00
tags:
---
## QRadioButton简介


`QRadioButton`小部件提供了一个带有文本标签的单选按钮（没错，本质上它还是一个按钮）。

`QRadioButton`是一个选项按钮，可以打开（选中）或关闭（取消选中）。单选按钮通常为用户提供“多选一”操作。在一组单选按钮中，一次只能检查一个单选按钮;如果用户选择另一个按钮，则先前选择的按钮被关闭。

单选按钮默认为autoExclusive（自动互斥）。如果启用了自动互斥功能，则属于同一个父窗口小部件的单选按钮的行为就属于同一个互斥按钮组的一部分。当然加入`QButtonGroup`中能够实现多组单选按钮互斥。

无论何时打开或关闭按钮，都会发出`toggled()`信号。如果要在每次按钮更改状态时触发某个操作，请连接到此信号。使用`isChecked()`来查看是否选择了一个特定的按钮。

就像QPushButton一样，单选按钮显示文本，还可以选择一个小图标。该图标是用`setIcon()`设置的。文本可以在构造函数中设置，也可以在`setText()`中设置。快捷键可以通过在文本前面加一个＆符号来指定。

<!--more-->
![img](/images/Snipaste_2018-09-18_11-53-12.png)

## 基本示例

```python
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(230, 40))
        self.setWindowTitle("Checkbox")
        # 1. 实例化raidobutton
        self.raido_yes = QRadioButton("是",self)
        self.raido_no = QRadioButton("否",self)
        # 2. 实例化QButtonGroup
        self.buttongroup = QButtonGroup(self)
        self.buttongroup.addButton(self.raido_yes,1)
        self.buttongroup.addButton(self.raido_no,2)
        # 3. 连接槽函数
        self.buttongroup.buttonClicked.connect(self.bgclicked)
        # 4. 调整按钮位置
        self.raido_yes.move(30,30)
        self.raido_no.move(80,30)

    def bgclicked(self):
        # 通过checkedId的方式判断某个单选按钮是否被勾选
        sender = self.sender()
        if sender == self.buttongroup:
            if self.buttongroup.checkedId() == 1:
                print('checkedId:是')

            elif self.buttongroup.checkedId() == 2:
                print('checkedId:否')
        # 通过isChecked的方式判断某个单选按钮是否被勾选
        if self.raido_yes.isChecked():
            print('isChecked:是')
        elif self.raido_no.isChecked():
            print('isChecked:否')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )

```

## 常用语法

**1.实例化一个单选按钮**

```python
self.radiobutton1 = QRadioButton('单选按钮1',self)
self.radiobutton2 = QRadioButton('单选按钮2',self)
```
**2.实例化一个按钮组**

其中`addButton`接受两个参数，第一个参数是添加入按钮组的按钮，第二个参数是分配给该按钮的id

```
self.buttongroup1 = QButtonGroup(self)
self.buttongroup1.addButton(self.radiobutton1,11)
```

**3.为按钮组连接槽函数**

```python
self.buttongroup1.buttonClicked.connect(self.bgclicked)
self.buttongroup2.buttonClicked.connect(self.bgclicked)
```

**4.得知是那个按钮组被点击**

```python
def bgclicked(self):
  sender = self.sender()
  if sender == self.buttongroup1:
    ...
  elif sender == self.buttongroup1:
    ...
```

**5.得知是哪个按钮被点击**

```python
def bgclicked(self):
  if self.buttongroup1.checkedId() == 11:
    ...
```
