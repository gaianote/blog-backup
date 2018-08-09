---
title: 用python生成一个随机的文件名
date: 2018-08-09 13:47:16
tags:
---

```python
import uuid
filename = uuid.uuid4().hex # 'ca73fa4ea3e74fb6be5bd0dc8d85b634'
```
