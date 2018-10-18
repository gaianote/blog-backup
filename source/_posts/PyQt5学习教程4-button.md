title: PyQt5学习教程4 button
author: 李云鹏
date: 2018-09-17 07:01:41
tags:
---
为了向窗口中添加按钮，我们需要了解如何将按钮小部件添加到现有的Pyqt窗口，以及了解如何将单击连接到Python方法。

<!--more-->

![img](https://pythonprogramminglanguage.com/wp-content/uploads/2017/06/pyqt-button.png)

## 示例

```python
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 200))    
        self.setWindowTitle("PyQt button example - pythonprogramminglanguage.com") 
        
        # 1.向窗口添加Button
        pybutton = QPushButton('Click me', self)
        # 2.将点击事件与python方法连接
        pybutton.clicked.connect(self.clickMethod)
        # 3.调整button大小
        pybutton.resize(100,32)
        # 4.调整button位置
        pybutton.move(50, 50)        

    def clickMethod(self):
        print('Clicked Pyqt button.')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
```
