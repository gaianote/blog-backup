---
title: dom节点操作常用方法
date: 2018-07-06 13:00:12
tags: web前端
---

## 操作常用方法

### 访问/获取节点

```javascript
document.getElementById(id);　　　　　　　　 　　//返回对拥有指定id的第一个对象进行访问

document.getElementsByName(name);　　　　　　//返回带有指定名称的节点集合　　 注意拼写:Elements

document.getElementsByTagName(tagname); 　　//返回带有指定标签名的对象集合　  注意拼写：Elements

document.getElementsByClassName(classname);  //返回带有指定class名称的对象集合 注意拼写：Elements
```

### 创建节点/属性

```javascript
document.createElement(eName);　　//创建一个节点

document.createAttribute(attrName); //对某个节点创建属性

document.createTextNode(text);　　　//创建文本节点
```

### 添加节点

```
document.insertBefore(newNode,referenceNode);　 //在某个节点前插入节点

parentNode.appendChild(newNode);　　　　　　　　//给某个节点添加子节点
```

### 复制节点

```
cloneNode(true | false);　　//复制某个节点  参数：是否复制原节点的所有属性
```

### 删除节点

```
parentNode.removeChild(node);　　//删除某个节点的子节点 node是要删除的节点
```

注意：为了保证兼容性，要判断元素节点的节点类型(nodeType)，若nodeType==1，再执行删除操作。通过这个方法，就可以在 IE和 Mozilla 完成正确的操作。

nodeType 属性可返回节点的类型.最重要的节点类型是：

元素类型    节点类型
元素element   1
属性attr  2
文本text  3
注释comments  8
文档document  9

### 修改文本节点


|               方法              |                 作用                |
|---------------------------------|-------------------------------------|
| appendData(data);               | 将data加到文本节点后面               |
| deleteData(start,length);       | 将从start处删除length个字符         |
| insertData(start,data);         | 在start处插入字符,start的开始值是0; |
| replaceData(start,length,data); | 在start处用data替换length个字符     |
| splitData(offset);              | 在offset处分割文本节点              |
| substringData(start,length);    | 从start处提取length个字符           |

### 属性操作

```javascript
getAttribute(name)　　　　//通过属性名称获取某个节点属性的值

setAttribute(name,value);  //修改某个节点属性的值

removeAttribute(name);　 //删除某个属性
```

### 查找节点

```javascript
parentObj.firstChild;　　//如果节点为已知节点的第一个子节点就可以使用这个方法。此方法可以递归进行使用 parentObj.firstChild.firstChild.....

parentObj.lastChild;　　//获得一个节点的最后一个节点，与firstChild一样也可以进行递归使用 parentObj.lastChild.lastChild.....

parentObj.childNodes;   //获得节点的所有子节点，然后通过循环和索引找到目标节点
```

### 获取相邻的节点

```javascript
curtNode.previousSibling;  //获取已知节点的相邻的上一个节点

curtNode.nextSlbling;　　  // 获取已知节点的下一个节点
```

### 获取父节点

```javascript
childNode.parentNode;　　//得到已知节点的父节点
```

### 替换节点

```javascript
node.replaceChild(newNode,oldNode);
```

## 获取文本内容

### innerHTML

innerHTML可以作为获取文本的方法也可以作为修改文本内容的方法

element.innerHTML 会直接返回element节点下所有的HTML化的文本内容

文本
文本
document.body.innerHTML //返回"
文本
文本
"; 同样逆向的： document.body.innerHTM="
文本
"会生成
文本
文本
！注意 innerHTML方法只能作用于元素节点调用；文本节点并不能使用这个方法返回undefined！

### nodeValue

nodeValue是一个HTML DOM的对象属性；

同样的 可以通过 nodeValue设置节点的文本内容也可以直接返回文本内容

直接用节点对象调用就都可以： 如上例

document.getElementsByTagName(div)[0].childNodes[0].nodeValue //返回“文本”

另外 nodeValue 属性并不只存在于文本节点下  元素节点和属性节点对象也都具有nodeValue属性

属性节点的 nodeValue属性返回属性值
元素节点的 nodeValue属性返回null

### textContent

textContent与innerHTML方法类似会返回对象节点下所有的文本内容

但是区别为 textContent返回的内容只有去HTML化的文本节点的内容 如上例：

document.body.textContent //返回"文本文本" ！注意在DOM中标签换行产生的空白字符会计入DOM中作为文本节点

另外IE8以前不支持textContent属性

### innerText

innerText方法与textContent方法类似 并且和innerHTML一样也是作用于元素节点上

但是浏览器对于这两种方法解析空白字符的机制不一样；不是很常用

类似的还有outText outHTML等类似操作文本相关的方法，不是很常用不介绍了；

最后要提醒一点：文本与文本节点一定要区分，有些方法是依靠元素节点返回子文本内容，有些方法是文本节点返回自身文本内容，文本节点是对象而文本只是字符串；

[Dom节点操作常用方法和获取文本内容](https://www.geekjc.com/post/593dff80b5a730309bc0a31d)