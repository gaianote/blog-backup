---
title: js实现通过xpath选择元素
date: 2018-06-25 10:43:55
tags: web前端
---

## 使用js实现xpath选择元素的功能

```javascript
function query_by_xpath(STR_XPATH) {
    var xresult = document.evaluate(STR_XPATH, document, null, XPathResult.ANY_TYPE, null);
    var xnodes = [];
    var xres;
    while (xres = xresult.iterateNext()) {
        xnodes.push(xres);
    }

    return xnodes;
}
```

## 通过chrome快速复制元素xpath

使用chrome的开发者模式可以快速复制元素的xpath，方便开发时调用。如图：

![通过chrome快速复制元素xpath](/images/180625xpath.png)