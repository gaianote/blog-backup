---
title: node模块与commonjs规范
date: 2017-04-28 17:37:19
tags: nodejs
---


Node应用由模块组成，采用CommonJS模块规范。

根据这个规范，每个文件就是一个模块，有自己的作用域。在一个文件里面定义的变量、函数、类，都是私有的，对其他文件不可见。

## 定义模块

```javascript
// example.js
var invisible = function () {
  console.log("invisible");
}

exports.message = "hi";

exports.say = function () {
  console.log(message);
}
```

运行下面的命令，可以输出exports对象。

```javascript
var example = require('./example.js');
example
// {
//   message: "hi",
//   say: [Function]
// }
```

如果模块输出的是一个函数，那就不能定义在exports对象上面，而要定义在module.exports变量上面。

```javascript
module.exports = function () {
  console.log("hello world")
}

require('./example2.js')()
```

上面代码中，require命令调用自身，等于是执行module.exports，因此会输出 hello world。

## 加载规则

require命令的基本功能是，读入并**执行**一个JavaScript文件，然后返回该模块的exports对象。如果没有发现指定模块，会报错。

### require 路径规则

require命令用于加载文件，后缀名默认为.js。

```javascript
var foo = require('foo');
//  等同于
var foo = require('foo.js');
```

根据参数的不同格式，require命令去不同路径寻找模块文件。

- 如果参数字符串以“/”开头，则表示加载的是一个位于绝对路径的模块文件。比如，require('/home/marco/foo.js')将加载/home/marco/foo.js。

- 如果参数字符串以“./”开头，则表示加载的是一个位于相对路径（跟当前执行脚本的位置相比）的模块文件。比如，require('./circle')将加载当前脚本同一目录的circle.js。

- 如果参数字符串不以“./“或”/“开头，则表示加载的是一个默认提供的核心模块（位于Node的系统安装目录中），或者一个位于各级node_modules目录的已安装模块（全局安装或局部安装）。

### 引入的同时执行了被引入模块

son.js

```javascript
console.log(msg)
module.exports = function () {
  console.log(msg)
}
```

father.js

```javascript
msg = 'hello world'
const foo = require('./child')
foo()
```

输出结果为:

```
hello world
hello world
```

## 模块之间变量不共享




