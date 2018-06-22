---
title: python3-cookbook学习笔记
date: 2018-06-21 14:10:38
tags:
---

## 第一章:数据结构和算法

### 1.4 查找最大或最小的 N 个元素（列表）
* 怎样从一个集合中获得最大或者最小的 N 个元素列表？`heapq` 模块有两个函数：`nlargest()` 和 `nsmallest()`
* 列表元素是数字：`heapq.nlargest(3, list)` 返回list中包含最大的三个元素的列表
* 列表元素是字典：`heapq.nsmallest(3, portfolio, key=lambda s: s['price'])` 返回所有字典的以price key键对应的值的最小值。

### 1.6 字典中的键映射多个值
* 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中， 比如列表或者集合里面
* 你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。比如`dic = defaultdict(set) dic['a'].add(1)`
* 自己实现需要使用if判断key是否存在，不够简洁。

### 1.7 字典排序
* 为了能控制一个字典中元素的顺序，你可以使用collections 模块中的 OrderedDict 类。 在迭代操作的时候它会保持元素被插入(创建)时的顺序
* 一个 OrderedDict 的大小是一个普通字典的两倍,数据量过大时需要仔细衡量

### 1.8 字典的运算
* 为了对字典值执行计算操作(得到值的最大值等)，通常需要使用 zip() 函数先将键和值反转过来 `min_price = min(zip(prices_dict.values(), prices_dict.keys()))`
* zip() 函数创建的是一个只能访问一次的迭代器，赋值给变量后，第二次访问会报错。

### 1.17 从字典中提取子集
* 使用**字典推导**的方式创建新字典，运行速度是更快的;通过if后面的条件不同，可以得到不同的新字典
* 通过value获得新字典：`dict1 = {key: value for key, value in base_dict.items() if value > 200}`
* 通过key值获得新字典：`dict2 = {key: value for key, value in base_dict.items() if key in ["name","price"]}`

### 1.18 映射名称到序列元素
* `collections.namedtuple()`工厂函数生成的实例可以将tuple转换为nametuple，并通过名称去访问元组元素，为代码增加可读性。
* `namedtuple()`跟元组类型是可交换的，支持所有的普通元组操作,和字典的区别主要在于命名元组是不可更改的

### 1.19 转换并同时计算数据
* 生成器表达式 x * x for x in nums => result（for x in list）if ()=> 对列表中的每一个对象进行同样的操作，后面可以加if作为条件。返回result，形成新的列表
* 生成器表达式返回的是一个`<generator object>` ,你可以使用`[x * x for x in nums]`,形成临时列表再去使用`sum()`调用它，或者直接使用`sum(x * x for x in nums)`,得出结果。后一种方案是更省内存的。

### 1.20 合并多个字典或映射
* collections模块中的 ChainMap 将字典从逻辑上合并为一个单一的映射后执行某些操作，如果key值重复，任何操作都将指向第一个字典的key
* 当使用ChainMap映射的原字典更新了内容，ChainMap可以获取到最新的值。而update方法不可以。

## 第二章:字符串和文本

### 2.1 使用多个界定符分割字符串

* string 对象的 split() 方法只适应于非常简单的字符串分割情形， 它并不允许有多个分隔符或者是分隔符周围不确定的空格。
* 当你需要更加灵活的切割字符串的时候，最好使用 re.split() 方法：`re.split(r'[;,\s]\s*', line)`
* 当partern使用分组时，分组里的内容也会被传入数组中：`fields = re.split(r'(;|,|\s)\s*', line)`

### 2.2 字符串开头或结尾匹配

* 检查字符串开头或结尾的一个简单方法是使用 `str.startswith()` 或者是 `str.endswith()` 方法,返回`True`或`False`
* 多种匹配可能，只需要将所有的匹配项放入到一个tuple中去(必须时tuple，list类型不可以，需要转换)， 然后传给 `startswith()` 或者 `endswith()` 方法: `strline.startswith(('.py','.json'))`
* 得到固定类型的文件名列表：`[name for name in filenames if name.endswith(('.c', '.h')) ]`
* 判断是否有某种类型的文件: `any(name.endswith('.py') for name in filenames)`

### 2.4 字符串匹配和搜索

