title: PyQt5学习教程2 Hello World
author: 李云鹏
date: 2018-09-17 06:11:28
tags:
---
使用PyQt制作的图形界面可运行于 Microsoft Windows，Apple Mac OS X和Linux。我们将使用PyQt创建一个Hello World应用程序。

![img](/images/a8e638fb97e34cbe8ded0fd222d5e553.png)
<!--more-->


PyQt Hello World

我们编写的应用程序将在图形窗口中显示消息“Hello World”。

```python
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize    

class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1.设置窗口大小和标题
        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Hello world") 
        
        # 2.为主窗口设置CentralWidget
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget) 
        
        # 3.为centralWidget设置Layout
        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  

        # 4.向Layout中添加Widget
        title = QLabel("Hello World from PyQt", self) 
        title.setAlignment(QtCore.Qt.AlignCenter) 
        gridLayout.addWidget(title, 0, 0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )

```
该程序从main开始。我们初始化Qt并创建一个`HelloWindow`类型的对象。我们调用`show()`方法来显示窗口。

`HelloWindow`类继承自`QMainWindow`类。我们称其超级方法初始化窗口。

然后设置了几个类变量：大小和窗口标题。我们向窗口添加小部件，包括显示消息“Hello World”的标签小部件（QLabel）。
