title: PyQt5学习教程6 tooltip
author: 李云鹏
date: 2018-09-17 07:24:52
tags:
---
tooltip是图形界面中的提示。将鼠标悬停在窗口小部件上时（不单击），经常会出现tooltip。Pyqt支持tooltip，可以为小部件配置它们。     

![img](/images/53ef45b96d3c430eb29f6f8320bd2381.png)<!--more-->

可以使用小部件setTooltip方法设置工具提示。

```python
pybutton.setToolTip('This is a tooltip for the QPushButton widget')
```

## 完整示例

```python
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 100))    
        self.setWindowTitle("PyQt tooltip example - pythonprogramminglanguage.com") 

        pybutton = QPushButton('Pyqt', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,32)
        pybutton.move(50, 20)        
        pybutton.setToolTip('This is a tooltip message.')  

    def clickMethod(self):
        print('PyQt')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
```
              