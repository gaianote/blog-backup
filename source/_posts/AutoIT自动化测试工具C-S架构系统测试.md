---
title: AutoIT自动化测试工具C/S架构系统测试
date: 2018-06-12 17:39:38
tags:
---

## AutoIT 介绍
### AutoIt 简介
AutoIt是用以编写并生成具有BASIC语言风格的脚本程序的免费软件，它被设计用来在WindowsGUI(用户界面)中进行自动操作。通过它可以组合使用模拟键击，鼠标移动和窗口/控件操作等来实现自动化任务。AutoIt非常小巧，可以在所有windows操作系统上运行，且不需要任何运行库。官网：https://www.autoitscript.com

### AutoIt 下载安装
直接从官网下载最新版本（v3.3.14.2）后安装即可，下载地址：https://www.autoitscript.com/site/autoit/downloads/

### AutoIt 快速入门

1. 首先安装完成之后，你会看到AutoIt v3安装目录：

其中`AutoIt Help File`是帮助手册，`AutoIt Window Info`是窗口信息工具（x64或x86分别代表64位或32位版本），`Compile Script to .exe`是打包工具（打包au3脚本为exe文件），`Run Script`是运行脚本工具，`SciTE Script Editor`是脚本编辑器即IDE。



2. 我们运行SciTE Script Editor，输入如下代码（弹出消息框，输出Hello World）

```
MsgBox(0,'Hello World','AutoIt Demo by Lovesoo')
```

3. Ctrl+S保存当前文件

4. F5运行文件

## pyautoit

autoit支持python，只需下载相应的库pyautoit

### 安装

可以使用pip直接安装

```
pip install -U pyautoit
```

或者下载到本地后安装

```
git clone https://github.com/jacexh/pyautoit.git
cd pyautoit-master
python setup.py install
```
参考资料:

[自动化工具 C/S 架构系统自动化测试入门](https://testerhome.com/topics/11105)