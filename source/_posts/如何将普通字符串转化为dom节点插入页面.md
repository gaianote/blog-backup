---
title: 如何将普通字符串转化为dom节点插入页面
date: 2018-07-11 10:07:18
tags:
---

## innerHTML

在elem内使用elem.innerHTML = html_str是最简单的方法
整个页面(包含html)变更可以使用document.write(html_str)

## 主要转化原理
将存储在存储在字符串中的XML或HTML解析为一个DOM文档，然后使用parseFromString方法将这个DOM文档转化为一个DOM对象。选择到要插入的节点后使用append方法插入到对应的位置即可。

有点懵？没关系，继续往下看。

## 主要操作
创建DOMParser()文档
使用parseFromString()方法将DOMParser()文档转化为DOM对象
选择DOM对象中需要的节点对象
将节点对象插入html页面
代码示例
使用parseFromString()方法

```javascript
let str='<h1>Interesting</h1>';
let parser = new DOMParser();
let doc = parser.parseFromString(str, "text/xml");
let node = doc.getElementsByTagName('h1')[0];

$('#test')[0].append(node);
```

## 注意
* parseFromString转化的结果是一个document对象，无法直接进行插入操作，需提取内部节点后再插入。
* 在往table标签中插入数据时必须使用<table></table>标签包裹，否则插入的节点中parseFromString方法会将其中的tr标签和td标签自动删除。