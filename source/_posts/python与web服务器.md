---
title: python与web服务器
date: 2018-08-10 11:48:44
tags:
---

python 中自带简易的web服务器,首先cd到准备作为服务器的根目录的目录下，然后执行`http.server`命令，即可访问目录内的相关文件。目录下需要`index.html`作为主页。

<!--more-->

在python2中

```python
python -m SimpleHTTPServer 80
```

在python3中

```python
python -m http.server 80
```
