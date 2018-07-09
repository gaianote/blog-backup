---
title: 从零开始flask学习
date: 2018-07-09 19:05:30
tags: python
---

## 静态文件

静态文件指网页需要引入的img,css,js等文件

flask的静态文件都需要位于应用的 `/static` 中:

```
|-templates
|    |-index.html
|-static
|    |-css
|        |-demo.css
|-app.js
```

有两种方法引入静态文件：

1. 直接在html模板中引用该路径，如下：

index.html

```html
<link href="/static/css/demo.css" rel="stylesheet" type="text/css" />
```

2. 在app.js中使用url_for构造路径,然后在html模板中引入变量:

app.js

```python
@app.router("/")
def template():
    demo_css = url_for('static',filename = 'css/demo.css')
    return render_template('index.html',demo_css = demo_css)
```
index.html

```html
<link href="{{demo_css}}" rel="stylesheet" type="text/css" />
```
