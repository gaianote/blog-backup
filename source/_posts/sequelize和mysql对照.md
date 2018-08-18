---
title: sequelize和mysql对照
date: 2017-05-04 21:54:15
tags: mysql
---

## 建立数据库连接

```javascript
var sequelize = new Sequelize(
    'dbname', // 数据库名
    'username',   // 用户名
    'password',   // 用户密码
    {
        'dialect': 'mysql',  // 数据库使用mysql
        'host': 'localhost', // 数据库服务器ip
        'port': 3306,        // 数据库服务器端口
        'define': {
            // 字段以下划线（_）来分割（默认是驼峰命名风格）
            'underscored': true
        }
    }
);
```

## 定义单张表

```javascript
var User = sequelize.define(
    // 默认表名（一般这里写单数），生成时会自动转换成复数形式
    // 这个值还会作为访问模型相关的模型时的属性名，所以建议用小写形式
    'user',
    // 字段定义（主键、created_at、updated_at默认包含，不用特殊定义）
    {
        'emp_id': {
            'type': Sequelize.CHAR(10), // 字段类型
            'allowNull': false,         // 是否允许为NULL
            'unique': true              // 字段是否UNIQUE(唯一)
        },
        'nick': {
            'type': Sequelize.CHAR(10),
            'allowNull': false
        },
        'department': {
            'type': Sequelize.STRING(64),
            'allowNull': true
        }
    }
);
```

## 单表增删改查

通过Sequelize获取的模型对象都是一个DAO（Data Access Object）对象，这些对象会拥有许多操作数据库表的实例对象方法（比如：save、update、destroy等），需要获取“干净”的JSON对象可以调用get({'plain': true})。

通过模型的类方法可以获取模型对象（比如：findById、findAll等）。

### 增

Sequelize：

```javascript
// 方法1：build后对象只存在于内存中，调用save后才操作db
var user = User.build({
    'emp_id': '1',
    'nick': '小红',
    'department': '技术部'
});
user = await user.save();
console.log(user.get({'plain': true}));

// 方法2：直接操作db
var user = await  User.create({
    'emp_id': '2',
    'nick': '小明',
    'department': '技术部'
});
console.log(user.get({'plain': true}));
```

Sequelize会为主键 `id` 设置 `DEFAULT` 值来让数据库产生自增值，还将当前时间设置成了 `created_at` 和 `updated_at` 字段，非常方便。

### 改

```javascript
// 方法1：操作对象属性（不会操作db），调用save后操作db
user.nick = '小白';
user = await user.save();
console.log(user.get({'plain': true}));

// 方法2：直接update操作db
user = await user.update({
    'nick': '小白白'
});
console.log(user.get({'plain': true}));
```

更新操作时，Sequelize将将当前时间设置成了updated_at，非常方便。

如果想限制更新属性的白名单，可以这样写：

```javascript
// 方法1
user.emp_id = '33';
user.nick = '小白';
user = await user.save({'fields': ['nick']});

// 方法2
user = await user.update(
    {'emp_id': '33', 'nick': '小白'},
    {'fields': ['nick']}
});
```

这样就只会更新nick字段，而emp_id会被忽略。这种方法在对表单提交过来的一大推数据中只更新某些属性的时候比较有用。

### 删

```javascript
await user.destroy();
```

这里有个特殊的地方是，如果我们开启了paranoid（偏执）模式，destroy的时候不会执行DELETE语句，而是执行一个UPDATE语句将deleted_at字段设置为当前时间（一开始此字段值为NULL）。我们可以使用user.destroy({force: true})来强制删除，从而执行DELETE语句进行物理删除。

### 查

**查全部**

```javascript
var users = await User.findAll();
console.log(users);
```

**限制字段**

```javascript
var users = await User.findAll({
    'attributes': ['emp_id', 'nick']
});
console.log(users);
```

**字段重命名**

```javascript
var users = await User.findAll({
    'attributes': [
        'emp_id', ['nick', 'user_nick']
    ]
});
console.log(users);
```

## where子句

Sequelize的where配置项基本上完全支持了SQL的where子句的功能，非常强大。我们一步步来进行介绍。

### 基本条件

