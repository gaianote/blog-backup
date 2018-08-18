[python爬虫神器PyQuery的使用方法](https://segmentfault.com/a/1190000005182997)

## 安装pyquery

```bash
$ pip install pyquery
```

## 初始化

在这里介绍四种初始化方式。

### 直接字符串

```python
from pyquery import PyQuery as pq
doc = pq("<html>...</html>")
```

pq 参数可以直接传入 HTML 代码，doc 现在就相当于 jQuery 里面的 `$` 符号了。

### lxml.etree

```python
from lxml import etree
doc = pq(etree.fromstring("<html></html>"))
```

可以首先用 lxml 的 etree 处理一下代码，这样如果你的 HTML 代码出现一些不完整或者疏漏，都会自动转化为完整清晰结构的 HTML代码。

### 直接传URL

```python
from pyquery import PyQuery as pq
doc = pq('http://www.baidu.com')
```

这里就像直接请求了一个网页一样，类似用 urllib2 来直接请求这个链接，得到 HTML 代码。

### 传文件

```python
from pyquery import PyQuery as pq
doc = pq(filename='hello.html')
```

可以直接传某个路径的文件名。

## 常用方法

### 得到html .html()

`doc('li')` 返回的 pyquery 对象，如果需要得到网页源代码，可以调用 `.html()` 方法

```python
from pyquery import PyQuery as pq
doc = pq("<html>...</html>")
lis = doc('li')
for li in lis.items():
    print li.html()
```

### 遍历 .items()


遍历用到 `items` 方法返回对象列表

```python
from pyquery import PyQuery as pq
doc = pq("<html>...</html>")
lis = doc('li')
for li in lis.items():
    print li.html()
```

### 得到属性 .attr()

```python
from pyquery import PyQuery as pq
doc = pq("<html>...</html>")
li = doc('li')
li.attr('id')
```

### 得到文本 .text()

```python
from pyquery import PyQuery as pq
doc = pq("<html>...</html>")
lis = doc('li')
for li in lis.items():
    print li.html()
```