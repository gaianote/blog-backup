title: PyQt5学习教程11 checkbox
author: 李云鹏
date: 2018-09-17 11:30:15
tags:
---
可以使用`QCheckBox`小部件创建一个复选框。使用`QCheckBox`类创建新复选框时，第一个参数是label。

要将操作应用于切换开关，我们调用`.stateChanged.connect()`，然后调用回调方法。调用此方法时，它会将一个boolean值作为state的参数发送。如果选中，则其值为`QtCore.Qt.checked`

![img](/images/85714c71b264486186db84001ba485d8.png)
## 基本示例

```python
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget
from PyQt5.QtCore import QSize    

class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(140, 40))    
        self.setWindowTitle("Checkbox") 
        # 1. 实例化一个QCheckBox
        self.b = QCheckBox("Awesome?",self)
        # 2. 当状态改变时，调用self.clickBox方法
        self.b.stateChanged.connect(self.clickBox)
        self.b.move(20,20)
        self.b.resize(320,40)

    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )
```
## 常用方法

**1.实例化一个QCheckBox：**

```python
self.checkbox = QCheckBox("Awesome?",self)
```

**2.当复选框的被选中或取消选中时，连接槽函数**

```
self.checkbox.stateChanged.connect(self.clickBox)
```

**3. 判断复选框是否被选中**

1. 通过槽函数接受stateChanged信号emit的参数state判断,该方法比`isCechked`判断多了一种状态，半选状态。半选状态表现为，√ 显示为灰色

  ```python
  def clickBox(self, state):

    if state == QtCore.Qt.Checked:
      print('Checked')
    elif state == QtCore.Qt.UnChecked:
      print('Unchecked')
    elif state == QtCore.Qt.PartiallyChecked:
      print('PartiallyChecked')
  ```
2. 通QCheckBox的实例方法`isChecked()`判断，返回一个布尔值

  ```python
  def clickBox(self):

    if self.checkbox.isChecked() == True:
      print('Checked')
    else:
      print('Unchecked')
  ```

**4. 设置复选框的选中状态**

2. 通过QCheckBox的实例方法`setCheckState()`设置状态  

```python
self.checkbox.setCheckState(Qt.Checked) # 勾选复选框
self.checkbox.setCheckState(Qt.PartiallyChecked) # 半勾选复选框
self.checkbox.setCheckState(Qt.Unchecked) # # 取消勾选复选框
```

2. 通过QCheckBox的实例方法`setChecked()`设置状态        

```python
self.checkbox.setChecked(True) # 勾选复选框
self.checkbox.setChecked(False) # 取消勾选复选框
```
