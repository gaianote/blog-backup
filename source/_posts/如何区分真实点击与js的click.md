---
title: 如何区分真实点击与js的click
date: 2017-04-23 22:02:19
tags: javascript
---

## 区分真实与虚拟点击

使用event.isTrusted以及e.clientX, e.pageX可以区分真实点击与js虚拟点击

```javascript
elem  = document.querySelector('#elem_id')
elem.addEventListener('click',function(e){
  console.log(e.isTrusted,e.clientX,e.clientY,e.pageX,e.pageY)
})
```
鼠标真实点击，控制台输出了 true 60 60
通过js控制的elem.click()，控制台输出false 0 0

## 使用javascript尝试破解

对于坐标，可以通过自定义事件解决，但是坐标范围比较麻烦
而且对于浏览器底层的event.isTrusted无解
所以总体来说，js无法解决此问题

```javascript
//event = new MouseEvent(typeArg, mouseEventInit);
var event = new MouseEvent('click', {
  'screenX': 10,
  'screenY': 10,
  'clientX': 10,
  'clientY': 10
});
elem.dispatchEvent(event)
```

输出结果为 false 10 10 10 10

## 使用selinium模拟真实点击

通过自动化测试软件selinium，注入检测用js代码并执行点击操作

```python
browser.find_element_by_id("elem_id").click()
```

查看控制台输出结果为：true 633 358 633 458

[网页中，鼠标点击与javascript的click事件怎么区分](https://developer.mozilla.org/zh-CN/docs/Web/API/Event/isTrusted)
[javascript自定义事件(event)](http://blog.allenm.me/2010/02/javascript自定义事件event/)
[MouseEvent()](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)