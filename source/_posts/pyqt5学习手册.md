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

![img](/images/b04ef8edf2df447c9007ac4c1860a2db.png)
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
![img](/images/dce8fd834a1049e3b9e42aff7ec810a9.png)
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

![img](/images/6ad746d0d0244e3986031b8e537b42bf.png)
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

![image](/images/f112afbd15fb4ca5903c694531a25690.png)
### 例5，消息盒子 QMessageBox

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

![img](/images/136a1644815c48b0b7d5718dda747073.png)
```
QMessageBox.information(NULL, "Title", "Content", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes);
```

下面是一个简单的例子：

![img](/images/046f2b91373f41bca7f9517d8ba58cf4.png)

现在我们从 API 中看看它的函数签名：

```
static StandardButton QMessageBox.information ( QWidget * parent, const QString &amp; title, const QString &amp; text, StandardButtons buttons = Ok, StandardButton defaultButton = NoButton );
```

首先，它是 static 的，所以我们能够使用类名直接访问到(怎么看都像废话…)；然后看它那一堆参数，第一个参数 parent，说明它的父组件；第二个参数 title，也就是对话框的标题；第三个参数 text，是对话框显示的内容；第四个参数 buttons，声明对话框放置的按钮，默认是只放置一个 OK 按钮，这个参数可以使用或运算，例如我们希望有一个 Yes 和一个 No 的按钮，可以使用 QMessageBox.Yes | QMessageBox.No，所有的按钮类型可以在 QMessageBox 声明的 StandarButton 枚举中找到；第五个参数 defaultButton 就是默认选中的按钮，默认值是 NoButton，也就是哪个按钮都不选中。这么多参数，豆子也是记不住的啊！所以，我们在用 QtCreator 写的时候，可以在输入QMessageBox.information 之后输入(，稍等一下，QtCreator 就会帮我们把函数签名显示在右上方了，还是挺方便的一个功能！

#### 其它接口

Qt 提供了五个类似的接口，用于显示类似的窗口。具体代码这里就不做介绍，只是来看一下样子吧！

```python
QMessageBox.critical(NULL, "critical", "Content", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes);
```

![img](/images/f2d5ef1f5b2545919954080e95bf046c.png)

```python
QMessageBox.warning(NULL, "warning", "Content", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes);
```

![img](/images/54291ffa6d99425b9d038fc5db4204d3.png)

```python
QMessageBox.question(NULL, "question", "Content", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes);
```

![img](/images/b8245ca6741747609f077112a0efd86c.png)

```python
QMessageBox.about(NULL, "About", "About this application");
```

![img](/images/90e4e0bc5ef34232b0262dd122f7451d.png)

请注意，最后一个 about()函数是没有后两个关于 button 设置的按钮的！

QMessageBox 对话框的文本信息时可以支持 HTML 标签的。例如：

```
QMessageBox.about(NULL, "About", "About this <font color='red'>application</font>");
```

运行效果如下：

![img](/images/a239f1033ad545fa98e7b3529496f23e.png)

如果我们想自定义图片的话，也是很简单的。这时候就不能使用这几个 static 的函数了，而是要我们自己定义一个 QMessagebox 来使用：

```python
message = QMessageBox(QMessageBox.NoIcon, "Title", "Content with icon.");
message.setIconPixmap(QPixmap("icon.png"));
message.exec();
```

这里我们使用的是 `exec()`函数，而不是 `show()`，因为这是一个模态对话框，需要有它自己的事件循环，否则的话，我们的对话框会一闪而过哦(感谢 laetitia 提醒).

需要注意的是，同其他的程序类似，我们在程序中定义的相对路径都是要相对于运行时的.exe 文件的地址的。比如我们写"icon.png"，意思是是在.exe 的当前目录下寻找一个"icon.png"的文件。这个程序的运行效果如下：

![img](/images/7cbdebeb087144eca585c8d028c6a23f.png)

还有一点要注意，我们使用的是 png 格式的图片。因为 Qt 内置的处理图片格式是 png，所以这不会引起很大的麻烦，如果你要使用 jpeg 格式的图片的话，Qt 是以插件的形式支持的。在开发时没有什么问题，不过如果要部署的话，需要注意这一点。

最后再来说一下怎么处理对话框的交互。我们使用 `QMessageBox` 类的时候有两种方式，一是使用`static``函数，另外是使用构造函数。

首先来说一下 static 函数的方式。注意，static 函数都是要返回一个 `StandardButton`，我们就可以通过判断这个返回值来对用户的操作做出相应。

```python
replay = QMessageBox.question(NULL, "Show Qt", "Do you want to show Qt dialog?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes);
if replay == QMessageBox.Yes:
    print('you press yes')
```

如果要使用构造函数的方式，那么我们就要自己运行判断一下啦：

```python
 message = QMessageBox(QMessageBox.NoIcon, "Show Qt", "Do you want to show Qt dialog?", QMessageBox.Yes | QMessageBox.No, NULL);
if message.exec() == QMessageBox.Yes:
    QMessageBox.aboutQt(NULL, "About Qt");
```

其实道理上也是差不多的。

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

## QWidget，QDialog和Qmainwindow的区别

### QWidget

QWidget类是所有用户界面对象的基类。

窗口部件是用户界面的一个原子：它从窗口系统接收鼠标、键盘和其它事件，并且将自己的表现形式绘制在屏幕上。每一个窗口部件都是矩形，并且它们按Z轴顺序排列。一个窗口部件可以被它的父窗口部件或者它前面的窗口部件盖住一部分。

QWidget有很多成员函数，但是它们中的一些有少量的直接功能：例如，QWidget有字体属性，但是自己从来不用。为很多继承它的子类提供了实际的功能，比如QLabel、QPushButton、QCheckBox等等。

没有父窗体的小部件始终是一个独立的窗口（顶级窗口部件）。非窗口的小部件为子部件，它们在父窗口中显示。Qt中大多数部件主要被用作子部件。例如：可以显示一个按钮作为顶层窗口，但大多数人更喜欢将按钮内置于其它部件，如QDialog。

![img](https://img-blog.csdn.net/20160117195225083)


上图显示了一个QGroupBox，里面包含了大量由QGridLayout布局的子控件。

### QDialog

QDialog类是对话框窗口的基类。

对话框窗口是一个顶级窗体，主要用于短期任务以及和用户进行简要通讯。QDialog可以是模式的也可以是非模式的。QDialog支持扩展性并且可以提供返回值。它们可以有默认按钮。QDialog也可以有一个QSizeGrip在它的右下角，使用setSizeGripEnabled()。

注意：QDialog（以及其它使用Qt.Dialog类型的widget）使用父窗口部件的方法和Qt中其它类稍微不同。对话框总是顶级窗口部件，但是如果它有一个父对象，它的默认位置就是父对象的中间。它也将和父对象共享工具条条目。

#### 模式对话框

阻塞同一应用程序中其它可视窗口输入的对话框。模式对话框有自己的事件循环，用户必须完成这个对话框中的交互操作，并且关闭了它之后才能访问应用程序中的其它任何窗口。模式对话框仅阻止访问与对话相关联的窗口，允许用户继续使用其它窗口中的应用程序。

显示模态对话框最常见的方法是调用其exec()函数，当用户关闭对话框，exec()将提供一个有用的返回值，并且这时流程控制继续从调用exec()的地方进行。通常情况下，要获得对话框关闭并返回相应的值，我们连接默认按钮，例如：”确定”按钮连接到accept()槽，”取消”按钮连接到reject()槽。另外我们也可以连接done()槽，传递给它Accepted或Rejected。

#### 非模式对话框

和同一个程序中其它窗口操作无关的对话框。在文字处理中的查找和替换对话框通常是非模式的，允许用户同时与应用程序的主窗口和对话框进行交互。调用show()来显示非模式对话框，并立即将控制返回给调用者。

如果隐藏对话框后调用show()函数，对话框将显示在其原始位置，这是因为窗口管理器决定的窗户位置没有明确由程序员指定，为了保持被用户移动的对话框位置，在closeEvent()中进行处理，然后在显示之前，将对话框移动到该位置。

#### 半模式对话框

调用setModal(true)或者setWindowModality()，然后show()。有别于exec()，show() 立即返回给控制调用者。

对于进度对话框来说，调用setModal(true)是非常有用的，用户必须拥有与其交互的能力，例如：取消长时间运行的操作。如果使用show()和setModal(true)共同执行一个长时间操作，则必须定期在执行过程中调用QApplication.processEvents()，以使用户能够与对话框交互（可以参考QProgressDialog）。

### QMainWindow

QMainWindow类提供一个有菜单条、工具栏、状态条的主应用程序窗口（例如：开发Qt常用的IDE-Visual Studio、Qt Creator等）。

一个主窗口提供了构建应用程序的用户界面框架。Qt拥有QMainWindow及其相关类来管理主窗口。

QMainWindow拥有自己的布局，我们可以使用QMenuBar（菜单栏）、QToolBar（工具栏）、QStatusBar（状态栏）以及QDockWidget（悬浮窗体），布局有一个可由任何种类小窗口所占据的中心区域。

例如：

![img](https://img-blog.csdn.net/20160117185134087)


#### 使用原则

* 如果需要嵌入到其他窗体中，则基于QWidget创建。

* 如果是顶级对话框，则基于QDialog创建。

* 如果是主窗体，则基于QMainWindow创建。

### QMainWindow与Qwidget通信

```python
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(600, 220)
        self.setWindowTitle('Statusbar')
        self.setWindowIcon(QIcon('icon.png'))
        self.statusBar().showMessage('Ready')
        # Querstion是一个Qwidget，忽略相关代码
        self.widget = Querstion()
        self.widget.btn_submit.clicked.connect(self.submit)
        self.setCentralWidget(self.widget)
        self.show()
    def submit(self):
        print('submit')
        if self.q.yes.isChecked():
            print('yes')
            self.q.question.setText('請查看LED是否亮起绿燈?')
```

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


```python

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
    QPushButton, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

1. 生成grid布局

```python
grid = QGridLayout()
self.setLayout(grid)
```
2. 写出列表形式的布局组件和定位，它们应该是一一对应的关系

```python
names = ['Cls', 'Bck', '', 'Close',
         '7', '8', '9', '/',
        '4', '5', '6', '*',
         '1', '2', '3', '-',
        '0', '.', '=', '+']

positions = [(i,j) for i in range(5) for j in range(4)]
# (0,0) (0,1) (0,2) (0,3)
# (0,0) (1,1) (1,2) (1,3)
# ...

```

3. 将names和positions组成对应关系,并将组件和定位add入布局中

```python
# zip 将可迭代对象对应的关系打包成一个个元组
for position, name in zip(positions, names):

    if name == '':
        continue
    button = QPushButton(name)
    grid.addWidget(button, *position)
```

程序预览：

![img](/images/acb70618e32e4f60b6de4f3f26a2417f.png)
### 跨行显示

`grid.addWidget`支持五个参数，第一个是需要加入的组件，第二个和第三个分别是行和列的定位，第四个和第五个表示跨行和跨列数

```python
grid.addWidget(reviewE`t, 3, 1, 5, 1)
```

`grid.setSpacing(10)`用来生成组件之间的空间


```python
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

程序预览：

![img](/images/d087b9ae18714100818926583022e970.png)
## 事件和信号

所有的应用都是事件驱动的。事件大部分都是由用户的行为产生的，当然也有其他的事件产生方式，比如网络的连接，窗口管理器或者定时器等。调用应用的exec_()方法时，应用会进入主循环，主循环会监听和分发事件。

在事件模型中，有三个角色：

* 事件源
* 事件
* 事件目标

事件源就是发生了状态改变的对象。事件是这个对象状态的改变撞他改变的内容。事件目标是事件想作用的目标。事件源绑定事件处理函数，然后作用于事件目标身上。

PyQt5处理事件方面有个signal and slot机制。Signals and slots用于对象间的通讯。事件触发的时候，发生一个signal，slot是用来被Python调用的，slot只有在事件触发的时候才能调用。

### 事件对象

事件对象是用python来描述一系列的事件自身属性的对象。+

```python

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()


    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

这个示例中，我们在一个组件里显示鼠标的X和Y坐标。+

```python
self.text = "x: {0},  y: {1}".format(x, y)

self.label = QLabel(self.text, self)

```

X Y坐标显示在`QLabel`组件里+

```python
self.setMouseTracking(True)

```

鼠标追踪默认没有开启，当有鼠标点击事件发生后才会开启。+

```python
def mouseMoveEvent(self, e):

    x = e.x()
    y = e.y()

    text = "x: {0},  y: {1}".format(x, y)
    self.label.setText(text)

```

`e`代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象。`x()`和`y()`方法得到鼠标的x和y坐标点，然后拼成字符串输出到`QLabel`组件里。+

程序展示：

![img](/images/e4827a0d4c9c418abf47c5ad5753d1b5.png)

### 事件发送

有时候我们会想知道是哪个组件发出了一个信号，PyQt5里的`sender()`方法能搞定这件事。+

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

这个例子里有俩按钮，`buttonClicked()`方法决定了是哪个按钮能调用`sender()`方法。+

```
btn1.clicked.connect(self.buttonClicked)
btn2.clicked.connect(self.buttonClicked)

```

两个按钮都和同一个slot绑定。+

```
def buttonClicked(self):

    sender = self.sender()
    self.statusBar().showMessage(sender.text() + ' was pressed')

```

我们用调用`sender()`方法的方式决定了事件源。状态栏显示了被点击的按钮。+

程序展示：+

![img](/images/ff0722a3b50e4425aa378607c32ec846.png)


### 不同窗口的通信与信号发送

A 类通过 `QObject` 实例定义一个信号并使用`emit()`广播它,B 类通过 `connect(self.method...)` 将自身的方法与该信号进行绑定，这就是一个信号槽机制

```python
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject):

    closeApp = pyqtSignal()

