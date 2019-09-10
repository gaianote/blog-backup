---
title: nodejs路径略解与path模块
date: 2017-04-23 21:19:05
tags: nodejs
---

## 绝对路径与相对路径

nodejs中有三种绝对路径和两种相对路径

* `__dirname`: 总是返回被执行的 js 所在文件夹的绝对路径
* `__filename`: 总是返回被执行的 js 文件的绝对路径
* `process.cwd()`: 总是返回运行 node 命令时所在的文件夹的绝对路径
* `./` `../`

举个例子，我有一个模块，文件结构如下：

```
app/
  -lib/
      -common.js
  -model
      -task.js
```

在app文件夹执行cmd命令 `node task.js` 结果如下：

```
__dirname : /Users/app/model
__filename : /Users/app/model/task.js
process.cwd() : /Users/app
```
在model文件夹执行cmd命令 `node task.js` 结果如下：

```
__dirname : /Users/app/model
__filename : /Users/app/model/task.js
process.cwd() : /Users/app
```
对于 ./ 有如下结论：

在 require() 中使用是跟 __dirname 的效果相同，不会因为启动脚本的目录不一样而改变，在其他情况下跟 process.cwd() 效果相同，是相对于启动脚本所在目录的路径。

因此只有在 require() 时才使用相对路径(./, ../) 的写法，其他地方一律使用绝对路径，如下：

```javascript
// 当前目录下
path.dirname(__filename) + '/task.js';
// 相邻目录下
path.resolve(__dirname, '../lib/common.js');
```

## 参考资料

[浅析 NodeJs 的几种文件路径](https://github.com/imsobear/blog/issues/48)