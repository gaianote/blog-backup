---
title: requests速查手册
date: 2017-04-23 22:07:42
tags:
- python
- requests
- 爬虫
---

import requests

## get

请求网址与传递参数

```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=payload)
```

定制请求头

```python
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

超时

```python
r = requests.get(url, timeout=0.001)
```

## post

发送表单数据

```python
data = {'key':'value'}
r = requests.post(url, data=data)
```

发送json数据

```python
# requests会自动序列化data
data = {'key':'value'}
r = requests.post(url, json=data)
```
## 处理返回结果

```python
# 得到json
r.json()
```
