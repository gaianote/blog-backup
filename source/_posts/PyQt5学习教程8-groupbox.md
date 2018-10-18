title: PyQt5学习教程8 groupbox
author: 李云鹏
date: 2018-09-17 08:32:45
tags:
---
您可以将widgets放在grip中。grip可以包含groupbox，其中每个groupbox都有一个或多个widgets。groupbox的作用是，我们可以现在groupbox中设置好布局，然后方便的在window中自由组合groupbox

![img](https://pythonprogramminglanguage.com/wp-content/uploads/2017/06/groupbox.png)
<!--more-->

## 示例


可以使用PyQt创建gropbox和grip。它的工作原理如下：
1. PyQt5窗口可以包含grip
2. grip可以包含任意数量的gropbox
3. gropbox可以包含小部件（按钮，文本，图像）以及适合的布局


可以使用类QGridLayout创建网格。正如您所想象的那样，必须将网格布局添加到窗口中。可以使用类QGroupBox创建groupbox。

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget)

class Window(QWidget):
    def __init__(self, parent=None):
        # 1. 继承QWidget生成窗口
        super(Window, self).__init__(parent)
        # 2.创建一个layout，将gropBox添加到layout中
        grid = QGridLayout()
        grid.addWidget(self.createExampleGroup(), 0, 0)
        grid.addWidget(self.createExampleGroup(), 1, 0)
        grid.addWidget(self.createExampleGroup(), 0, 1)
        grid.addWidget(self.createExampleGroup(), 1, 1)
        # 3. 应用之前设置好的layout
        self.setLayout(grid)

        self.setWindowTitle("PyQt5 Group Box")
        self.resize(400, 300)

    def createExampleGroup(self):
        # 1.生成实例 groupBox =》 对应窗口
        groupBox = QGroupBox("Best Food")
        
        # 2.创建一些小部件，比如button或者raido
        radio1 = QRadioButton("Radio pizza")
        radio2 = QRadioButton("Radio taco")
        radio3 = QRadioButton("Radio burrito")
        radio1.setChecked(True)
        
        # 3.创建一个layout，将小部件添加到layout中
        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addStretch(1)
        
        # 4. 应用之前设置好的layout
        groupBox.setLayout(vbox)

        return groupBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())
```