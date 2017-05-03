---
title: "koa2系列教程8 koa与MVVM"
date: 2017-05-03 16:10:23
tags:
---

## 什么是MVVM

什么是MVVM？MVVM是Model-View-ViewModel的缩写。

要编写可维护的前端代码绝非易事。我们已经用MVC模式通过koa实现了后端数据、模板页面和控制器的分离，但是，对于前端来说，还不够。

在了解MVVM之前，我们先回顾一下前端发展的历史。用JavaScript在浏览器中操作HTML，经历了若干发展阶段：

第一阶段，直接用JavaScript操作DOM节点，使用浏览器提供的原生API：

```javascript
var dom = document.getElementById('name');
dom.innerHTML = 'Homer';
dom.style.color = 'red';
```

第二阶段，由于原生API不好用，还要考虑浏览器兼容性，jQuery横空出世，以简洁的API迅速俘获了前端开发者的芳心：

```javascript
$('#name').text('Homer').css('color', 'red');
```

第三阶段，MVC模式，需要服务器端配合，JavaScript可以在前端修改服务器渲染后的数据。

现在，随着前端页面越来越复杂，用户对于交互性要求也越来越高，想要写出Gmail这样的页面，仅仅用jQuery是远远不够的。MVVM模型应运而生。

MVVM最早由微软提出来，它借鉴了桌面应用程序的MVC思想，在前端页面中，把Model用纯JavaScript对象表示，View负责显示，两者做到了最大限度的分离。

把Model和View关联起来的就是ViewModel。ViewModel负责把Model的数据同步到View显示出来，还负责把View的修改同步回Model。

## 安装Vue

安装Vue有很多方法，可以用npm或者webpack。但是我们现在的目标是尽快用起来，所以最简单的方法是直接在HTML代码中像引用jQuery一样引用Vue。可以直接使用CDN的地址，例如：

```html
<script src="https://unpkg.com/vue@2.0.1/dist/vue.js"></script>
```

也可以把vue.js文件下载下来，放到项目的/static/js文件夹中，使用本地路径：

```html
<script src="/static/js/vue.js"></script>
```

这里需要注意，vue.js是未压缩的用于开发的版本，它会在浏览器console中输出很多有用的信息，帮助我们调试代码。当开发完毕，需要真正发布到服务器时，应该使用压缩过的vue.min.js，它会移除所有调试信息，并且文件体积更小。

## 单向数据绑定
## 双向数据绑定

## 参考资料
