---
title: python内网电脑离线/使用代理安装依赖
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

## pip使用代理安装依赖包

正常网络情况下我们安装如果比较多的python包时，会选择使用pip install -r requirements.txt -i https://pypi.douban.com/simple --trusted-host=pypi.douban.com这种国内的镜像来加快下载速度。 
但是，当这台被限制上网时（公司安全考虑）就不能连外网了，如果懒得一个个下载，又懒得找运维开网络权限时，可以选择设置代理来解决。

## 有三种常用方式：

### ①永久设置：

```bash
vim /etc/profile：
    export http_proxy='http://代理服务器IP:端口号'
    export https_proxy='http://代理服务器IP:端口号'
source /etc/profile
```

### ②临时设置（重连后失效）： 

```bash
export http_proxy='http://192.168.71.60:1080'
export https_proxy='http://192.168.71.60:1080'
```
注意：设置之后可能使用ping时还是无法连接外网，但是pip时可以的，因为ping的协议不一样不能使用这个代理

### ③单次设置： 

直接在pip时设置代理也是可以的： 

```bash
pip install -r requirements.txt --proxy=代理服务器IP:端口号
```