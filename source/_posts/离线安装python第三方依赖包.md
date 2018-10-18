---
title: python内网电脑离线安装依赖
date: 2018-06-11 22:07:42
tags: python
---

## python内网电脑安装依赖n


## pip常用命令

```python
#安装包
pip install xxx

#升级包，可以使用-U 或者 --upgrade
pip install -U xxx

#卸载包
pip uninstall xxx

#列出已安装的包
pip list
```

## pip离线安装依赖包


### Step 1. 下载需要离线安装的Packages

在一台可以访问外网的机器上执行如下命令：


```bash
$ pip install <package>
$ pip download <package>
$ pip freeze > requirements.txt
```

### Step 2. 将下载好的Packages拷贝至内网服务器

使用scp、sftp等方式将下载好的Packages拷贝至需要离线安装这些包的内网服务器。

### Step 3. 安装Packages

假设内网服务器的目录 `/tmp/transferred_packages` 包含你上一步远程拷贝过来packages，在内网服务器上执行如下命令

安装单个Package的情况

```bash
$ pip install --no-index --find-links="/tmp/tranferred_packages" <package>
```

安装多个Packages

```bash
$ pip install --no-index --find-links="/tmp/tranferred_packages" -r requirements.txt
```