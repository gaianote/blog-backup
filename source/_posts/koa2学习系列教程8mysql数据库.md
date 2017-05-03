---
title: koa2学习系列教程8 mysql数据库
tags:
  - nodejs
  - mysql
date: 2017-04-25 20:31:36
---

## 在命令行使用mysql

### 安装mysql

对于mysql，我们除了在官网下载安装包以外，还可以使用XAMPP建站集成环境进行安装，安装完成后打开MySQL模块即可使用

### 添加环境变量

找到mysql的bin文件夹，将其添加到环境变量路径，方便在cmd中使用mysql

添加方法：使用win自带的搜索功能，搜索环境变量，进入编辑环境变量后选择**用户环境变量**，选择PATH后编辑，选择新建，输入mysql的bin路径，比如我的是 E:\xampp\mysql\bin

编辑PATH完成后，cmd重启生效

### 命令行的基本操作

**连接数据库**

```bash
$ mysql -h localhost -u root -p
```

要求输入password时，假如未设定，直接回车即可

**显示用户名下的所有数据库**

```bash
$ show databases;
```

注意sql语句要求以';'结尾，执行命令后，会输出形如下列的表格

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mynote             |
| mysql              |
| performance_schema |
| phpmyadmin         |
+--------------------+
```

**进入某个数据库**

```bash
$ use databasename
```

**退出mysql**

```bash
$ exit;
```

## MYSQL 与 ORM

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
npm install sequelize --save
npm install mysql --save
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

## Model

为了避免格式上的混乱，我们需要一个统一的模型，强迫所有Model都遵守同一个规范，这样不但实现简单，而且容易统一风格。

我们首先要定义的就是Model存放的文件夹必须在models内，并且以Model名字命名，例如：Pet.js，User.js等等。

其次，每个Model必须遵守一套规范：

- 统一主键，名称必须是`id`，类型必须是`STRING(50)`；
- 主键可以自己指定，也可以由框架自动生成（如果为`null`或`undefined`）；
- 所有字段默认为`NOT NULL`，除非显式指定；
- 统一`timestamp`机制，每个Model必须有`createdAt`、`updatedAt`和`version`，分别记录创建时间、修改时间和版本号。其中，`createdAt`和`updatedAt`以`BIGINT`存储时间戳，最大的好处是无需处理时区，排序方便。`version`每次修改时自增。

### 数据库配置

接下来，我们把简单的config.js拆成3个配置文件：

- config-default.js：存储默认的配置;
- config-override.js：存储特定的配置;
- config-test.js：存储用于测试的配置;

例如，默认的config-default.js可以配置如下：

```javascript
var config = {
    dialect: 'mysql',
    database: 'nodejs',
    username: 'www',
    password: 'www',
    host: 'localhost',
    port: 3306
};


module.exports = config;
```

而config-override.js可应用实际配置：

```javascript
var config = {
    database: 'production',
    username: 'www',
    password: 'secret-password',
    host: '192.168.1.199'
};

module.exports = config;
```

config-test.js可应用测试环境的配置：

```javascript
var config = {
    database: 'test'
};
module.exports = config;
```

读取配置的时候，我们用config.js实现不同环境读取不同的配置文件：

```javascript
const defaultConfig = './config-default.js';
// 可设定为绝对路径，如 /opt/product/config-override.js
const overrideConfig = './config-override.js';
const testConfig = './config-test.js';

const fs = require('fs');

var config = null;

if (process.env.NODE_ENV === 'test') {
    console.log(`Load ${testConfig}...`);
    config = require(testConfig);
} else {
    console.log(`Load ${defaultConfig}...`);
    config = require(defaultConfig);
    try {
        if (fs.statSync(overrideConfig).isFile()) {
            console.log(`Load ${overrideConfig}...`);
            config = Object.assign(config, require(overrideConfig));
        }
    } catch (err) {
        console.log(`Cannot load ${overrideConfig}.`);
    }
}

module.exports = config;
```

具体的规则是：

先读取config-default.js；
如果不是测试环境，就读取config-override.js，如果文件不存在，就忽略。
如果是测试环境，就读取config-test.js。
这样做的好处是，开发环境下，团队统一使用默认的配置，并且无需config-override.js。部署到服务器时，由运维团队配置好config-override.js，以覆盖config-override.js的默认设置。测试环境下，本地和CI服务器统一使用config-test.js，测试数据库可以反复清空，不会影响开发。

配置文件表面上写起来很容易，但是，既要保证开发效率，又要避免服务器配置文件泄漏，还要能方便地执行测试，就需要一开始搭建出好的结构，才能提升工程能力。

### 使用Model

要使用Model，就需要引入对应的Model文件，例如：User.js。一旦Model多了起来，如何引用也是一件麻烦事。

自动化永远比手工做效率高，而且更可靠。我们写一个model.js，自动扫描并导入所有Model：

```javascript
const fs = require('fs');
const db = require('./db');

let files = fs.readdirSync(__dirname + '/models');

let js_files = files.filter((f)=>{
    return f.endsWith('.js');
}, files);

module.exports = {};

for (let f of js_files) {
    console.log(`import model from file ${f}...`);
    let name = f.substring(0, f.length - 3);
    module.exports[name] = require(__dirname + '/models/' + f);
}

module.exports.sync = () => {
    return db.sync();
};
```

这样，需要用的时候，写起来就像这样：

```javascript
const model = require('./model');

let
    Pet = model.Pet,
    User = model.User;

var pet = await Pet.create({ ... });
```

### 工程结构

最终，我们创建的工程model-sequelize结构如下：

```
model-sequelize/
|
|-.vscode
|  |-launch.json    # VSCode 配置文件
|-models            # 存放所有Model
|  |-Pet.js         # Pet
|  |-User.js        # User
|-config.js         # 配置文件入口
|-config-default.js # 默认配置文件
|-config-test.js    # 测试配置文件
|-db.js             # 如何定义Model
|-model.js          # 如何导入Model
|-init-db.js        # 初始化数据库
|-app.js            # 业务代码
|-package.json      # 项目描述文件
|-node_modules/     # npm安装的所有依赖包
```

注意到我们其实不需要创建表的SQL，因为Sequelize提供了一个`sync()`方法，可以自动创建数据库。这个功能在开发和生产环境中没有什么用，但是在测试环境中非常有用。测试时，我们可以用`sync()`方法自动创建出表结构，而不是自己维护SQL脚本。这样，可以随时修改Model的定义，并立刻运行测试。开发环境下，首次使用`sync()`也可以自动创建出表结构，避免了手动运行SQL的问题。

init-db.js的代码非常简单，作用是创建Pets和User表，只需要执行一次即可。


```javascript
const model = require('./model.js');

model.sync().then(()=>{
    console.log('sync done');
    process.exit(0);
}).catch((e)=>{
    console.log('failed with: '+e);
    process.exit(0);});

console.log('init db ok.');
```
参考文档

[廖雪峰的官方网站](http://www.liaoxuefeng.com)
[Sequelize官方文档](http://docs.sequelizejs.com)