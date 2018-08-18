---
title: 获取元素的CSS值
date: 2018-06-04 00:21:09
tags: javascript
---

## getComputedStyle

getComputedStyle是一个可以获取当前元素所有最终使用的CSS属性值。返回的是一个CSS样式声明对象([object CSSStyleDeclaration])，只读。

getComputedStyle() gives the final used values of all the CSS properties of an element.

语法如下：

```javascript
var style = window.getComputedStyle("元素", "伪类");
```
例如：

```javascript
var dom = document.getElementById("test"),
    style = window.getComputedStyle(dom , ":after");
```

## 参考链接

[获取元素CSS值之getComputedStyle方法熟悉](http://www.zhangxinxu.com/wordpress/2012/05/getcomputedstyle-js-getpropertyvalue-currentstyle/)