class A(QtWidgets):

    def __init__():
        self.c = Communicate()
        self.c.closeApp.emit()

class B(QtWidgets):
    def __init__():
        a = A()
        a.c.closeApp.connect(B.method(...))
```

## 控件1

控件就像是应用这座房子的一块块砖。PyQt5有很多的控件，比如按钮，单选框，滑动条，复选框等等。在本章，我们将介绍一些很有用的控件：`QCheckBox`，`ToggleButton`，`QSlider`，`QProgressBar`和`QCalendarWidget`。

### QCheckBox

`QCheckBox`组件有俩状态：开和关。通常跟标签一起使用，用在激活和关闭一些选项的场景。+

```python
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()


    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```
### 图片

`QPixmap`是处理图片的组件。本例中，我们使用`QPixmap`在窗口里显示一张图片。+

```python

from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("redrock.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

```
pixmap = QPixmap("redrock.png")

```

创建一个`QPixmap`对象，接收一个文件作为参数。+

```
lbl = QLabel(self)
lbl.setPixmap(pixmap)

```

把`QPixmap`实例放到`QLabel`组件里。

程序展示：

![img](/images/d8624617c1b3451c9d239fdae05d6870.png)
## 多线程

默认情况下PyQt5的界面是阻塞的，当程序内部处理一些耗时的工作时，界面就会等待该工作处理完成才会响应其它事件(点击下一步的按钮)，这样就造成了程序卡顿。我们可以使用多线程处理耗时的工作来避免这个问题。

```python
from PyQt5.QtCore import pyqtSignal, QObject,QThread
class WorkThread(QThread):
    sig = pyqtSignal()
    def __int__(self):
        super(WorkThread,self).__init__()

    def run(self):
        # 模拟工作线程
        time.sleep(5)
        self.sig.emit()
work_thread = WorkThread()



class widget(Qwidget):
    """docstring for ClassName"""
    def __init__(self, arg):
        # 当work_thread处理完毕时，调用某些方法
        work_thread.sig.connect(self.method)
    def some_method(self):
        # 启动线程
        work_thread.start()
```
## 常用API或方法

### 文字与样式设置

```
lable = QLabel('請查看LED是否亮起紅燈?')
```

### 设置字体样式

**使用setStyleSheet设置样式**

```python
lable.setStyleSheet("color:red;font-size:12px;font-style:Microsoft YaHei");
```
**在创建时直接使用css设置样式**

```
question = QLabel('請查看LED是否亮起<span style = 'color:red;font-size:14px'>紅燈?</span>')
```
**修改文字内容**

```
lable.setText('請查看LED是否亮起绿燈?')
```

**设置自动换行**

默认是不会换行的，如果文字过长则会超出窗口从而不显示，而且使用setStyleSheet无效

```
lable.setWordWrap(True)
```
### 设置lable显示或隐藏

```
QWidge.setVisible(bool)
```

`show()`、`hide()`、`setHidden()`都能控制元素显示或隐藏，并且他们的内部都是通过`setVisible(bool)`实现的


## 参考手册

[PyQt5中文教程](https://maicss.gitbooks.io/pyqt5/content/hello_world.html)