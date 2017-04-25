---
title: nodejs与mysql数据库
tags:
  - nodejs
  - mysql
date: 2017-04-25 20:31:36
---


## ORM

如果直接使用mysql包提供的接口，我们编写的代码就比较底层，例如，查询代码：

```javascript
connection.query('SELECT * FROM users WHERE id = ?', ['123'], function(err, rows) {
  for (let row in rows) {
      processRow(row);
  }
});
```

考虑到数据库表是一个二维表，包含多行多列，例如一个pets的表：

```
mysql> select * from pets;
+----+--------+------------+
| id | name   | birth      |
+----+--------+------------+
|  1 | Gaffey | 2007-07-07 |
|  2 | Odie   | 2008-08-08 |
+----+--------+------------+
2 rows in set (0.00 sec)
```

每一行可以用一个JavaScript对象表示，例如第一行：

```
{
  "id": 1,
  "name": "Gaffey",
  "birth": "2007-07-07"
}
```

这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上

但是由谁来做这个转换呢？所以ORM框架应运而生。

## ORM框架 Sequelize

我们选择Node的ORM框架Sequelize来操作数据库。这样，我们读写的都是JavaScript对象，Sequelize帮我们把对象变成数据库中的行。

用Sequelize查询pets表，代码像这样：

```javascript
Pet.findAll()
   .then(function (pets) {
       for (let pet in pets) {
           console.log(`${pet.id}: ${pet.name}`);
       }
   }).catch(function (err) {
       // error
   });
```

因为Sequelize返回的对象是Promise，所以我们可以用then()和catch()分别异步响应成功和失败。

但是用then()和catch()仍然比较麻烦。有没有更简单的方法呢？

可以用ES7的await来调用任何一个Promise对象，这样我们写出来的代码就变成了：

```javascript
(async () => {
    var pets = await Pet.findAll();
})();
```

真的就是这么简单！

考虑到koa的处理函数都是async函数，所以我们实际上将来在koa的async函数中直接写await访问数据库就可以了！

这也是为什么我们选择Sequelize的原因：只要API返回Promise，就可以用await调用，写代码就非常简单！

## 使用 Sequelize

```bash
npm install sequelize
npm mysql
```

注意mysql是驱动，我们不直接使用，但是sequelize会用

配置config.js,他是一个简单的配置文件

```javascript
var config = {
    database: 'test', // 使用哪个数据库
    username: 'www', // 用户名
    password: 'www', // 口令
    host: 'localhost', // 主机名
    port: 3306 // 端口号，MySQL默认3306
};

module.exports = config;
```

第一步，创建一个sequelize对象实例：

```javascript
const Sequelize = require('sequelize');
const config = require('./config');

var sequelize = new Sequelize(config.database, config.username, config.password, {
    host: config.host,
    dialect: 'mysql',
    pool: {
        max: 5,
        min: 0,
        idle: 30000
    }
});
```

第二步，定义模型Pet，告诉Sequelize如何映射数据库表：

```javascript
var Pet = sequelize.define('pet', {
    id: {
        type: Sequelize.STRING(50),
        primaryKey: true
    },
    name: Sequelize.STRING(100),
    gender: Sequelize.BOOLEAN,
    birth: Sequelize.STRING(10),
    createdAt: Sequelize.BIGINT,
    updatedAt: Sequelize.BIGINT,
    version: Sequelize.BIGINT
}, {
        timestamps: false
    });
```

用sequelize.define()定义Model时，传入名称pet，默认的表名就是pets。第二个参数指定列名和数据类型，如果是主键，需要更详细地指定。第三个参数是额外的配置，我们传入{ timestamps: false }是为了关闭Sequelize的自动添加timestamp的功能。所有的ORM框架都有一种很不好的风气，总是自作聪明地加上所谓“自动化”的功能，但是会让人感到完全摸不着头脑。

### 插入数据

```javascript
(async () => {
    var dog = await Pet.create({
        id: 'd-' + now,
        name: 'Odie',
        gender: false,
        birth: '2008-08-08',
        createdAt: now,
        updatedAt: now,
        version: 0
    });
    console.log('created: ' + JSON.stringify(dog));
})();
```

显然await代码更胜一筹。

### 查询数据

```javascript
(async () => {
    var pets = await Pet.findAll({
        where: {
            name: 'Gaffey'
        }
    });
    console.log(`find ${pets.length} pets:`);
    for (let p of pets) {
        console.log(JSON.stringify(p));
    }
})();
```

### 更新数据，可以对查询到的实例调用save()方法：

```javascript
(async () => {
    var p = await queryFromSomewhere();
    p.gender = true;
    p.updatedAt = Date.now();
    p.version ++;
    await p.save();
})();
```

### 删除数据，可以对查询到的实例调用destroy()方法：

```javascript
(async () => {
    var p = await queryFromSomewhere();
    await p.destroy();
})();
```

参考文档

[廖雪峰的官方网站](http://www.liaoxuefeng.com)
[Sequelize官方文档](http://docs.sequelizejs.com)