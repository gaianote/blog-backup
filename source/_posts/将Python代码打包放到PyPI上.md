---
title: 将Python代码打包放到PyPI上
date: 2017-04-23 22:07:42
tags: python
---

## 什么是PyPI

PyPI(Python Package Index)是python官方的第三方库的仓库。
所有人都可以下载第三方库或上传自己开发的库到PyPI。
PyPI推荐使用pip包管理器来下载第三方库

## 包的文件结构

```
foo
|-- bin/ #存放项目的一些可执行文件
|   |-- foo
|-- foo/ # 所有模块、包都应该放在此目录，程序的入口最好命名为main.py
|   |-- tests/ # 存放单元测试代码；
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |-- __init__.py
|   |-- main.py
|-- docs/ # 用于存放文档
|   |-- conf.py
|   |-- abc.rst
|-- setup.py # 来管理代码的打包、安装、部署问题
|-- requirements.txt # 存放软件依赖的外部Python包列表
|-- README.rst # 项目说明文件
```

## setup文件

```python
import codecs
import os
import sys
try:
  from setuptools import setup
except:
  from distutils.core import setup

def read(fname):
  return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "project_name"
PACKAGES = ["somefunctions",]
DESCRIPTION = "package description."
LONG_DESCRIPTION = read("README.rst")
KEYWORDS = "test python package"
AUTHOR = "your_name"
AUTHOR_EMAIL = "youremail@email.com"
URL = "http://your_blog/"
VERSION = "1.0.1"
LICENSE = "MIT"
CLASSFIERS = ['License :: OSI Approved :: MIT License','Programming Language :: Python','Intended Audience :: Developers','Operating System :: OS Independent']

setup(
  name = NAME,
  version = VERSION,
  description = DESCRIPTION,
  long_description =LONG_DESCRIPTION,
  classifiers =  CLASSFIERS,
  keywords = KEYWORDS,
  author = AUTHOR,
  author_email = AUTHOR_EMAIL,
  url = URL,
  license = LICENSE,
  packages = PACKAGES,
  include_package_data=True,
  zip_safe=True,
)

```


## 打包上传

使用check命令查看是否存在语法问题，使用sdist进行打包。

```bash
python setup.py check
python setup.py sdist
```

发布前，需要到[pypi官网](https://pypi.python.org/pypi)注册一个账号，并在用户目录新建文件 ~/.pypirc ，并键入以下内容

```
[distutils]
index-servers = pypi
[pypi]
repository: https://pypi.python.org/pypi
username: yourname
password: yourpwd
```

执行以下内容进行打包上传，服务器返回Server response (200): OK表示上传成功

```bash
python setup.py sdist upload
```

发布成功后就可以使用`pip install`安装你自己的python包了！

## 参考资料
[Invalid or non-existent authentication information](https://github.com/pypa/setuptools/issues/941)