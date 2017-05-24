---
title: requests速查手册
date: 2017-04-23 22:07:42
tags:
- python
- requests
- 爬虫
---

## get

**请求网址与传递参数**

```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=payload)
```

**定制请求头**

```python
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
```

**超时**

```python
r = requests.get(url, timeout=0.001)
```

**短链接**

```python
r = requests.get(url,headers={'Connection':'close'})
```

## post

**发送表单数据**

```python
data = {'key':'value'}
r = requests.post(url, data=data)
```

**发送json数据**

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

## 代理ip

```python
import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

requests.get('http://example.org', proxies=proxies)
```

## 编码与解码问题

我们可以通过 `r.encoding` 查看requests抓取文件的编码

```python
r = requests.get(url)
print (r.encoding)
```

如果 Requests 检测不到正确的编码，那么你告诉它正确的是什么：

```python
response.encoding = 'gbk'
print (response.text)
```

字符串在Python内部的表示是 `unicode` 编码，因此，在做编码转换时，通常需要以 `unicode` 作为中间编码，即先将其他编码的字符串解码 `decode` 成 `unicode` ，再从 `unicode` 编码 `encode` 成另一种编码。

`decode` 的作用是将其他编码的字符串转换成unicode编码，如 `str1.decode('gb2312')`，表示将 `gb2312` 编码的字符串 `str1` 转换成 `unicode` 编码。

`encode` 的作用是将 `unicode` 编码转换成其他编码的字符串，如 `str2.encode('gb2312')`，表示将 `unicode` 编码的字符串 `str2` 转换成 `gb2312`编码。

如果一个字符串已经是 `unicode` 了，再进行解码则将出错，因此通常要对其编码方式是否为 `unicode` 进行判断，用非 `unicode` 编码形式的str来 `encode` 会报错