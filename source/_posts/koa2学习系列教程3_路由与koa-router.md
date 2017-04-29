---
title: koa2学习系列教程3 路由与koa-router
date: 2017-04-24 19:45:05
tags:
- koa
- nodejs
---

## 路由的基本用法

可以通过this.path属性，判断用户请求的路径，从而起到路由作用。

```javascript
app.use(async (ctx,next)=>{
  if (ctx.path === '/') {
    ctx.body = 'we are at home!';
  } else {
    await next;
  }
})

app.use(async (ctx,next)=>{
  if (ctx.path === '/404') {
    ctx.body = 'page not found';
  } else {
    await next;
  }
})
```

上面代码中，每一个中间件负责一个路径，如果路径不符合，就传递给下一个中间件。

复杂的路由需要安装koa-router插件。

## koa-router

由于api更新等问题，使用时如果未达到预想效果，可以到[npm](https://www.npmjs.com/package/koa-router)查看官方文档

### koa-router 基本的使用

```javascript
var Koa = require('koa');
var Router = require('koa-router');

var app = new Koa();
var router = new Router();

router.get('/', async (ctx, next) =>{
  ctx.body = 'we are at home!';
});

app
  .use(router.routes())
  .use(router.allowedMethods());

app.listen(3000)
```

路径匹配的时候，不会把查询字符串考虑在内。比如，/index?param=xyz 匹配路径为 /index

### HTTP动词方法

Koa-router实例提供一系列动词方法，即一种HTTP动词对应一种方法。

```javascript
router
  .get('/', async (ctx, next) => {
    ctx.body = 'Hello World!';
  })
  .post('/users', async (ctx, next) => {...})
  .put('/users/:id', async (ctx, next) => {...})
  .del('/users/:id', async (ctx, next) => {...})
  .all('/users/:id', async (ctx, next) => {...})
```

router.all()用于表示上述所有的动词方法

```javascript
router.get('/', async (ctx,next) => {
  ctx.body = 'Hello World!';
});
```

上面代码中，router.get方法的第一个参数是根路径，第二个参数是对应的函数方法。


### 路由参数

我们可以通过`ctx.params`得到URL参数

```javascript
router.get('/:category/:title', function (ctx, next) {
  console.log(ctx.params);
  // => { category: 'programming', title: 'how-to-node' }
});
```

### 支持多个中间件

```javascript
router.get(
  '/users/:id',
  function (ctx, next) {
    return User.findOne(ctx.params.id).then(function(user) {
      ctx.user = user;
      return next();
    });
  },
  function (ctx) {
    console.log(ctx.user);
    // => { id: 17, name: "Alex" }
  }
);
```


### 路由前缀

```javascript
var router = new Router({
  prefix: '/users'
});

router.get('/', ...); // responds to "/users"
router.get('/:id', ...); // responds to "/users/:id"
```

## 重构

每个 url 对应一个规则，如果全部放在 app.js 中会造成代码紊乱且难以理解。因此重构整个项目，项目文件结构如下：

```
|-controller        # 用于存放路由规则
| |-index.js        # 首页路由规则
| |-user.js         # user路由规则
|-controller.js     # 自动导入controller下的所有路由规则
|-app.js            # 入口文件，用于启动koa服务器
```

index.js 内容如下

```javascript
const homepage = async (ctx, next) =>{
  ctx.body = 'we are at home!';
}

module.exports = {
    'GET /': homepage
};
```

当 require('controller/index') 时，会得到一个包含了规则的对象 `{'GET /': homepage}` 其中，`GET` 表示 `GET` 方法 `/` 表示解析路径，`homepage` 是针对这个路径所做的操作。解析规则由 controller.js 的 `add_rule` 方法实现

controller.js 内容如下：

```javascript
const fs = require('fs')
const Router = require('koa-router');
const router = new Router();

// 解析规则 {'GET /': homepage}
function add_rule(router, rule) {
    for (let key in rule) {
        // key = 'GET /' rule = {'GET /': homepage}
        if (key.startsWith('GET ')) {
            let path = key.substring(4);
            router.get(path, rule[key]);
            console.log(`register URL mapping: GET ${path}`);
        } else if (key.startsWith('POST ')) {
            let path = key.substring(5);
            router.post(path, rule[key]);
            console.log(`register URL mapping: POST ${path}`);
        } else {
            console.log(`invalid URL: ${key}`);
        }
    }
}

//自动导入controller文件夹下所有的路由规则
function add_rules(router) {
    // 得到 /controller 所有以js结尾的文件
    let files = fs.readdirSync(__dirname + '/controller');
    let js_files = files.filter((f) => {
        return f.endsWith('.js');
    });

    // 添加规则
    for (let f of js_files) {
        console.log(`process controller: ${f}...`);
        let rule = require(__dirname + '/controller/' + f);
        add_rule(router, rule);
    }
}

module.exports = function () {
    add_rules(router);
    return router.routes();
};
```

app.js 内容如下:

```javascript
const Koa = require('koa');
const app = new Koa();

const controller = require('./controller');

//app.use(router.routes())
app.use(controller())
app.listen(3000)
```

[koa-router源码解读](http://www.tuicool.com/articles/7Zre63f)
[廖雪峰的官方网站](http://www.liaoxuefeng.com)