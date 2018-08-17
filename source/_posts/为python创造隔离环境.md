---
title: 为python创造隔离环境
date: 2018-08-17 14:14:15
tags:
---

virtualenv 是一个非常流行的用于创建独立的python libraries环境的工具。我强烈推荐你学习并了解它，因为他非常实用，并且应用广泛，很多人用它来搭建python开发环境。后面其他工具来主要与virtualenv来进行比较以说明差异。

<!--more-->

## virtualenv

1.在系统中安装virtualenv，建议用pip进行安装：

```
pip install virtualenv
```

2.创建项目目录，为项目安装虚拟环境，首先创建了项目文件夹myproject，然后在该文件夹中安装了虚拟环境env。下面代码是在命令行（cmd）下输入。

```bash
# 创建项目目录
mkdir myproject
# 进入项目目录
cd myproject
# 创建虚拟环境env
virtualenv env
```
3.启动虚拟环境，在windows中虚拟环境的启动使用命令：your_env_dir\Scripts\activate 默认情况下，virtualenv已经安装好了pip。在启动虚拟环境后直接使用pip install 命令就可以为该虚拟环境安装类库。

```
# 启动虚拟环境
env\Scripts\activate
```

4. 如果想退出虚拟环境，直接在命令行输入`deactivate`即可

### 离线使用virtualenv

执行`virtualenv env`时，virtualenv会自动安装pip等工具，离线时就会导致安装失败；

通过virtualenv.py源代码，我们可以看到它在创建venv时使用pip来安装setuptools/pip/wheel。因此，我们可以利用pip中提供的离线安装选项即可：

1. 首先下载setuptools/pip/wheel到本地setuptoolsPackages文件夹

```
pip download setuptools
pip download pip
pip download wheel
```

2. 执行以下命令生成ENV

```
# --extra-search-dir can be set multiple times, then it produces a list
virtualenv --extra-search-dir path/to/setuptoolsPackages --no-download ENV
```

3. 推出虚拟环境

```
deactivate
```
## 重定位文件路径

当我们将文件部署到其它的服务器上时，文件路径发生了变化导致虚拟环境运行失败，因此可以使用`relocatable`参数重新定位文件路径

```
virtualenv --relocatable ENV
```

## 导出项目中所需要的依赖

需要配合virtualenv环境使用,以避免导出整个环境的依赖。

```
pip freeze > requirements.txt
```

如果部署到离线服务器的话，可以:

```
mkdir packagesMirror
cd packagesMirror
pip freeze > requirements.txt
pip download -r requirements.txt
```
