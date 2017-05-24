koa2里面使用ES7的语法，如async、await所以需要运行在node7.6之后；但在node7.6之前也可以利用babel是的koa2可以运行。

首先项目中安装babel，和babel的几个模块：

```bash
npm install babel babel-register babel-preset-env --save
```

然后在入口文件中引入‘babel-register'模块

```bash
require('babel-register');
```

而后引入业务代码：

```bash
require('./server.js');
```

在配置.babelrc文件：

```bash
{
 "presets": [
  ["env", {
   "targets": {
    "node": true
   }
  }]
 ]
}
```

app.js:

```javascript
require('babel-register');

require('./servers/devserver');
```

devserver.js:

```javascript
var koa = require('koa');
var app = new koa();

app.use(async (ctx) => {
  await ctx.body = 'hello world!'
});

app.listen(8080);
```

[源码地址](code/koa2_with_nodejs6)