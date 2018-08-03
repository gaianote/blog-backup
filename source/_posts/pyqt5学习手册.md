---
title: pyqt5学习手册
date: 2018-08-03 13:30:12
tags:
---

PyQt5 是Digia的一套Qt5与python绑定的应用框架，同时支持2.x和3.x。本教程使用的是3.x。Qt库由Riverbank Computing开发，是最强大的GUI库之一 ，官方网站：www.riverbankcomputing.co.uk/news。

<!--more-->

## 关于 PyQt5

PyQt5是由一系列Python模块组成。超过620个类，6000和函数和方法。能在诸如Unix、Windows和Mac OS等主流操作系统上运行。PyQt5有两种证书，GPL和商业证书。

PyQt5类分为很多模块，主要模块有：

* `QtCore` 包含了核心的非GUI的功能。主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用。
* `QtGui` 包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类。
    * `QIcon('web.png')` 创建一个QIcon(显示图标)对象，接受一个图片路径作为参数
* `QtWidgets` 类包含了一系列创建桌面应用的UI元素[必要]
    * `app = QApplication(sys.argv)` 用于创建一个应用对象[必要]
    * `window = QWidget()` 用于创建用户界面
    * `QColorDialog` 提供颜色的选择
    * `QFontDialog` 能做字体的选择
    * `QInputDialog` 提供了一个简单方便的对话框，可以输入字符串，数字或列表
    * `QFileDialog` 给用户提供文件或者文件夹选择的功能。能打开和保存文件
    * `hbox = QHBoxLayout()` 水平盒子布局
    * `vbox = QVBoxLayout()` 垂直盒子布局
    * `grid = QGridLayout()` 栅格布局
* `QtMultimedia` 包含了处理多媒体的内容和调用摄像头API的类。
* `QtBluetooth` 模块包含了查找和连接蓝牙的类。
* `QtNetwork` 包含了网络编程的类，这些工具能让TCP/IP和UDP开发变得更加方便和可靠。
* `QtPositioning` 包含了定位的类，可以使用卫星、WiFi甚至文本。
* `Engine` 包含了通过客户端进入和管理Qt Cloud的类。
* `QtWebSockets` 包含了WebSocket协议的类。
* `QtWebKit` 包含了一个基WebKit2的web浏览器。
* `QtWebKitWidgets` 包含了基于QtWidgets的WebKit1的类。
* `QtXml` 包含了处理xml的类，提供了SAX和DOM API的工具。
* `QtSvg` 提供了显示SVG内容的类，Scalable Vector Graphics (SVG)是一种是一种基于可扩展标记语言（XML），用于描述二维矢量图形的图形格式（这句话来自于维基百科）。
* `QtSql` 提供了处理数据库的工具。QtTest提供了测试PyQt5应用的工具。

## 安装PyQt5

```bash
pip install pyqt5
```

## hello PyQt5！

### 例一： 简单的小窗口

这个简单的小例子展示的是一个小窗口。但是我们可以在这个小窗口上面做很多事情，改变大小，最大化，最小化等，这需要很多代码才能实现。这在很多应用中很常见，没必要每次都要重写这部分代码，Qt已经提供了这些功能。PyQt5是一个高级的工具集合，相比使用低级的工具，能省略上百行代码。

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = QWidget()

    window.resize(250, 150)
    window.move(300, 300)
    window.setWindowTitle('Simple')
    window.show()

    sys.exit(app.exec_())
```

运行上面的代码，能展示出一个小窗口。

#### 基本流程解析

1. 创建一个应用实例和用户界面实例，这是所有PyQt5程序所必须的操作

```python
app = QApplication(sys.argv)
window = QWidget()
```

2. 使用 window 实例方法操作 window

```python
window.resize(250, 150)
window.move(300, 300)
window.setWindowTitle('Simple')
window.show()
```
其中:

`resize()` 方法能改变控件的大小，这里的意思是窗口宽250px，高150px。
`move()` 是修改控件位置的的方法。它把控件放置到屏幕坐标的(300, 300)的位置。注：屏幕坐标系的原点是屏幕的左上角。
`setWindowTitle()` 用于为窗口添加标题，标题在标题栏展示
`show()`能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。

3. 安全退出主循环

```python
sys.exit(app.exec_())
```


程序预览：

![img](https://maicss.gitbooks.io/pyqt5/content/images/1-simple.png)

### 例2，面向对象编程

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

面向对象编程最重要的三个部分是类(class)、数据和方法。我们创建了一个类的调用，这个类继承自`QWidget`。这就意味着，我们调用了两个构造器，一个是这个类本身的，一个是这个类继承的。`super()`构造器方法返回父级的对象。`__init__()`方法是构造器的一个方法。

1. 创建新类并继承`QWidget` ，紧接着调用`super().__init__()`方法，如此 self 便能在类中调用 `QWidget` 实例的全部方法了,通常我们对于程序的操作都是基于 `QWidget` 进行的

```python
class Example(QWidget):

    def __init__(self):
        super().__init__()
```

2. 创建 `initUI` 并在 `__init__`方法内调用它，

```python
def __init__(self):
    # ...
    self.initUI()

def initUI(self):

    self.setGeometry(300, 300, 300, 220)
    self.setWindowTitle('Icon')
    self.setWindowIcon(QIcon('web.png'))

    self.show()
```

3. 应用和示例的对象创立，主循环开始。

```python
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```


程序预览：
![img](https://maicss.gitbooks.io/pyqt5/content/images/1-icon.png)

### 例3，提示框

```python
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

在这个例子中，我们为应用创建了一个提示框。

```python
QToolTip.setFont(QFont('SansSerif', 10))

```
这个静态方法设置了提示框的字体，我们使用了10px的SansSerif字体。

