title: PyQt5学习教程10 line edit
author: 李云鹏
date: 2018-09-15 09:37:59
tags:
---
## PyQt line edit

在本教程中，我们将创建一个显示输入字段的应用程序。

可以使用QLineEdit类创建文本框或LineEdit。许多应用程序具有诸如表单字段之类的文本输入。

![img](/images/ff7324805a8d49a7a73466ebee8ab0b7.png)

### 介绍

首先导入QLineEdit小部件：

```python
from PyQt5.QtWidgets import QLineEdit
```



我们还将添加一个文本标签，以向用户显示要键入的内容。导入QLabel：

```python
from PyQt5.QtWidgets import QLabel
```



然后将两者都添加到屏幕：

```python
self.nameLabel = QLabel(self)
self.nameLabel.setText('Name:')
self.line = QLineEdit(self)
self.line.move(80, 20)
self.line.resize(200, 32)
self.nameLabel.move(20, 20)
```



可以使用以下方式打印文本值：

```python
print('Your name: ' + self.line.text())
```




## QLineEdit 示例


```python
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)

    def clickMethod(self):
        print('Your name: ' + self.line.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )

```