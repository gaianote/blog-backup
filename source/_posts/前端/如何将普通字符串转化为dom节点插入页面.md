---
title: 如何将普通字符串转化为dom节点插入页面
date: 2018-07-11 10:07:18
tags: javascript
---

## innerHTML

在elem内使用elem.innerHTML = html_str是最简单的方法

```javascript
elem = document.getElementsById('simple')
elem.innerHTML = '<h1>simple</h1>'
```