```javascript
var users = await User.findAll({
    'where': {
        'id': [1, 2, 3],
        'nick': 'a',
        'department': null
    }
});
console.log(users);
```

### 操作符

操作符是对某个字段的进一步约束，可以有多个（对同一个字段的多个操作符会被转化为AND）。

Sequelize：

```javascript
var users = await User.findAll({
    'where': {
        'id': {
            '$eq': 1,                // id = 1
            '$ne': 2,                // id != 2

            '$gt': 6,                // id > 6
            '$gte': 6,               // id >= 6

            '$lt': 10,               // id < 10
            '$lte': 10,              // id <= 10

            '$between': [6, 10],     // id BETWEEN 6 AND 10
            '$notBetween': [11, 15], // id NOT BETWEEN 11 AND 15

            '$in': [1, 2],           // id IN (1, 2)
            '$notIn': [3, 4]         // id NOT IN (3, 4)
        },
        'nick': {
            '$like': '%a%',          // nick LIKE '%a%'
            '$notLike': '%a'         // nick NOT LIKE '%a'
        },
        'updated_at': {
            '$eq': null,             // updated_at IS NULL
            '$ne': null              // created_at IS NOT NULL
        }
    }
});
```


### 条件

上面我们说的条件查询，都是AND查询，Sequelize同时也支持OR、NOT、甚至多种条件的联合查询。

**AND条件**

```javascript
var users = await User.findAll({
    'where': {
        '$and': [
            {'id': [1, 2]},
            {'nick': null}
        ]
    }
});
```

**OR条件**

```javascript
var users = await User.findAll({
    'where': {
        '$or': [
            {'id': [1, 2]},
            {'nick': null}
        ]
    }
});
```

**NOT条件**

```javascript
var users = await User.findAll({
    'where': {
        '$not': [
            {'id': [1, 2]},
            {'nick': null}
        ]
    }
});
```

### 批量操作

**插入**

```javascript
var users = yield User.bulkCreate(
    [
        {'emp_id': 'a', 'nick': 'a'},
        {'emp_id': 'b', 'nick': 'b'},
        {'emp_id': 'c', 'nick': 'c'}
    ]
);
```

这里需要注意，返回的users数组里面每个对象的id值会是null。如果需要id值，可以重新取下数据。

**更新**

```javascript
var affectedRows = yield User.update(
    {'nick': 'hhhh'},
    {
        'where': {
            'id': [2, 3, 4]
        }
    }
);
```

**删除**

```javascript
var affectedRows = yield User.destroy({
    'where': {'id': [2, 3, 4]}
});
```

## 关系

关系一般有三种：一对一、一对多、多对多。Sequelize提供了清晰易用的接口来定义关系、进行表间的操作。

### 一对一

#### 模型定义

```javascript
var User = sequelize.define('user',
    {
        'emp_id': {
            'type': Sequelize.CHAR(10),
            'allowNull': false,
            'unique': true
        }
    }
);
var Account = sequelize.define('account',
    {
        'email': {
            'type': Sequelize.CHAR(20),
            'allowNull': false
        }
    }
);

/*
 * User的实例对象将拥有getAccount、setAccount、addAccount方法
 */
User.hasOne(Account);
/*
 * Account的实例对象将拥有getUser、setUser、addUser方法
 */
Account.belongsTo(User);
```

可以看到，这种关系中外键user_id加在了Account上。另外，Sequelize还给我们生成了外键约束。

一般来说，外键约束在有些自己定制的数据库系统里面是禁止的，因为会带来一些性能问题。所以，建表的SQL一般就去掉约束，同时给外键加一个索引（加速查询），数据的一致性就靠应用层来保证了。

#### 关系操作

**增**

```javascript
var user = yield User.create({'emp_id': '1'});
var account = user.createAccount({'email': 'a'});
console.log(account.get({'plain': true}));
```

**改**

```javascript
var anotherAccount = yield Account.create({'email': 'b'});
console.log(anotherAccount);
anotherAccount = yield user.setAccount(anotherAccount);
console.log(anotherAccount);
```

**删**

```javascript
yield user.setAccount(null);
```

**查**

```javascript
var account = yield user.getAccount();
console.log(account);
```

