---
title: "koa2系列教程7 koa与REST规范"
date: 2017-05-03 11:17:15
tags: nodejs
---

## hello REST

```
rest-hello
|-controller
| |-api.js  # 符合 REST 规范的 product 信息管理
|-app.js
|-controller.js
```

我们在 api.js 内实现 REST 规范，用于管理 product 信息，当 GET 请求 /api/products 时，返回包含product信息的 json 字符串，当 POST 请求 /api/products 时，将新产品添加到产品列表。信息交流统一以 json 格式进行

api.js

```javascript

//用于模拟数据库，储存products产品信息，简化流程
var products = [{
    name: 'iPhone',
    price: 6999
}, {
    name: 'Kindle',
    price: 999
}];

module.exports = {

    'GET /api/products': async (ctx, next) => {
        ctx.response.type = 'application/json';
        ctx.response.body = {
            products: products
        };
    },

    'POST /api/products': async (ctx, next) => {
        var p = {
            name: ctx.request.body.name,
            price: ctx.request.body.price
        };
        products.push(p);
        ctx.response.type = 'application/json';
        ctx.response.body = p;
    }
};
```

## REST规范

### http请求规范

REST规范定义了资源的通用访问格式，虽然它不是一个强制要求，但遵守该规范可以让人易于理解。

例如，商品Product就是一种资源。获取所有Product的URL如下：

```
GET /api/products
```

而获取某个指定的Product，例如，id为123的Product，其URL如下：

```
GET /api/products/123
```

新建一个Product使用POST请求，JSON数据包含在body中，URL如下：

```
POST /api/products
```

更新一个Product使用PUT请求，例如，更新id为123的Product，其URL如下：

```
PUT /api/products/123
```

删除一个Product使用DELETE请求，例如，删除id为123的Product，其URL如下：

```
DELETE /api/products/123
```

资源还可以按层次组织。例如，获取某个Product的所有评论，使用：

```
GET /api/products/123/reviews
```

当我们只需要获取部分数据时，可通过参数限制返回的结果集，例如，返回第2页评论，每页10项，按时间排序：

```
GET /api/products/123/reviews?page=2&size=10&sort=time
```

### URL 与数据通信格式约定

在实际工程中，一个Web应用既有REST，还有MVC，可能还需要集成其他第三方系统。如何组织URL？

为了利于开发与实际应用，我们进行如下规定:

- REST API的返回值全部是`object`对象，而不是简单的number、boolean、null或者数组；

- REST API必须使用前缀/api/

## 封装 ctx.rest() 输出 json 数据

每次输出 json 数据时，都要使用 `ctx.response.type = 'application/json';` 不够又优雅，我们可以可以通过一个 middleware 给 ctx 添加一个 `rest()` 方法，直接输出JSON数据

```javascript
module.exports = {
    restify: (pathPrefix) => {
        pathPrefix = pathPrefix || '/api/';
        return async (ctx, next) => {
            if (ctx.request.path.startsWith(pathPrefix)) {
                console.log(`Process API ${ctx.request.method} ${ctx.request.url}...`);
                ctx.rest = (data) => {
                    ctx.response.type = 'application/json';
                    ctx.response.body = data;
                }
            } else {
                await next();
            }
        };
    }
};
```

此后，输出json数据时，使用 `ctx.rest(data)` 即可

```javascript
ctx.rest({products: products})
//等价于
ctx.response.type = 'application/json';
ctx.response.body = {products: products};
```

## 错误处理

### 两种错误类型

在涉及到REST API的错误时，我们必须先意识到，客户端会遇到两种类型的REST API错误。

- 403，404，500等错误，这些错误实际上是HTTP请求可能发生的错误。REST请求只是一种请求类型和响应类型均为JSON的HTTP请求，因此，这些错误在REST请求中也会发生。针对这种类型的错误，客户端除了提示用户“出现了网络错误，稍后重试”以外，并无法获得具体的错误信息。

