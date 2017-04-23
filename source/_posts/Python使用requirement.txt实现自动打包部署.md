---
title: Python使用requirement.txt实现自动打包部署
date: 2017-04-23 22:07:42
tags: python
---

## 不要在本地打包依赖

python一些模块是下载源码然后本机编译的。如果本机打包模块发布在别的机器上可能会出现兼容性问题。所以，统一使用pip进行模块安装打包。

## 使用pip进行依赖部署

在开发环境中，统一运行以下命令安装依赖

```bash
sudo pip install xx
```

在开发环境中，运行以下命令导出依赖

```bash
pip freeze > requirement.txt
```

在生产环境中，执行以下命令安装依赖

```bash
pip install -r requirement.txt
```
