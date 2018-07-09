---
title: 复制一个dom的所有样式到另一个dom
date: 2018-07-05 16:31:58
tags:
---
如果不要求支持IE, 那么只要一行。

```javascript
dom.style.cssText = window.getComputedStyle(srcDom, null).cssText;
```

如果要兼容各个浏览器，那么要原始一点：

```javascript
/**
 * IE8不支持window.getComputedStyle
 * IE9~11中，window.getComputedStyle().cssText返回的总为空字符串
 * 默认的window.getComputedStyle || dom.currentStyle, 返回的css键值对中，键是驼峰命名的。
 */
var oStyle = (window.getComputedStyle && window.getComputedStyle(srcDom, null)) || srcDom.currentStyle,
    cssText = '';
for (var key in oStyle) {
    var v = oStyle[key];
    if (/^[a-z]/i.test(key) && [null, '', undefined].indexOf(v) === -1) {
        dom.style[key] = v;
    }
}
```