- 业务逻辑错误，例如，输入了不合法的Email地址，试图删除一个不存在的Product，等等。这种类型的错误完全可以通过JSON返回给客户端，这样，客户端可以根据错误信息提示用户“Email不合法”等，以便用户修复后重新请求API。

### 错误响应

第一类的错误实际上客户端可以识别，并且我们也无法操控HTTP服务器的错误码。

第二类的错误信息是一个JSON字符串，例如：

```json
{
    "code": "400",
    "message": "Bad email address"
}
```

对于第二类错误的 HTTP 返回码，我们做出如下约定：正确的REST响应使用 `200`，对错误的REST响应使用 `400`

但是，要注意，绝不能混合其他HTTP错误码。例如，使用401响应“登录失败”，使用403响应“权限不够”。这会使客户端无法有效识别HTTP错误码和业务错误，，其原因在于HTTP协议定义的错误码十分偏向底层，而REST API属于“高层”协议，不应该复用底层的错误码。

### 定义错误码

我们约定使用字符串作为错误码。原因在于，使用数字作为错误码时，API提供者需要维护一份错误码代码说明表，并且，该文档必须时刻与API发布同步，否则，客户端开发者遇到一个文档上没有写明的错误码，就完全不知道发生了什么错误。

我们定义的REST API错误格式如下：

```
{
    "code": "错误代码",
    "message": "错误描述信息"
}
```

其中，错误代码命名规范为大类:子类，例如，口令不匹配的登录错误代码为 `auth:bad_password`，用户名不存在的登录错误代码为 `auth:user_not_found`。这样，客户端既可以简单匹配某个类别的错误，也可以精确匹配某个特定的错误。

### 返回错误

**使用ctx.rest()返回错误**

如果一个REST异步函数想要返回错误，一个直观的想法是调用ctx.rest()：

```javascript
user = processLogin(username, password);
if (user != null) {
    ctx.rest(user);
} else {
    ctx.response.status = 400;
    ctx.rest({
        code: 'auth:user_not_found',
        message: 'user not found'
    });
}
```

这种方式不好，因为控制流程会混乱，而且，错误只能在Controller函数中输出。

**使用throw语句抛出错误**

更好的方式是异步函数直接用throw语句抛出错误，让middleware去处理错误：

```javascript
user = processLogin(username, password);
if (user != null) {
    ctx.rest(user);
} else {
    throw new APIError('auth:user_not_found', 'user not found');
}
```

这种方式可以在异步函数的任何地方抛出错误，包括调用的子函数内部。

我们只需要稍稍改写一个middleware就可以处理错误：

```javascript
module.exports = {
    APIError: function (code, message) {
        this.code = code || 'internal:unknown_error';
        this.message = message || '';
    },
    restify: (pathPrefix) => {
        pathPrefix = pathPrefix || '/api/';
        return async (ctx, next) => {
            if (ctx.request.path.startsWith(pathPrefix)) {
                // 绑定rest()方法:
                ctx.rest = (data) => {
                    ctx.response.type = 'application/json';
                    ctx.response.body = data;
                }
                try {
                    await next();
                } catch (e) {
                    // 返回错误:
                    ctx.response.status = 400;
                    ctx.response.type = 'application/json';
                    ctx.response.body = {
                        code: e.code || 'internal:unknown_error',
                        message: e.message || ''
                    };
                }
            } else {
                await next();
            }
        };
    }
};
```

这个错误处理的好处在于，不但简化了Controller的错误处理（只需要throw，其他不管），并且，在遇到非APIError的错误时，自动转换错误码为internal:unknown_error。

受益于async/await语法，我们在middleware中可以直接用try...catch捕获异常。如果是callback模式，就无法用try...catch捕获，代码结构将混乱得多。

最后，顺便把APIError这个对象export出去。

**抛出错误
我们在 api.js 中，通过 `throw new APIError()` 返回错误：

```
'DELETE /api/products/:id': async (ctx, next) => {
        console.log(`delete product ${ctx.params.id}...`);
        var p = products.deleteProduct(ctx.params.id);
        if (p) {
            ctx.rest(p);
        } else {
            throw new APIError('product:not_found', 'product not found by id.');
        }
```

