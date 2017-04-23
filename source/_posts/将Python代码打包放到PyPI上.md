---
title: 将Python代码打包放到PyPI上
date: 2017-04-23 22:07:42
tags: python
---

## 什么是PyPI

PyPI(Python Package Index)是python官方的第三方库的仓库。
所有人都可以下载第三方库或上传自己开发的库到PyPI。
PyPI推荐使用pip包管理器来下载第三方库

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
[将自己写的Python代码打包放到PyPI上](http://blog.csdn.net/crisschan/article/details/51840552)