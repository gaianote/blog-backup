---
title: GUI自动化测试框架思路
date: 2018-07-11 15:14:40
tags:
---

## 可测试方向分析

前端自动化测试的方向有：

* 单元测试
* UI回归测试
* 功能测试
* 性能测试

## 单元测试

在计算机编程中，单元测试（Unit Testing）又称为模块测试, 是针对程序模块（软件设计的最小单位）来进行正确性检验的测试工作。

常用的单元测试框架有：

* AVA
* Jest
* Mocha
* Jasmine
* Tape

## UI回归测试

UI回归测试主要有两种方式

* 截图后像素对比
* dom树差异对比

主要的步骤为：

1. 快照截图，得到基准页面
2. 测试时与基准页面对比，如果相同则测试通过
3. 如果不相同则提示错误，或者更新基准页面

## PhantomFlow介绍

* PhantomFlow是基于决策树(decision tree)的ui test 框架，是对PhantomJS、CasperJS、PhantomCSS的包装。

## 持续集成

持续集成（Continuous integration，CI），一种软件工程流程，指工程师将自己对于软件的复本，每天集成数次到主干上。在测试驱动开发（TDD）的做法中，通常还会搭配自动单元测试。

[基于PhantomFlow的自动化UI测试](https://juejin.im/post/59c131c9518825396f4f617d)