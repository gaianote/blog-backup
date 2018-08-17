---
title: 为python创造隔离环境
date: 2018-08-17 14:14:15
tags:
---

## Python 下各种环境隔离工具简介

virtualenv 是一个非常流行的用于创建独立的python libraries环境的工具。我强烈推荐你学习并了解它，因为他非常实用，并且应用广泛，很多人用它来搭建python开发环境。后面其他工具来主要与virtualenv来进行比较以说明差异。

### 非标准库

1.1 virtualenv 通过安装一些列的可执行和库文件到某个目录（例如：env/)，然后通过修改环境变量PATH中可执行文件(bin目录)目录的先后顺序来实现其功能，比如将 env/bin/ 放到环境变量PATH的前面。然后将一个 python或python3的可执行文件放到 env/bin/目录下，由于python运行时，会优先搜索与其路径接近的相对目录位置，这样就可达成优先使用virtualenv创建的libraries目录的目的，运行activated进入virtualenv环境后，就可以通过pip安装libraries到env/环境下

1.2 pyenv
pyenv 用于创建独立的python版本环境。例如，有可能你想要分别测试你的代码在 python2.6、2.7、3.3、3.4、3.5版本下的运行情况，那么你就需要类似pyenv这样的工具来快速切换python版本。一旦激活pyenv环境，它就将 ~/.pyenv/shims中的值放到环境变量PATH的前面，用于覆盖默认的python、pip可执行文件目录。它不会copy可执行文件，它仅仅是通过一些脚本代码基于 PYENV_VERSION或.python-version文件 来决定使用哪个python可执行文件运行python程序。另外，也可以通过 pyenv install 来安装多个python版本。

1.3 pyenv-virtualenv
pyenv-virtualenv, pyenv作者为pyenv写的一个插件，通过该插件可以让你方便的同时使用pyenv和virtualenv。另外，如果你使用的是python3.3及以上的版本，它会尝试使用venv而不是virtualenv。当然，其实你也可以自己配置同时使用pyenv和virtualenv，而不直接使用pyenv-virtualenv。

1.4 virtualenvwrapper
virtualenvwrapper 是virtualenv的一些列扩展，它提供了诸如 mkvirtualenv, lssitepackages 等命令行工具，特别是 workon 命令行工具，当你需要使用多个virtualenv目录时使用该工具特别方便。

1.5 pyenv-virtualenvwrapper
pyenv-virtualenvwrapper pyenv作者为pyenv写的另外一个插件，可方便集成virtualenvwrapper到pyenv。

1.6 pipenv
pipenv, requests 库的作者 Kenneth Reitz 编写的一个工具，目标是合并 Pipfile、pip、virtualenv 到同一个命令行工具中，实际使用中类似nodejs的依赖包管理工具npm。

### 标准库

2.1 pyvenv
pyvenv 是python3自带的的一个标准工具，但是在python3.6中已经弃用，取而代之的是 venv (python3 -m venv)。

2.2 venv
venv 是 python3 自带的命令行工具，可以通过运行 python3 -m venv 启动。另外在某些发行版中，venv需要额外安装，比如Ubuntu需要安装 python3-venv。venv和virtualenv很接近，主要差别是不需要单独copy python可执行文件到相应目录。如果你不需要支持python2，那么你可以直接使用venv。不过到目前为止，python社区仍然更偏向于使用virtuanenv。

##

二、安装过程
1.在系统中安装virtualenv，建议用pip进行安装：

```
pip install virtualenv
```

2.创建项目目录，为项目安装虚拟环境，首先创建了项目文件夹myproject，然后在该文件夹中安装了虚拟环境env。下面代码是在命令行（cmd）下输入。

```
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

4. 如果想退出虚拟环境，直接在命令行输入`deactivate`接口