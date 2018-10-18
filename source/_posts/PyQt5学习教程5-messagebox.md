title: PyQt5学习教程5 messagebox
author: 李云鹏
date: 2018-09-17 07:15:43
tags:
---
在创建Python GUI时，您可能希望在某个时刻显示消息框。Pyqt在PyQt4和PyQt5中都带有消息框支持。要使用的类是QMessageBox。在本教程中，您将学习如何在单击时显示消息框。

![img](/images/Snipaste_2018-09-18_18-47-25.png)

## QMessageBox示例

```python

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(200, 200, 380,200)
        self.setWindowTitle('消息对话框')

        self.bt1 = QPushButton('提示',self)
        self.bt1.move(20,70)

        self.bt1.clicked.connect(self.info)

        self.show()

    def info(self):
        reply = QMessageBox.information(self,'提示','这是一个消息提示对话框!',QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            print('你选择了Ok！')
        else:
            print('你选择了Close！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

### 实例化一个消息盒子

```python
reply = QMessageBox.information(self,'提示','这是一个消息提示对话框!',QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
```
1. 第一个参数指定信息盒子的父窗口
2. 第二个参数指定消息盒子的标题
3. 第三个参数指定消息盒子的文本
4. 第四个参数指定消息盒子使用的按钮
5. 第五个参数指定消息盒子的默认选中按钮

当然还有更多的按钮可以供我们选择，如下图：

![img](http://img.xdbcb8.com/wp-content/uploads/2018/05/%E5%A5%BD%E5%A4%9A%E6%8C%89%E9%92%AE.jpg)


这个函数中我们显示的按钮分别是Ok、Close，默认按钮是Close。

### 获取点击的按钮

```
if reply == QMessageBox.Ok:
    print('你选择了Ok！')
else:
    print('你选择了Close！')
```

## 自定义一个消息盒子

我们可以通过设置`QMessageBox`属性自定义消息盒子，过程比较繁琐，但是可以灵活的修改按钮文本以及图标

![img](http://img.xdbcb8.com/wp-content/uploads/2018/05/%E8%AD%A6%E5%91%8A3.jpg)



```python
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(200, 200, 380,200)
        self.setWindowTitle('消息对话框')

        self.bt1 = QPushButton('提示',self)
        self.bt1.move(20,70)

        self.bt1.clicked.connect(self.warning)

        self.show()

    def warning(self):
        checkbox = QCheckBox('所有文档都按此操作')
        msgBox = QMessageBox()
        msgBox.setWindowTitle('警告')
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText('这是一个警告消息对话框')
        msgBox.setInformativeText('出现更改愿意保存吗?')
        Save = msgBox.addButton('保存', QMessageBox.AcceptRole)
        NoSave = msgBox.addButton('取消', QMessageBox.RejectRole)
        Cancel = msgBox.addButton('不保存', QMessageBox.DestructiveRole)
        msgBox.setDefaultButton(Save)
        msgBox.setCheckBox(checkbox)
        checkbox.stateChanged.connect(self.check)
        reply = msgBox.exec()

        if reply == QMessageBox.AcceptRole:
            print('你选择了保存！')
        elif reply == QMessageBox.RejectRole:
            print('你选择了取消！')
        else:
            print('你选择了不保存！')
    def check(self):
        if self.sender().isChecked():
            print('isChecked')
        else:
            print('unChecked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

### 自定义图标

我们可以通过`msgBox.setIconPixmap(QPixmap("icon.png"))`自定义提示信息的图标

```python
from PyQt5.QtGui import QPixmap
def about(self):
    msgBox = QMessageBox(QMessageBox.NoIcon, '关于','关于的提示信息!')
    msgBox.setIconPixmap(QPixmap("beauty.png"))
    reply = msgBox.exec()
    ...
```
