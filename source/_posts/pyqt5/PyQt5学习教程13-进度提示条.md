title: PyQt5学习教程13 进度提示条
author: 李云鹏
date: 2018-09-18 06:34:48
tags:
---
在日常处理事务的过程，由于过程漫长，需要等待一会，这时一般软件都会给予一定的提示，我们可以使用进度条来给出友好的提示

![img](http://img.xdbcb8.com/wp-content/uploads/2018/05/%E8%BF%9B%E5%BA%A6%E6%9D%A1.gif)


## 基本示例

**进度条的基本流程是：**
1. 实例化一个进度条提示窗口`progress = QProgressDialog(self)`
2. 使用`progress.setRange(0,max_value)`得到进度条的取值范围
3. 使用`progress.setValue(value)`设置当前的进度值
  1. 使用`value/max_value`得到百分比，就是进度条的百分百
  2. 当`value == max_value`时，进度百分之百，表示进程操作完成
  3. 具体做法是:工作线程通过`sig.emit(int)`发送值，ui线程接收到信号后，执行相应的槽函数设置进度

**示例：**

```python
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog)
from PyQt5.QtCore import Qt
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(300,150)
        self.setWindowTitle("微信公众号：学点编程吧--进度对话框")
        self.lb = QLabel("文件数量",self)
        self.lb.move(20,40)
        self.bt1 = QPushButton('开始',self)
        self.bt1.move(20,80)
        self.edit = QLineEdit('1000000',self)
        self.edit.move(100,40)
        self.show()
        self.bt1.clicked.connect(self.showDialog)

    def showDialog(self):
        num = int(self.edit.text())
        # 实例化一个QProgressDialog
        progress = QProgressDialog(self)
        
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        # 如果任务的预期持续时间小于minimumDuration，则对话框根本不会出现。这样可以防止弹出对话框，快速完成任务。
        progress.setMinimumDuration(5)
        # 当progress窗口显示时，阻止用户对所有父级窗口的输入（默认情况为不阻止）
        progress.setWindowModality(Qt.WindowModal)
        # setRange(0,num)就是设置其进度的最小和最大值，这里最小值0，最大值num，分别对应0%和100%
        progress.setRange(0,num)
        for i in range(num):
            # 通过调用setValue得到的 值/最大值 得到的百分比显示进度
            progress.setValue(i)
            # 用户点击取消会提示操作失败
            if progress.wasCanceled():
                QMessageBox.warning(self,"提示","操作失败")
                break
        # 完全完成后，提示操作成功
        else:
            progress.setValue(num)
            QMessageBox.information(self,"提示","操作成功")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

## 实际应用

首先定义一个process_value信号:

```python
from PyQt5.QtCore import QObject,pyqtSignal

class Sig(QObject):

    # 进度条提示
    process_value = pyqtSignal(int)

sig = Sig()
```

工作线程:发送`process_value`信号，参数为int：

```
for i in range(100):
  time.sleep(0.1)
  self.sig.process_value.emit(i)
```

ui线程:接收到`process_value`信号时，调用`self.process.setValue`方法设置当前进度数值

```
def showDialog(self):
  self.progress = QProgressDialog(self)
  ...
  self.sig.process_value.connect(self.process.setValue)
```
           

## 参考文档

[PyQt5系列教程（13）：进度对话框](http://www.xdbcb8.com/archives/354.html)