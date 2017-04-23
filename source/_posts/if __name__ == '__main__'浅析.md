---
title: if __name__ == '__main__'浅析
date: 2017-04-23 21:19:05
tags: nodejs
---

```python
def main():
  print "we are in %s"%__name__
if __name__ == '__main__':
  main()
```
其中 `__name__ == '__main__'`: 的作用是：
当该文件作为脚本运行时，main()函数可以运行
当该文件作为模块被其他文件导入时，main()函数不会运行,避免了模块重复运行