```python
self.setToolTip('This is a <b>QWidget</b> widget')

```
调用`setTooltip()`创建提示框可以使用富文本格式的内容。

```python
btn = QPushButton('Button', self)
btn.setToolTip('This is a <b>QPushButton</b> widget')

```
创建一个按钮，并且为按钮添加了一个提示框。

```python
btn.resize(btn.sizeHint())
btn.move(50, 50)

```
调整按钮大小，并让按钮在屏幕上显示出来，`sizeHint()`方法提供了一个默认的按钮大小。
程序预览：

！[img](https://maicss.gitbooks.io/pyqt5/content/images/1-tooltips.png)

### 例4，关闭窗口

关闭一个窗口最直观的方式就是点击标题栏的那个叉，这个例子里，我们展示的是如何用程序关闭一个窗口。这里我们将接触到一点single和slots的知识。
本例使用的是QPushButton组件类。

```
QPushButton(string text, QWidget parent = None)

```
`text`参数是想要显示的按钮名称，`parent`参数是放在按钮上的组件，在我们的 例子里，这个参数是`QWidget`。应用中的组件都是一层一层（继承而来的？）的，在这个层里，大部分的组件都有自己的父级，没有父级的组件，是顶级的窗口。

```python
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

这里创建了一个点击之后就退出窗口的按钮。

```python
from PyQt5.QtCore import QCoreApplication

```
程序需要`QtCore`对象。

```python
qbtn = QPushButton('Quit', self)

```
创建一个继承自`QPushButton`的按钮。第一个参数是按钮的文本，第二个参数是按钮的父级组件，这个例子中，父级组件就是我们创建的继承自`Qwidget`的`Example`类。

```python
qbtn.clicked.connect(QCoreApplication.instance().quit)

```

事件传递系统在PyQt5内建的single和slot机制里面。点击按钮之后，信号会被捕捉并给出既定的反应。`QCoreApplication`包含了事件的主循环，它能添加和删除所有的事件，`instance()`创建了一个它的实例。`QCoreApplication`是在`QApplication`里创建的。 点击事件和能终止进程并退出应用的quit函数绑定在了一起。在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。
程序预览：

![image](https://maicss.gitbooks.io/pyqt5/content/images/1-quitbutton.png)

### 例5，消息盒子

默认情况下，我们点击标题栏的×按钮，QWidget就会关闭。但是有时候，我们修改默认行为。比如，如果我们打开的是一个文本编辑器，并且做了一些修改，我们就会想在关闭按钮的时候让用户进一步确认操作。

```python

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

如果关闭QWidget，就会产生一个QCloseEvent。改变控件的默认行为，就是替换掉默认的事件处理。

```python
reply = QMessageBox.question(self, 'Message',
    "Are you sure to quit?", QMessageBox.Yes |
    QMessageBox.No, QMessageBox.No)

```
我们创建了一个消息框，上面有俩按钮：Yes和No.第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的。返回值在变量`reply`里。

```python
if reply == QtGui.QMessageBox.Yes:
    event.accept()
else:
    event.ignore()

```
这里判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否者就忽略关闭事件。
程序预览：

![img](https://maicss.gitbooks.io/pyqt5/content/images/1-messagebox.png)

### 例6，窗口居中

```python
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

`QtGui.QDesktopWidget`提供了用户的桌面信息，包括屏幕的大小。

```
self.center()

```
这个方法是调用我们下面写的，实现对话框居中的方法。

```
qr = self.frameGeometry()

```
得到了主窗口的大小。

```
cp = QDesktopWidget().availableGeometry().center()

```
获取显示器的分辨率，然后得到中间点的位置。

```
qr.moveCenter(cp)

```
然后把自己窗口的中心点放置到qr的中心点。

```
self.move(qr.topLeft())

```
然后把窗口的坐上角的坐标设置为qr的矩形左上角的坐标，这样就把窗口居中了。
程序预览：

## 布局管理

在一个GUI程序里，布局是一个很重要的方面。布局就是如何管理应用中的元素和窗口。有两种方式可以搞定：绝对定位和PyQt5的layout类

绝对定位就是通过 `move(x,y)` 方法定位每一个元素，而layout类分为盒布局和栅格布局

### 盒布局

```python
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

#### 核心步骤解析

1. 创建一个水平布局盒子实例 hbox

```python
hbox = QHBoxLayout()
```

2. 在水平布局盒子左面添加一个弹性空间

```python
hbox.addStretch(1)
```

3. 将创建好的组件添加进布局盒子中

```python
hbox.addWidget(okButton)
hbox.addWidget(cancelButton)
```

4. 创建一个竖直布局盒子,在组件上面加入弹性空间，接着将 hbox 添加入 vbox

```python
vbox = QVBoxLayout()
vbox.addStretch(1)
vbox.addLayout(hbox)
```

5. 最后，将布局添加入windows

```
self.setLayout(vbox)
```

### 栅格布局

## 事件和信号

所有的应用都是事件驱动的。事件大部分都是由用户的行为产生的，当然也有其他的事件产生方式，比如网络的连接，窗口管理器或者定时器等。调用应用的exec_()方法时，应用会进入主循环，主循环会监听和分发事件。

在事件模型中，有三个角色：

* 事件源
* 事件
* 事件目标

事件源就是发生了状态改变的对象。事件是这个对象状态的改变撞他改变的内容。事件目标是事件想作用的目标。事件源绑定事件处理函数，然后作用于事件目标身上。

PyQt5处理事件方面有个signal and slot机制。Signals and slots用于对象间的通讯。事件触发的时候，发生一个signal，slot是用来被Python调用的，slot只有在事件触发的时候才能调用。

## 对话框


## 参考手册

[PyQt5中文教程](https://maicss.gitbooks.io/pyqt5/content/hello_world.html)