* 如果你想匹配的是**字面字符串**，那么你通常只需要调用基本字符串方法就行， 比如 `str.find()` , `str.endswith()` , `str.startswith()` 或者类似的方法
* 当写正则式字符串的时候，相对普遍的做法是使用原始字符串比如 `r'(\d+)/(\d+)/(\d+)'`。 这种字符串将不去解析反斜杠，如果不这样做的话，你必须使用两个反斜杠，类似 `'(\\d+)/(\\d+)/(\\d+)'` 。
* 在正则中使用分组()的作用是，可以方便的调用group()方法得到相应的分组内容

### 2.5 字符串搜索和替换
* 对于简单的字面模式，直接使用字符串方法 `str.replace(base_word,new_word)` 方法即可，它会将所有的`base_word`替换为`new_word`
* 对于复杂的替换可以使用`re.complain(pattern).sub(new_word,base_str)`

### 2.6 字符串忽略大小写的搜索替换
* 为了在文本操作时忽略大小写，你需要在使用 re 模块的时候给这些操作提供 `re.IGNORECASE` 标志参数。
* 默认情况下，正则方法和字符串的搜索方法都是大小写严格匹配的

### 2.7 最短匹配模式
* 贪婪模式: `re.compile(r'"(.*)"')` 这个规则匹配的是第一个`"`到最后一个`"`
* 非贪婪模式:`str_pat = re.compile(r'"(.*?)"')` 这个规则匹配的是第一个`"`和接下来遇到的第一个 `"`

### 2.8 多行匹配模式
* `.`不能匹配换行符
* `?:`开头的分组为不捕获分组`r'(?:.|\n)'`，不占索引位置，仅仅用来做匹配，而不能通过单独捕获或group方法得到。
* 通过定义正则`r'(?:.|\n)'`增加了匹配多行的功能，可以将这个分组当作`.`来使用
* 标志参数`re.DOTALL`可以让正则表达式中的点`.`匹配包括换行符在内的任意字符。

### 2.9 将Unicode文本标准化

* 同一个字符可能有不同的编码方式，比如拼音，它可以是由整体组成或者是有字母+音标的方式组成，虽然显示上一致，但是两个字符是不相等的。
* 可以使用unicodedata模块先将文本标准化(转换为你希望的格式),例如`t1 = unicodedata.normalize('NFC', base_str)`
    * `normalize()` 第一个参数指定字符串标准化的方式。 `NFC`表示字符应该是整体组成(比如可能的话就使用单一编码)，而`NFD`表示字符应该分解为多个组合字符表示
* `unicodedata.combining(code)`可以判断字符code是否为和音字符，结合分解方式的标准化可以用于清洗数据。

### 2.11 删除字符串中不需要的字符

* `strip()` 方法能用于删除开始或结尾的字符。 `lstrip()` 和 `rstrip()` 分别从左和从右执行删除操作。
* `strip()` 方法默认删除包括换行符在内的空白字符，但是可以传入参数来删除其他字符，`strip('---')`

### 2.13 字符串对齐与格式化字符串
* 对于基本的字符串对齐操作，可以使用字符串的 `ljust()` , `rjust()` 和 `center()` 方法。 `'hello world'.center(20,'*')`
* `str.format()`方法比格式化文本的 % 操作符更强大,详见此文档[format格式化字符串方法](./format格式化字符串方法.md)

### 2.14 合并拼接字符串
* 如果你想要合并的字符串是在一个序列或者 iterable 中，那么最快的方式就是使用`join()`方法
* `+`合并字符串会创造临时变量，造成性能问题

### 2.15 字符串中插入变量
* `base.format(name='Guido', age=37)`是目前最好的插入变量解决办法
* 如果希望能将变量域中的参数直接传入字符串中，使用`base_str.format_map(vars())`即可

### 以指定列宽格式化字符串(用于控制台)

* 可以使用 textwrap 模块来格式化字符串的输出。`textwrap.fill(base_str, 70)`每行的输出字符宽为70
* 可以结合 `os.get_terminal_size()` 方法来获取终端的大小尺寸

### 在字符串中处理html和xml

* 你想将HTML或者XML实体如 `&entity;` 或 `&#code;` 替换为对应的文本或者转换文本中特定的字符(比如`<`, `>`, 或 `&`)，可以引入html模块
* `html.escape(base_str)`会将`<` 转换为 `&lt;`

