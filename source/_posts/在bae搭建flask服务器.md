---
title: 在bae搭建flask服务器
date: 2017-05-11 23:38:25
tags:
---

使用百度bae搭建flask服务器，有以下几点需要注意:

目录结构

```
app
|-app.conf
|-favicon.io
|-index.py
|-requirement.txt
```

在 `requirement.txt` 写入需要依赖的包，若没有 `requirement.txt` 文件则新建即可

```
flask
```

在 `app.conf` 更改路由规则，若不更改则 flask 路由无法访问，会返回 `404`

默认的配置只能作用于 `/`

```
handlers:
  - url : /
    script: index.py
```

更改为：

```
handlers:
  - url : /.*
    script: index.py
```

