---
title: bootstrap中table宽度设置无效解决办法
date: 2018-06-15 13:23:51
tags: web前端
---

bootstrap中需要为table设置`table-layout:fixed`属性，才可以设置table的宽度，否则设置无效

因此可以：

```html
<table style="table-layout:fixed; width:100%; height:90%;" border="1">
```

或者

```css
table {table-layout:fixed; width:100%;}
```