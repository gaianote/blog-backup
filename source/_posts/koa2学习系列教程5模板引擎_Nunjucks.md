---
title: koa2学习系列教程5模板引擎 Nunjucks
date: 2017-04-27 17:27:43
tags: nodejs
---

## hello Nunjucks

[Nunjucks](http://mozilla.github.io/nunjucks/)是Mozilla开发的一个纯JavaScript编写的模板引擎，语法与Python的模板引擎jinja2类似

### 目录结构

```
hello-Nunjucks/
|-views          # 用于存放模板文件
| |-hello.html   # HTML模板文件
|-app.js         # 入口js
```

### 安装Nunjucks

```bash
npm install Nunjucks --save
```

### 开始使用

app.js

```javascript
const Koa = require('koa');
const app = new Koa();

const nunjucks = require('nunjucks');
nunjucks.configure('views', { autoescape: true });

app.use(ctx => {
  ctx.body = nunjucks.render('hello.html', { name: 'nunjucks' })
});
app.listen(3000);
```

hello.html

```html
<h1>Hello {{ name }}</h1>
```

启动服务器，打开 http://127.0.0.1:3000/ 就可以看到 Hello nunjucks 的字样，是不是很简单？

## 常用语法

### for

**遍历一维数组**

```javascript
var items = [{ title: "foo", id: 1 }, { title: "bar", id: 2}];
```

```html
<h1>Posts</h1>
<ul>
{% for item in items %}
  <li>{{ item.title }}</li>
{% else %}
  <li>This would display if the 'item' collection were empty</li>
{% endfor %}
</ul>
```

**遍历二维数组**

```javascript
var points = [[0, 1, 2], [5, 6, 7], [12, 13, 14]];
```

```html
{% for x, y, z in points %}
  Point: {{ x }}, {{ y }}, {{ z }}
{% endfor %}
```

**遍历字典**

```javascript
var food = {
  'ketchup': '5 tbsp',
  'mustard': '1 tbsp',
  'pickle': '0 tbsp'
};
```

```html
{% for ingredient, amount in food %}
  Use {{ amount }} of {{ ingredient }}
{% endfor %}
```

## 模板继承

parent.html

```html
{% block header %}
This is parent top content!
{% endblock %}

<section class="left">
  {% block left %}
  {% endblock %}
</section>

<section class="right">
  {% block right %}
  This is parent right content!
  {% endblock %}
</section>
```

child.html

```html
{% extends "parent.html" %}

{% block left %}
This is child left content!
{% endblock %}

{% block right %}
This is clild right content!
{% endblock %}
```

app.js

```javascript
const Koa = require('koa');
const app = new Koa();

const nunjucks = require('nunjucks');
nunjucks.configure('views', { autoescape: true });

app.use(ctx => {
  ctx.body = nunjucks.render('child.html', { name: 'nunjucks' })
});
app.listen(3000);
```

输出结果如下:

```
This is father top content


<section class="left">

This is child left content!

</section>

<section class="right">

This is clild right content!

</section>
```

```
可以看出，继承的使用方式为：使用 `{% block <blockname> %}{% endblock %}` 进行定义，使用 `{% extends "parent.html" %}` 进行继承，重新在子页面定义的内容将被重写
```

题外话

```
当文中出现 {% block <blockname> %}{% endblock %} 的时候，hexo g 报错，是因为 hexo 模板引擎的原因;所以我将上面那句话放到了代码块中
```

## 参考资料

[Nunjucks官网文档](http://mozilla.github.io/nunjucks/getting-started.html)