### 字符串令牌解析
### 实现一个简单的递归下降分析器

## 第三章 数字日期和时间
## 第四章 迭代器与生成器

### 4.1手动遍历迭代器

* 对于一个`genrator object`,可以使用next(genertor)得到每一个结果，当越界后，程序会报`StopIteration`错误
* 我们可以使用`next(genertor,msg)`，第二个参数表示越界后返回的值来标记结尾。当传入第二个参数后，越界就不会报错了。

### 4.2 代理迭代

### 4.3 使用生成器创建新的迭代模式
* 一个函数中需要有一个 `yield` 语句即可将其转换为一个生成器。
* `yield`和`return`类似，每次被`next`调用时，会返回`yield`后面的变量值
* 我们通常使用for循环来调用一个迭代器，此时不用考虑越界等细节

### 4.4 实现迭代器协议
### 4.5 反向迭代一个序列

* 可以通过`reversed(list)`来得到list的反向迭代器

### 4.6  带有外部状态的生成器函数

* 如果生成器函数需要跟你的程序其他部分打交道的话，可以定义类，并把迭代器放到 `__iter__()` 方法中
* 如果该类生成的实例不使用for进行迭代的化，需要先调用`iter(object)`，才能进行迭代操作，否则会报错。

### 4.7 迭代器切片

* 函数 `itertools.islice(<generator>,start_num,end_num)` 正好适用于在迭代器和生成器上做切片操作
* `itertools.islice()`会消耗掉<generator>，因此只能使用一次
* 当`end_num`的值为`None`时，表示匹配的最后，当`start_num`的值为`None`时,表示从第一个开始匹配

### 4.8 跳过可迭代对象的开始部分

* itertools模块的dropwhile可以跳过符合规则的内容：`for line in dropwhile(lambda line: line.startswith('#'), f):`
* dropwhile它会返回一个迭代器对象，丢弃原有序列中直到函数**返回Flase之前**的所有元素，然后返回后面所有元素。
* lambda作用是构建匿名函数，其中，`:`前的表示传入的参数，后面的表示return的结构

### 4.9 排列组合的迭代

* `itertools.permutations(items,num)` 生成列表items内元素的所有排列组合(考虑顺序)
* `itertools.combinations(items,num)` 可得到输入集合中元素的所有的组合,不考虑顺序(1，2)和(2，1)算一个结果
* 更多的工具，可以在`itertools`中寻找

## 第五章:文件与IO
## 第六章:数字据编码与处理
## 第七章:函数
## 第八章:类与对象
## 第九章:元编程
## 第十章:模块与包
## 第十一章:网络与web编程
## 第十二章:并发编程
## 第十三章:脚本编程与系统管理

### 终止程序并给出错误信息

* `raise SystemExit('It failed!')`,它会将消息在 sys.stderr 中打印，然后程序以状态码1退出。

### 解析命令行选项

* argparse 模块可被用来解析命令行选项

### 创建和解压归档文件

* 解压: `shutil.unpack_archive('Python-3.3.0.tgz')`
* 压缩: `shutil.make_archive('new_file_name','zip','base_file_name')`
* 得到shutil支持的压缩类型: `shutil.get_archive_formats()`

### 运行时弹出密码输入提示

* `passwd = getpass.getpass()`主要是能够使用户在输入密码时不明文显示密码
* `user = getpass.getuser()`会根据该用户的shell环境来使用当前用户的登录名，如果希望弹出用户名输入提示，使用内置的 input 函数：`user = input('Enter your username: ')`

### 获取终端的大小

* 你需要知道当前终端的大小以便正确的格式化输出。可以使用 `size = os.get_terminal_size()` 函数来做到这一点
* 然后使用`size.columns`和`size.lines`来得到终端的行和列

### 实现一个计时器
* 通过计时器可以得到脚本运行的时间，文中给了个可以运行的计时器类用于计时

### 通过文件名查找文件

* `os.walk(basedir)`返回一个生成器对象,每次返回一个三元数组，分别是当前目录绝对路径字符串,当前目录下的文件夹名称列表，当前目录下的文件名称列表

### 启动一个WEB浏览器

* webbrowser模块可以快速的使用默认浏览器打开一个网页：`webbrowser.open('http://www.python.org')`

## 参考文档

[python3-cookbook](https://github.com/yidao620c/python3-cookbook)



