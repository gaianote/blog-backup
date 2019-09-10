title: PyQt5学习教程9 textarea
author: 李云鹏
date: 2018-09-17 11:15:11
tags:
---
`QPlainTextEdit`是PyQt中的多行文本区域。要设置文本，我们使用其方法`insertPlainText()`。我们可以使用方法`move()`和`resize()`来设置它的位置和大小。

<!--more-->

![img](https://pythonprogramminglanguage.com/wp-content/uploads/2017/07/pyqt-textarea.png)

## Textarea

下面的示例使用`PyQt5`创建文本区域。我们将创建通常的`QMainWindow`来添加小部件。它只适用于纯文本，如记事本。要添加新行，我们添加`\n`字符。

```python
import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize

class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(440, 240))
        self.setWindowTitle("PyQt5 Textarea example")

        # 实例化一个QPlainTextEdit
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("You can write text here.\n")
        self.b.move(10,10)
        self.b.resize(400,200)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )
```