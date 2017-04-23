---
title: npm常用命令与nodejs版本更新
date: 2017-04-23 02:02:22
tags: nodejs
---

## 更新nodejs

node有一个模块叫n，是专门用来管理node.js的版本的。

```bash
npm install -g n
n stable # 升级node.js到最新稳定版
```

可惜不支持windows，windows直接到官网下载即可

## npm 常用命令

```bash
npm -v          #显示版本，检查npm 是否正确安装。
npm install express   #安装express模块
npm install -g express  #全局安装express模块
npm list         #列出已安装模块
npm show express     #显示模块详情
npm update        #升级当前目录下的项目的所有模块
npm update express    #升级当前目录下的项目的指定模块
npm update -g express  #升级全局安装的express模块
npm uninstall express  #删除指定的模块
```
