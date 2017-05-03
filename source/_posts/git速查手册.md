---
title: git速查手册
date: 2017-05-02 14:28:06
tags:
---

当一个文件提交了，但是又更新了 .gitignore 文件，可以使用如下方式删除缓存，再重新提交

```
git rm --cached file_path
```

示例，项目文件结构如下：

```
learn-js
|-node
  |-.gitignore
  |-koa2
  |-node_moudles
```

我未创建 .gitignore 文件便进行提交，之后希望忽略 node_moudles ，只需进行如下操作

```bash
git rm -r --cached node_moudles
```