这里就是调用user的getAccount方法，根据外键来获取对应的account。

但是其实我们用面向对象的思维来思考应该是获取user的时候就能通过user.account的方式来访问account对象。这可以通过Sequelize的eager loading（急加载，和懒加载相反）来实现。

eager loading的含义是说，取一个模型的时候，同时也把相关的模型数据也给我取过来（我很着急，不能按默认那种取一个模型就取一个模型的方式，我还要更多）。方法如下：

```javascript
var user = yield User.findById(1, {
    'include': [Account]
});
console.log(user.get({'plain': true}));
/*
 * 输出类似：
 { id: 1,
  emp_id: '1',
  created_at: Tue Nov 03 2015 15:25:27 GMT+0800 (CST),
  updated_at: Tue Nov 03 2015 15:25:27 GMT+0800 (CST),
  account:
   { id: 2,
     email: 'b',
     created_at: Tue Nov 03 2015 15:25:27 GMT+0800 (CST),
     updated_at: Tue Nov 03 2015 15:25:27 GMT+0800 (CST),
     user_id: 1 } }
 */
```

可以看到，我们对2个表进行了一个外联接，从而在取user的同时也获取到了account。

其他补充说明

如果我们重复调用user.createAccount方法，实际上会在数据库里面生成多条user_id一样的数据，并不是真正的一对一。

所以，在应用层保证一致性时，就需要我们遵循良好的编码约定。新增就用user.createAccount，更改就用user.setAccount。

也可以给user_id加一个UNIQUE约束，在数据库层面保证一致性，这时就需要做好try/catch，发生插入异常的时候能够知道是因为插入了多个account。

另外，我们上面都是使用user来对account进行操作。实际上反向操作也是可以的，这是因为我们定义了Account.belongsTo(User)。在Sequelize里面定义关系时，关系的调用方会获得相关的“关系”方法，一般为了两边都能操作，会同时定义双向关系（这里双向关系指的是模型层面，并不会在数据库表中出现两个表都加上外键的情况，请放心）。

### 一对多

#### 模型定义

```javascript
var User = sequelize.define('user',
    {
        'emp_id': {
            'type': Sequelize.CHAR(10),
            'allowNull': false,
            'unique': true
        }
    }
);
var Note = sequelize.define('note',
    {
        'title': {
            'type': Sequelize.CHAR(64),
            'allowNull': false
        }
    }
);

/*
 * User的实例对象将拥有getNotes、setNotes、addNote、createNote、removeNote、hasNote方法
 */
User.hasMany(Note);
/*
 * Note的实例对象将拥有getUser、setUser、createUser方法
 */
Note.belongsTo(User);
```

#### 关系操作

**增**

```javascript
//方法1
var user = yield User.create({'emp_id': '1'});
var note = yield user.createNote({'title': 'a'});
console.log(note);
//方法2
var user = yield User.create({'emp_id': '1'});
var note = yield Note.create({'title': 'b'});
yield user.addNote(note);
```

**改**

```javascript
// 为user增加note1、note2
var user = yield User.create({'emp_id': '1'});
var note1 = yield user.createNote({'title': 'a'});
var note2 = yield user.createNote({'title': 'b'});
// 先创建note3、note4
var note3 = yield Note.create({'title': 'c'});
var note4 = yield Note.create({'title': 'd'});
// user拥有的note更改为note3、note4
yield user.setNotes([note3, note4]);
```

**删**

```javascript
yield user.removeNote(note);
```

**查**

情况1

查询user的所有满足条件的note数据。

```javascript
var notes = yield user.getNotes({
    'where': {
        'title': {
            '$like': '%css%'
        }
    }
});
notes.forEach(function(note) {
    console.log(note);
});
```

情况2

查询所有满足条件的note，同时获取note属于哪个user。

```javascript
var notes = yield Note.findAll({
    'include': [User],
    'where': {
        'title': {
            '$like': '%css%'
        }
    }
});
notes.forEach(function(note) {
    // note属于哪个user可以通过note.user访问
    console.log(note);
});
```

情况3

查询所有满足条件的user，同时获取该user所有满足条件的note。

