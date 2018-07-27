---
title: Jinja2使用教程
date: 2018-07-26 18:36:59
tags:
---

## 安装

```
pip install Jinja2
```

## 概要

模板仅仅是文本文件。它可以生成任何基于文本的格式（HTML、XML、CSV、LaTex 等等）。它并没有特定的扩展名， .html 或 .xml 都是可以的。

模板包含 变量 或 表达式 ，这两者在模板求值的时候会被替换为值。模板中
还有标签，控制模板的逻辑。模板语法的大量灵感来自于 Django 和 Python 。

下面是一个最小的模板，它阐明了一些基础。我们会在文档中后面的部分解释细节:


```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}
</body>
</html>

```

这里有两种分隔符: `{% ... %}` 和 `{{ ... }}` 。前者用于执行诸如 for 循环或赋值的语句，后者把表达式的结果打印到模板上。

## 变量

应用把变量传递到模板，你可以使用点`.`来访问变量的属性，作为替代，也可以使用所谓的“下标”语
法`[]`。下面的几行效果是一样的:

```html
{{ foo.bar }}
{{ foo['bar'] }}
```
## 过滤器

变量可以通过 过滤器 修改。过滤器与变量用管道符号`|`分割，并且也可以用圆括号传递可选参数。多个过滤器可以链式调用，前一个过滤器的输出会被作为后一个过滤器的输入。

例如 `{{ name|striptags|title }}` 会移除 name 中的所有 HTML 标签并且改写为标题样式的大小写格式。过滤器接受带圆括号的参数，如同函数调用。这个例子会把一个列表用逗号连接起来: `{{ list|join(', ') }}` 。

下面的 [内置过滤器清单](http://docs.jinkan.org/docs/jinja2/templates.html#builtin-filters) 节介绍了所有的内置过滤器。


## 测试[¶](http://docs.jinkan.org/docs/jinja2/templates.html#tests)

除了过滤器，所谓的“测试”也是可用的。测试可以用于对照普通表达式测试一个变量。要测试一个变量或表达式，你要在变量后加上一个 is 以及测试的名称。例如，要得出一个值是否定义过，你可以用 name is defined ，这会根据 name 是否定义返回true 或 false 。

测试也可以接受参数。如果测试只接受一个参数，你可以省去括号来分组它们。例如，
下面的两个表达式做同样的事情:


```
{% if loop.index is divisibleby 3 %}
{% if loop.index is divisibleby(3) %}

```


下面的 [内置测试清单](http://docs.jinkan.org/docs/jinja2/templates.html#builtin-tests) 章节介绍了所有的内置测试。













## 参考链接
[模板设计者文档](http://docs.jinkan.org/docs/jinja2/templates.html)