---
title: requests速查手册
date: 2017-04-23 22:07:42
tags:
- python
- requests
- 爬虫
---

import requests

## get与post

```python
# 请求网址与传递参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=payload)
```

```python
# 定制请求头
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

```python
# 超时
r = requests.get(url, timeout=0.001)
```

处理返回结果

```python
# 得到json
r.json()
```
