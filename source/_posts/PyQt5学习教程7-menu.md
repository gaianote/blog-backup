title: PyQt5学习教程7 menu
author: 李云鹏
date: 2018-09-17 07:46:32
tags:
---
你想要PyQt应用程序中的菜单吗？Pyqt有菜单支持。几乎每个GUI应用程序都在窗口顶部有一个主菜单。添加菜单与添加小部件略有不同。

![img](/images/4e456ebd76bc4e83a6aba17d6fb9d26c.png)
菜单可以包含子菜单，它们通常类似于（文件，编辑，视图，历史记录，帮助）。每个菜单都有相依的动作。

完整示例:

```python
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 100))
        self.setWindowTitle("PyQt menu example - pythonprogramminglanguage.com")

        # 1.1 创建menuBar
        menuBar = self.menuBar()
        # 1.2 定义一个menu，并将该meun添加到menuBar
        fileMenu = menuBar.addMenu('&File')

        # 2.1 创建一个Action
        newAction = QAction(QIcon('new.png'), '&New', self)
        # 2.2 为Action添加快捷键
        newAction.setShortcut('Ctrl+N')
        # 2.3 为Action添加setStatusTip
        newAction.setStatusTip('New document')
        # 2.4 为Action绑定相应的方法
        newAction.triggered.connect(self.newCall)

        # Create new action
        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open document')
        openAction.triggered.connect(self.openCall)

        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # 3. 将创建好的Action添加到Menu
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

    def openCall(self):
        print('Open')

    def newCall(self):
        print('New')

    def exitCall(self):
        print('Exit app')

    def clickMethod(self):
        print('PyQt')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
```