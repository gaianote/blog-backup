---
title: koa2学习系列教程3 路由与koa-router
date: 2017-04-24 19:45:05
tags:
- koa
- nodejs
---

可以通过this.path属性，判断用户请求的路径，从而起到路由作用。

```javascript
app.use(async (ctx,next)=>{
  if (ctx.path === '/') {
    ctx.body = 'we are at home!';
  } else {
    await next;
  }
})
```

```javascript
let koa = require('koa')
let app = koa()

// normal route
app.use(function* (next) {
  if (this.path !== '/') {
    return yield next
  }

  this.body = 'hello world'
});

// /404 route
app.use(function* (next) {
  if (this.path !== '/404') {
    return yield next;
  }

  this.body = 'page not found'
});

// /500 route
app.use(function* (next) {
  if (this.path !== '/500') {
    return yield next;
  }

  this.body = 'internal server error'
});

app.listen(8080)
```

上面代码中，每一个中间件负责一个路径，如果路径不符合，就传递给下一个中间件。

复杂的路由需要安装koa-router插件。

## koa-router

由于api更新等问题，使用时如果未达到预想效果，可以到[npm](https://www.npmjs.com/package/koa-router)查看官方文档

### 基本的使用

```javascript
var Koa = require('koa');
var Router = require('koa-router');

var app = new Koa();
var router = new Router();

router.get('/', function (ctx, next) {...});

app
  .use(router.routes())
  .use(router.allowedMethods());
```

路径匹配的时候，不会把查询字符串考虑在内。比如，/index?param=xyz匹配路径/index

### HTTP动词方法

Koa-router实例提供一系列动词方法，即一种HTTP动词对应一种方法。

```javascript
router
  .get('/', function (ctx, next) {
    ctx.body = 'Hello World!';
  })
  .post('/users', function (ctx, next) {...})
  .put('/users/:id', function (ctx, next) {...})
  .del('/users/:id', function (ctx, next) {...})
  .all('/users/:id', function (ctx, next) {...});
```

router.all()用于表示上述所有的动词方法

```javascript
router.get('/', function *(next) {
  this.body = 'Hello World!';
});
```

上面代码中，router.get方法的第一个参数是根路径，第二个参数是对应的函数方法。

路径匹配的时候，不会把查询字符串考虑在内。比如，/index?param=xyz匹配路径/index

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

### 路由嵌套

```javascript
var forums = new Router();
var posts = new Router();

posts.get('/', function (ctx, next) {...});
posts.get('/:pid', function (ctx, next) {...});
forums.use('/forums/:fid/posts', posts.routes(), posts.allowedMethods());

// responds to "/forums/123/posts" and "/forums/123/posts/123"
app.use(forums.routes());
```

### 路由前缀

```javascript
var router = new Router({
  prefix: '/users'
});

router.get('/', ...); // responds to "/users"
router.get('/:id', ...); // responds to "/users/:id"
```



[koa-router源码解读](http://www.tuicool.com/articles/7Zre63f)