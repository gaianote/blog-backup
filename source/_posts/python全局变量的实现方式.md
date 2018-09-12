title: python全局变量的实现方式
author: 李云鹏
date: 2018-09-10 10:55:38
tags:
---
## 全局变量

如何在一个项目中多个文件共享一个变量呢？使用一个config.py作为模块导入,并给需要作为全局变量的属性赋值即可

<!--more-->

示例：

config.py
```
class Config():
  def __init__(self):
    pass
config = Config()
```

main.py
```
form config import config
config.path = os.path.abspath('.')
```
other.py
```
form config import config
print(config.path)
```

## 原理

Python中所有加载到内存的模块都放在 `sys.modules` 。当 `import` 一个模块时首先会在这个列表中查找是否已经加载了此模块，如果加载了则只是将模块的名字加入到正在调用 `import` 的模块的 `Local` 名字空间中。如果没有加载则从 sys.path 目录中按照模块名称查找模块文件，模块可以是py、pyc、pyd，找到后将模块载入内存，并加到 `sys.modules` 中，并将名称导入到当前的 Local 名字空间。 

也就是说，多个模块`import`同一个模块，这个模块只会运行(初始化)一次。