```javascript
var users = yield User.findAll({
    'include': [Note],
    'where': {
        'created_at': {
            '$lt': new Date()
        }
    }
});
users.forEach(function(user) {
    // user的notes可以通过user.notes访问
    console.log(user);
});
```

### 多对多关系

在多对多关系中，必须要额外一张关系表来将2个表进行关联，这张表可以是单纯的一个关系表，也可以是一个实际的模型（含有自己的额外属性来描述关系）。我比较喜欢用一个模型的方式，这样方便以后做扩展。

#### 模型定义

```javascript
var Note = sequelize.define('note',
    {
        'title': {
            'type': Sequelize.CHAR(64),
            'allowNull': false
        }
    }
);
var Tag = sequelize.define('tag',
    {
        'name': {
            'type': Sequelize.CHAR(64),
            'allowNull': false,
            'unique': true
        }
    }
);
var Tagging = sequelize.define('tagging',
    {
        'type': {
            'type': Sequelize.INTEGER(),
            'allowNull': false
        }
    }
);

// Note的实例拥有getTags、setTags、addTag、addTags、createTag、removeTag、hasTag方法
Note.belongsToMany(Tag, {'through': Tagging});
// Tag的实例拥有getNotes、setNotes、addNote、addNotes、createNote、removeNote、hasNote方法
Tag.belongsToMany(Note, {'through': Tagging});
```

**增**

方法1

```javascript
var note = yield Note.create({'title': 'note'});
yield note.createTag({'name': 'tag'}, {'type': 0});
```

方法2


```javascript
var note = yield Note.create({'title': 'note'});
var tag = yield Tag.create({'name': 'tag'});
yield note.addTag(tag, {'type': 1});
```

方法3

```javascript
var note = yield Note.create({'title': 'note'});
var tag1 = yield Tag.create({'name': 'tag1'});
var tag2 = yield Tag.create({'name': 'tag2'});
yield note.addTags([tag1, tag2], {'type': 2});
```

**改**

```javascript
// 先添加几个tag
var note = yield Note.create({'title': 'note'});
var tag1 = yield Tag.create({'name': 'tag1'});
var tag2 = yield Tag.create({'name': 'tag2'});
yield note.addTags([tag1, tag2], {'type': 2});
// 将tag改掉
var tag3 = yield Tag.create({'name': 'tag3'});
var tag4 = yield Tag.create({'name': 'tag4'});
yield note.setTags([tag3, tag4], {'type': 3});
```

**删**

```javascript
// 先添加几个tag
var note = yield Note.create({'title': 'note'});
var tag1 = yield Tag.create({'name': 'tag1'});
var tag2 = yield Tag.create({'name': 'tag2'});
var tag3 = yield Tag.create({'name': 'tag2'});
yield note.addTags([tag1, tag2, tag3], {'type': 2});

// 删除一个
yield note.removeTag(tag1);

// 全部删除
yield note.setTags([]);
```

删除一个很简单，直接将关系表中的数据删除。

全部删除时，首先需要查出关系表中note_id对应的所有数据，然后一次删掉。

**查**

情况1

查询note所有满足条件的tag。

```javascript
var tags = yield note.getTags({
    //这里可以对tags进行where
});
tags.forEach(function(tag) {
    // 关系模型可以通过tag.tagging来访问
    console.log(tag);
});
```

情况2

查询所有满足条件的tag，同时获取每个tag所在的note。

```javascript
var tags = yield Tag.findAll({
    'include': [
        {
            'model': Note
            // 这里可以对notes进行where
        }
    ]
    // 这里可以对tags进行where
});
tags.forEach(function(tag) {
    // tag的notes可以通过tag.notes访问，关系模型可以通过tag.notes[0].tagging访问
    console.log(tag);
});
```

情况3

查询所有满足条件的note，同时获取每个note所有满足条件的tag。

```javascript
var notes = yield Note.findAll({
    'include': [
        {
            'model': Tag
            // 这里可以对tags进行where
        }
    ]
    // 这里可以对notes进行where
});
notes.forEach(function(note) {
    // note的tags可以通过note.tags访问，关系模型通过note.tags[0].tagging访问
    console.log(note);
});
```

## 参考资料

[sequelize和mysql对照](https://segmentfault.com/a/1190000003987871)