---
title: python一行命令启动http webserver
date: 2019-08-29 11:17:51
tags: python
---

1. 在python3中,可以使用如下命令快速启动一个简易的web服务：

```bash
$ python3 -m http.server
# 指定端口
python3 -m http.server 80
```

2. 如果希望后台运行

```bash
$ python3 -m http.server &
```

3. 如果希望保持服务，忽略所有挂断信号

```bash
$ nohub python3 -m http.server
```

4. 示例：

```bash
$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/)
```