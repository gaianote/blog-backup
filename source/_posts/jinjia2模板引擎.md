title: jinjia2模板引擎
author: 李云鹏
date: 2018-09-30 08:22:02
tags:
---
## for循环

### for循环序号

`loop.index` 从1开始序号循环
`loop.index0` 从零开始序号循环

```html
  {% for item in items %}
    <tr>
      <th>{{loop.index}}</th>
      <td>{{item[1]}}</td>
      <td>{{item[2]}}</td>
      <td>{{item[3]}}</td>
      <td><input item_id = {{item[0]}} type="checkbox"></td>
    </tr>
  {% endfor %}
```