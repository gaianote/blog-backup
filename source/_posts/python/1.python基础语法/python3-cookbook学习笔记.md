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

* `namedtuple`的意义在于，直接通过下标index访问list中的数据，意义不清晰。namedtuple为常规的list增加了key值访问的方式。可以通过`namedtuple.key`和`namedtuple()[index]`两种方式读取nametuple中的值
* `collections.namedtuple()`工厂函数生成的实例可以将tuple转换为nametuple，并通过名称去访问元组元素，为代码增加可读性。
* `namedtuple()`跟元组类型是可交换的，支持所有的普通元组操作,和字典的区别主要在于命名元组是不可更改的
* 基本使用如下，`namedtuple()`是一个构造函数，其中，第一个参数是类的名称，第二个参数是key值列表；然后在新类中传入value值列表，即形成了新的nametuple

```python
from collections import namedtuple
Book = namedtuple('Book',['name','author','price'])
book1 = Book('空之境界','奈须蘑菇','100')
```
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

scanner.match是逐行匹配，匹配完第一行再匹配第二行。

#### 使用示例

1. 命名捕获组的正则表达式来定义所有可能的令牌，包括空格

```python
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
```
2. 实现一个生成器

```python
from collections import namedtuple
def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
```

3. 调用并处理token

```python
text = '''foo = 42
key = 100
'''

for tok in generate_tokens(master_pat, text):
    print(tok)
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')
# Token(type='WS', value='\n')
# Token(type='NAME', value='key')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='100')
# Token(type='WS', value='\n')
```

#### 要点:

1. 如果一个re匹配模式恰好是另一个更长模式的子字符串，那么你需要确定长模式写在前面。('|'.join的顺序)
2. scanner.match从字符串开头扫描到结尾，如果遇到不满足re匹配模式的地方立刻停止扫描，因此，需要考虑所有的情况，比如空白字符。

### 实现一个简单的递归下降分析器

## 第三章 数字日期和时间

### 数字的四舍五入
### 执行精确的浮点数运算
### 数字的格式化输出
### 二八十六进制整数
### 字节到大证书的打包与解包
### 复数的数学运算
### 无穷大与NaN
### 分数运算
### 大型数组运算
### 矩阵与线性代数运算
### 随机选择

random 模块有大量的函数用来产生随机数和随机选择元素。

比如，要想从一个序列中随机的抽取一个元素，可以使用 `random.choice()` ：

```
>>> import random
>>> values = [1, 2, 3, 4, 5, 6]
>>> random.choice(values)
```
为了提取出N个不同元素的样本用来做进一步的操作，可以使用 `random.sample()`

```
>>> random.sample(values, 2)
[6, 2]
>>> random.sample(values, 2)
[4, 3]
>>> random.sample(values, 3)
```

如果你仅仅只是想打乱序列中元素的顺序，可以使用 `random.shuffle()` ：

```
>>> random.shuffle(values)
>>> values
[2, 4, 6, 5, 3, 1]
```

生成随机整数，请使用 `random.randint()` ：

```
>>> random.randint(0,10)
2
>>> random.randint(0,10)
5
>>> random.randint(0,10)
0
```

为了生成0到1范围内均匀分布的浮点数，使用 `random.random()`：

```
>>> random.random()
0.9406677561675867
>>> random.random()
0.133129581343897
```

如果要获取N位随机位(二进制)的整数，使用 `random.getrandbits()` ：

```
>>> random.getrandbits(200)
335837000776573622800628485064121869519521710558559406913275
```

### 计算最后一个周五的日期
### 计算当前月份的日期范围
### 字符串转换为日期
### 结合时区的日期操作



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

### 5.1 读写文本数据

```python
# Read the entire file as a single string
with open('somefile.txt', 'a+',encoding = 'utf-8') as f:
    data = f.read()

# Iterate over the lines of the file
with open('somefile.txt', 'a+ ',encoding = 'utf-8') as f:
    for line in f:
        # process line
        ...
# 复杂情况可以使用readline()逐行读取；while line：保证到最后一行时会退出读取 '\n != EOF'
with open('somefile.txt', 'a+',encoding = 'utf-8') as f:
    line = fh.readline()
    while line:
        print(line.strip())
        line = f.readline()
```



* 换行符的识别问题(自动处理)
    * 在Unix和Windows中是不一样的(分别是 `\n` 和 `\r\n` )。
    * 在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 `\n` 字符。
    * 在输出时会将换行符 `\n` 转换为系统默认的换行符。
    * 二进制模式的时候，python不会自动转化

* `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)`
    * buffering的可取值有0，1， >1三个，0代表buffer关闭（只适用于二进制模式），1代表line buffer（只适用于文本模式），>1表示初始化的buffer大小；
    * encoding表示的是返回的数据采用何种编码，一般采用utf8或者gbk；
    * errors的取值一般有strict，ignore，当取strict的时候，字符编码出现问题的时候，会报错，当取ignore的时候，编码出现问题，程序会忽略而过，继续执行下面的程序。
    * newline可以取的值有None, \n,  \r, '', ‘\r\n' ，用于区分换行符，但是这个参数只对文本模式有效；
    * closefd的取值，是与传入的文件参数有关，默认情况下为True，传入的file参数为文件的文件名，取值为False的时候，file只能是文件描述符，什么是文件描述符，就是一个非负整数，在Unix内核的系统中，打开一个文件，便会返回一个文件描述符。

* open参数mode
    * mode参数决定了file的行为,如果在r模式下使用file.write(lines)就会报错
    * r、w、a为打开文件的基本模式，对应着只读、只写、追加模式；
    * b、t、+、U这四个字符，与以上的文件打开模式组合使用，二进制模式，文本模式，读写模式、通用换行符，根据实际情况组合使用、

* open常见的mode取值组合
    * r或rt    默认模式，文本模式读
    * rb      二进制文件
    * w或wt    文本模式写，打开前文件存储被清空
    * wb    二进制写，文件存储同样被清空
    * a   追加模式，只能写在文件末尾
    * a+  可读写模式，写只能写在文件末尾
    * w+ 可读写，与a+的区别是要清空文件内容
    * r+   可读写，与a+的区别是可以写到文件任何位置

**对照列表：**

| 模式 |                                                                                描述                                                                                |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。                                                                                                   |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。                                                                                       |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。                                                                                                                 |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。                                                                                                     |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。                                           |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。                               |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。                                             |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。                                 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。             |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。                                 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。                                             |

### 5.2 打印输出至文件中

* print接受关键字参数file，可以将输出重定向到一个文件中去,此时print的作用和f.write()相同
* 文件必须是文本文件，不能是二进制文件，否则会报错
* 重定向后print的内容不会在控制台输出

```python
with open('data.txt', 'w') as f:
    print("hello world!",file = f)
```
### 5.3 使用其它分隔符或行终止符打印

* print() 函数支持使用 `sep` 和 `end` 关键字参数，sep表示每个参数之间的分割符,end表示打印的结尾：`print('ACME', 50, 91.5, sep=',', end='!!\n')`

### 5.4 读写字节数据

* 读取或写入二进制数据需要使用模式为 `rb` 或 `wb` 的 `open()` 函数：`with open('somefile.bin', 'rb') as f:`
* 二进制数据索引和迭代动作返回的是字节的值而不是字节字符串

```python
>>> b = b'Hello World'
>>> b[0]
72
```
* 如果你想从二进制模式的文件中读取或写入**文本数据**，必须确保要进行解码(decode)和编码(encode)操作。

```python
with open('somefile.bin', 'rb') as f:
    data = f.read(16) # 二进制格式
    text = data.decode('utf-8') # 文本格式

with open('somefile.bin', 'wb') as f:
    text = 'Hello World' # 文本格式
    f.write(text.encode('utf-8')) # 二进制格式
```

### 5.5 文件不存在才能写入

* 可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题。文件存在时程序会报错：`with open('somefile', 'xt') as f:`

### 5.6 字符串的I/O操作

* 使用 `io.StringIO()` 和 `io.BytesIO()` 类来创建类文件对象操作字符串数据

### 5.11 文件路径名的操作

* 详见[python操作文件和目录](python操作文件和目录.md)

### 5.12 测试文件是否存在(os.path)

* 测试一个文件是否存在,返回布尔值
    * `os.path.exists('/etc/passwd')`

* 测试这个文件时什么类型的,返回布尔值
    * `os.path.isfile('/etc/passwd')`
    * `os.path.isdir('/etc/passwd')`
    * `os.path.islink('/usr/local/bin/python3')`
    * `os.path.realpath('/usr/local/bin/python3')`

* 获取元数据(比如文件大小或者是修改日期)

    * `os.path.getsize('/etc/passwd')`
    * `os.path.getmtime('/etc/passwd')`

### 5.13 获取文件夹中的文件列表

* 得到某种类型的文件
    * endswith进行匹配 `pyfiles = [name for name in os.listdir('somedir') if name.endswith('.py')]`
    * 引入glob模块进行匹配: `pyfiles = glob.glob('somedir/*.py')`

### 5.14 忽略文件名编码

```python
with open('jalape\xf1o.txt', 'w') as f:
     f.write('Spicy!')

import os
os.listdir('.')
['jalapeño.txt']

os.listdir(b'.')
[b'jalapen\xcc\x83o.txt']
```

### 5.19 创建临时文件和文件夹

* tempfile 模块中有很多的函数可以完成这任务。 为了创建一个匿名的临时文件，可以使用 tempfile.TemporaryFile

```python
from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
# Temporary file is destroyed
```
### 5.20 与串行端口的数据通信

* 你想通过串行端口读写数据，典型场景就是和一些硬件设备打交道(比如一个机器人或传感器)。
* 但对于串行通信最好的选择是使用 [pySerial](https://pythonhosted.org/pyserial/pyserial_api.html)包(第三方)

#### 安装serial

```
pip install pyserial
```
#### 列出端口

```bash
python -m serial.tools.list_ports将打印可用端口列表。也可以添加regexp作为第一个参数，列表将只包含匹配的条目。
```

或

```python
import serial.tools.list_ports

plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("没有发现端口!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName, 9600, timeout=60)
    print("可用端口名>>>", serialFd.name)
```

**注意**

枚举可能不适用于所有操作系统。它可能不完整，列出不可用的端口或可能缺少端口的详细描述。

#### 初始化Serial,其中支持的参数如下：

```
ser = serial.Serial(port = None，baudrate = 9600，bytesize = EIGHTBITS，parity = PARITY_NONE，stopbits = STOPBITS_ONE，timeout = None，xonxoff = False，rtscts = False，write_timeout = None，dsrdtr = False，inter_byte_timeout = None)
```

参数：

* `port` - 设备名称或无。
* `baudrate(int)` - 波特率，如9600或115200等。
* `bytesize` - 数据位数。可能的值： `FIVEBITS`，`SIXBITS`，`SEVENBITS`， `EIGHBITS`
* `parity` - 启用奇偶校验。可能的值： `PARITY_NONE`，`PARITY_EVEN`，`PARITY_ODD PARITY_MARK`，`PARITY_SPACE`
* `stopbits` - 停止位数。可能的值： `STOPBITS_ONE`，`STOPBITS_ONE_POINT_FIVE`， `STOPBITS_TWO`
* `timeout(float)` - 设置读取超时值。
* `xonxoff(bool)` - 启用软件流控制。
* `rtscts(bool)` - 启用硬件(RTS / CTS)流量控制。
* `dsrdtr(bool)` - 启用硬件(DSR / DTR)流控制。
* `write_timeout(float)` - 设置写超时值。
* `inter_byte_timeout(float)` - 字符间超时，无禁用(默认）。

#### 异常:

* `ValueError` - 当参数超出范围时将引发，例如波特率，数据位。
* `SerialException` - 如果找不到设备或无法配置设备。

#### 实例方法：

##### `ser.read(size=1)`

Parameters: size – 需要读取的字节数.
Returns: 从端口返回的字节
Return type: byte

从串行端口读取大小字节。如果设置了超时，则可以按要求返回较少的字符。在没有超时的情况下，它将被阻塞，直到读取请求的字节数为止。

#### `ser.readline()`

Returns: 从端口返回的字节
Return type: byte

从串口读取一行字节。如果设置了超时，则可以按要求返回较少的字符。在没有超时的情况下，它将被阻塞，直到读取请求的字节数为止。

##### `write(data)`

Parameters: data – 要发送的数据.
Returns: 写入的字节数
Return type: int

向端口写入字节数据,Unicode字符串必须被编码,例如`ser.write('hello'.encode('utf-8'))`



### 5.21 序列化Python对象

* 所谓序列化是指Python对象(字典，数组)以特定格式转换为一个字节流，以便将它保存到一个文件用于日后读写。
* 对于序列化最普遍的做法就是使用`pickle`模块，它可以将对象等转换为字节编码储存在文档中，但只有python支持，因此不推荐
* 你最好使用更加标准的数据编码格式如XML，CSV或JSON来存储或是序列化数据

## 第六章:数字据编码与处理

### 6.1 读写CSV数据
* 对于大多数的CSV格式的数据读写问题，都可以使用 csv 库，而无需自己处理分隔符以及其它细节。
* csv的默认分隔符是','，可以使用delimiter参数进行指定
* 将这些数据读取为一个元组的序列:

```python
import csv
with open('stocks.csv') as f:
    f_csv = csv.reader(f,delimiter=',')
    headers = next(f_csv) # 通常第一行是headers，通过next得到lsit
    for row in f_csv:
        # row is list
```
* 可以使用`csv.DictReader(file)`和`csv.DictWriter(file, headerlist)`方便的以字典的形式读取或写入

### 6.2 读写JSON数据

* python对象与JSON字符串互相转换,可以使用`json.dumps()` 和 `json.loads()`

```python
import json
json_str = json.dumps(data)
data = json.loads(json_str)
```
* 如果你要处理的是文件而不是字符串，你可以使用 `json.dump(data,file)` 和 `json.load(file)` 来编码和解码JSON数据
* json.dump()在序列化的同时写入了文件。 等价于`data = json.dumps(data) file.write(data)`

```python
# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
```

* 可以使用`object_pairs_hook`或`object_hook`参数对传入的`json_str`进行处理,从而得到所需的数据类型

```python
data = json.loads(json_str, object_pairs_hook=OrderedDict)
```

### 读写ymal格式的文件

对于读取yaml文件，我们可以使用pyymal第三方模块，而无需自己编写语法解析规则

首先安装pyyaml

```
pip install pyyaml
```

然后读取并解析yaml

```python
import yaml

with open(file_path,'r',encoding = "utf-8") as file:
    dic = yaml.load(file).get(key)
```
###6.8 与关系型数据库的交互

* 你可以使用Python标准库中的 sqlite3 模块
* 不要使用Python字符串格式化操作符(如%)或者 .format() 方法来创建这样的字符串。否则很有可能遭受SQL注入攻击。
* 与sqlite3交互步骤
    1. 链接数据库,得到数据库实例 `db = sqlite3.connect('database.db')`
    2. 创建游标 `cursor = db.cursor()`
    3. 执行语句`cursor.execute('create table portfolio (symbol text, shares integer, price real)')`
    4. 提交语句`db.commit()`

### 6.10 编码解码Base64数据

* Base64编码仅仅用于面向字节的数据比如字节字符串和字节数组。
* 编码为base64:base64.b64encode( data)
* 解码为二进制字节:base64.b64decode(base64data)


```python
# Some byte data
s = b'hello'
import base64
# Encode as Base64
a = base64.b64encode(s) # b'aGVsbG8='
# Decode from Base64
base64.b64decode(a) # b'hello'
```

### 6.13 数据的累加与统计操作

* 于任何涉及到统计、时间序列以及其他相关技术的数据分析问题，都可以考虑使用Pandas库 。


## 第七章:函数

### 7.1 可接受任意数量参数的函数

* 为了能让一个函数接受任意数量的位置参数，可以使用一个以`*`开头的参数,这个参数是个tuple
* 为了接受任意数量的关键字参数，使用一个以`**`开头的参数,这个参数是个dict
* 一个`*`参数只能出现在函数定义中最后一个位置参数后面，而 `**`参数只能出现在最后一个参数。
* 有一点要注意的是，在`*`参数后面仍然可以定义其他参数。这种参数就是我们所说的强制关键字参数

### 7.2 只接受关键字参数的函数

* 将强制关键字参数放到某个`*`位置参数或者单个`*`后面就能达到强制使用关键字参数传递
* 如果你还希望某个函数能同时接受任意数量的位置参数和关键字参数，可以同时使用*和**

```python
def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict
```
### 7.3 给函数参数增加元信息

* 函数的注解方法`def add(x:int, y:int) -> int:`
* 注解和注释类似,python解释器不会对这些注解添加任何的语义,他们仅用于提示作用
* 函数注解只存储在函数的 `__annotations__` 属性中,`add.__annotations__`

### 7.4 返回多个值的函数

* `return a,b,c`返回的是一个元组
* 我们使用的是逗号来生成一个元组，而不是用括号 `b = 1,2,3 => b == (1,2,3)`

### 7.5 定义有默认参数的函数

* 测试默认参数`None`时不能使用:`if not b:`而要使用`if b is None:`以排除`0`,`''`等
* 默认参数的值仅仅在函数定义的时候赋值一次,比如将变量作为参数传入进去，实际传入的是变量的值的拷贝

### 7.6 定义匿名或内联函数

* lambda x, y: x + y lambda 定义一个匿名函数，`:`之前是函数的参数`:`之后是函数返回的值

```python
add = lambda x, y: x + y
add(2,3)
```
* lambda表达式中的x是一个自由变量， 在运行时绑定值，而不是定义时就绑定
* 如果需要在定义时确认值，只需给相应的参数提供默认值即可:`[lambda x, n=n: x+n for n in range(5)]`

* `[lambda x, n=n: x+n for n in range(5)]`解析：
    * 生成器表达式：`for n in range(5)`生成包含5个匿名函数的列表列表 lambda x,n=n:x+n
    * `lambda x, n=n: x+n`,由于n有默认值，所以在定义时确定n值，n值分别为0,1,2,3,4
    * 列表结果为(相似)：[lambda x: x+0,lambda x: x+1,lambda x: x+2,lambda x: x+3,lambda x: x+4]
    * 如果n没有默认值,则n=4,即迭代的最后一个值

### 7.8 减少可调用对象的参数个数

* `new_func = partial(func,*params)` 给一个或多个参数设置固定的值，减少接下来被调用时的参数个数。
* `partial(func,*params)`的意义是在调用其它函数库接受的回调函数时用来微调参数个数。
* 很多时候 `partial()` 能实现的效果，lambda表达式也能实现,但是稍显臃肿
* `list_obj.sort(key=partial(distance,pt))`
* 列表的 `list_obj.sort()` 方法
    * 接受一个回调函数`key = func()`的返回值作为新的列表排序依据， 但是它只能接受一个单个参数的函数，参数是列表的每个子元素

### 7.9 将单方法的类转换为函数

* 通常是为了保存额外状态来给函数使用，详见7.10

### 7.10 带额外状态信息的回调函数

* 有三种方式可以在回调函数的内部保存变量值
    * 创建一个类，使需要保存的变量在类内部传递。回调函数是有对象实例化的一个方法。
    * 创建一个闭包，使需要保存的变量在函数内部传递。回调函数是这个函数return的闭包。需要为变量声明nonlocal
    * 创建一个协程，使需要保存的变量在协程内部传递。回调函数是这个协程启动的send方法。

```python
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def add(x, y):
    return x + y

# 创建一个类保存变量
class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))
r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)

# 创建一个闭包保存变量
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)


# 创建一个协程保存变量
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler()
next(handler) # Advance to the yield
apply_async(add, (2, 3), callback=handler.send)
```

* 协程解析
    * 协程通过yield关键字实现,他实际上是个generator
    * 对于协程,第一次必须运行一次next(generator)启动它(进入到while True中,这才是协程运行的部分)，直接使用send方法会报错
    * 协程 `param = yield result`对于yield来说,`=`并不是赋值的意思。等号前的值generator通过send方法传入的参数，使其内部读取,yield后的值是其返回给外界的值
    * generator每次执行后，遇到yield就会中断执行，直到使用`next(generator)`或`generator.send(param)`再次调用它，才会继续执行。



## 第八章:类与对象

### 8.1 改变对象的字符串显示

* `__repr__()` 方法返回一个实例的代码表示形式，通常用来重新构造这个实例。 内置的 repr() 函数返回这个字符串，跟我们使用交互式解释器显示的值是一样的。
* `__str__()` 方法将实例转换为一个字符串，使用 `str()` 或 `print()` 函数会输出这个字符串。
* 为了更方便的调试代码，我们可以自定义类的 `__repr__()` 和 `__str__()`方法

### 8.3 让对象支持上下文管理协议

* 为了让一个对象兼容 with 语句，你需要实现 `__enter__()` 和 `__exit__()` 方法

```python
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None
```
### 8.5 在类中封装属性名(私有属性)

* 第一个约定是任何以单下划线_开头的名字都应该是内部实现(私有属性或方法)。
* Python并不会真的阻止别人访问内部名称,但是应该尽量去避免调用内部方法
* 双下划线__开头的属性或方法通过继承是无法被覆盖或者修改
* 有时候你定义的一个变量和某个保留关键字冲突，这时候可以使用单下划线作为后缀:`lambda_ = 2.0`
* 大多数而言，你应该让你的非公共名称以单下划线开头。但是，如果你清楚你的代码会涉及到子类， 并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线方案。

### 8.6 创建可管理的属性

* 你想给某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证。

```python
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")
```

### 8.25 创建缓存实例

* 在创建一个类的对象时，如果之前使用同样参数创建过这个对象， 你想返回它的缓存引用
* 详细实现请见9.13小节

### 8.9 创建新的类或实例属性(描述器)

* 定义描述器`__get__` `__set__` `__delete__`三种方法在类中
* 为了使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中:`x = Integer('x')`
* 描述器可实现大部分Python类特性中的底层魔法， 包括 @classmethod 、@staticmethod 、@property

## 第九章:元编程

* 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
* metaclass用来控制类的创建行为。当我们在类中传入关键字参数metaclass时，魔术就生效了。
* metaclass可以隐式地继承到子类，但子类自己却感觉不到。

### 9.1 在函数上添加装饰器

* 装饰器的用途是为函数增加额外功能而不影响代码的整体结构的一种方法，而@function是装饰器的语法糖
* 定义一个装饰器

```python
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper
```

* 使用装饰器

```python
@timethis
def countdown(n):
    while n > 0:
        n -= 1

>>> countdown(100000)
countdown 0.008917808532714844
>>> countdown(10000000)
countdown 0.87188299392912
```

### 9.2 创建装饰器时保留函数元信息


* 任何时候你定义装饰器的时候，都应该使用 `functools` 库中的 `@wraps` 装饰器来注解底层包装函数。

### 9.3 解除一个装饰器

* 解除一个装饰器是指:一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函数
* 假设装饰器是通过 @wraps (参考9.2小节)来实现的，那么你可以通过访问 `__wrapped__` 属性来访问原始函数：`orig_func = new_func.__wrapped__`
* 并不是所有的装饰器都使用了 @wraps ，因此这里的方案并不全部适用

### 9.4 定义一个带参数的装饰器

* 装饰器是可以使用参数的，关键点是包装器是可以使用传递给最外层的参数的
* 带参数的装饰器分为三层，最外层为装饰器名称以及参数:`def logged(level, name=None, message=None):`，中层为`def decorate(func):`,内层为`@wraps(func)`

### 9.5 可自定义属性的装饰器

* 你想写一个装饰器来包装一个函数，并且允许用户提供参数在运行时控制装饰器行为

### 9.6 带可选参数的装饰器

* 带可选参数的装饰器是指:你想写一个装饰器，既可以不传参数给它，比如 `@decorator` ，也可以传递可选参数给它，比如 `@decorator(x,y,z)`
* 主要实现装饰器带或者不带括号都可以正常工作，实现编程一致性
* 带参数与不带参数的装饰器区别是：初始化时，orig_func是否被传入
    * `new_func = logged(orig_func)`
    * `new_func = logged(level=logging.CRITICAL, name='example')(orig_func)`
* 实现原理:
    * 如果装饰器无参数，会传入`func`，跳过if语句内的`partial`方法,直接将orig_func传入
    * 如果装饰器有参数，初始化时func为None，执行`partial`方法，导入其它参数并返回一个未完全初始化的自身，以确定除了`orig_func`之外其它参数。此时等价于无参装饰器。继续初始化执行`new_func = logged(orig_func)`

### 9.7 利用装饰器强制函数上的类型检查

* `inspect.signature(func)` 函数，它可以得到func函数的参数：

```python
from inspect import signature
def func(x, y, z=42):
    pass
sig = signature(func)
sig # (x, y, z=42)
sig.parameters # mappingproxy(OrderedDict([('x', <Parameter at 0x10077a050 'x'>),('y', <Parameter at 0x10077a158 'y'>), ('z', <Parameter at 0x10077a1b0 'z'>)]))
sig.parameters['z'].name # 'z'
sig.parameters['z'].default # 42
sig.parameters['z'].kind # <_ParameterKind: 'POSITIONAL_OR_KEYWORD'>
```
* sig.bind()方法
    * `sig.bind(int, 2, 3).arguments`返回一个有序字典`OrderedDict([('x', int), ('y', 2), ('z', 3)])`,key值是被绑定的函数参数值,value是你指定的数据类型或者其他值。
    * `sig.bind_partial(int,z=int)`允许忽略一部分参数，而`sig.bind`方法不允许

* 核心原理：
    1. 使用`sig.bind_partial(*ty_args, **ty_kwargs).arguments`使`bound_types`指定根据装饰器参数形成一个有序字典，指定函数类型
    2. 使用`sig.bind(*args, **kwargs)arguments`方法使`bound_values`根据函数传入的值形成一个有序字典，为调用函数时传入的值
    3. 通过对比做出判断，然而这种方法不能判断出默认参数(内部转换)是否符合要求，由于可变对象[]不应作为参数，所以默认参数需做判断:`if x == None：x = []`

### 9.10 为类和静态方法提供装饰器

* 为类的方法提供装饰器和为函数添加装饰器定义与使用方法是一致的
* 如果类中方法存在装饰器  `@classmethod` 和 `@staticmethod` ，要把他们放在最上面，否则会报错
* 如果希望装饰器访问类的属性，需做如下修改：
    1. 在wrapper传入参数self
    2. 类方法`origin_func(self, *args, **kwargs)`传入参数self

```python
def catch_exception(origin_func):
    def wrapper(self, *args, **kwargs):
        try:
            u = origin_func(self, *args, **kwargs)
            return u
        except Exception:
            self.revive() #不用顾虑，直接调用原来的类的方法
            return 'an Exception raised.'
    return wrapper
class Test(object):
    def __init__(self):
        pass
    def revive(self):
        print('revive from exception.')
        # do something to restore
    @catch_exception
    def read_value(self):
        print('here I will do something.')
        # do something.
```

### 9.13 使用元类控制实例的创建

* 一个类可以在`__init_`中规定它的创建方式。
* 我们希望通过**创建元类**改变实例创建方式来实现单例、缓存或其他类似的特性。
* 我们可以通过定义元类中的 `__call__()` 方法规定类的创建方式。并在创建类时通过`metaclass`关键字参数确定创建方式:`class Spam(metaclass=NoInstances):...`


* 定义只能创建唯一的实例的元类Singleton

```python
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

# Example
class Spam(metaclass=Singleton):
    def __init__(self):

        print('Creating Spam')
```
* 详细解析
    * 元类Singleton(type)需要传入父类type(元类定义皆为如此)
    * 元类中`def __call__`方法定义了类实例化时的行为
    * Singleton在Spam定义(解释器扫描到`metaclass=Singleton`)时被初始化，此时`self.__instance = None`
    * 当Spam第一次实例化时，`self.__instance == None`返回`super().__call__(*args, **kwargs)`,即Spam的实例
    * 当Spam第二次实例化时，由于`self.__instance`等于Spam第一次返回的实例，这个值直接被返回了。
    * 注意的是,当Spam第二次实例化时,由于`super().__call__`方法根本没有执行，所以他的`__init__`方法也不会被调用了
    * 由此便实现了只能初始化一次的元类方法

### 9.21 避免重复的属性方法

* 本节展示了对类进行类型检查的三种方式，并逐步简化的过程

### 9.22 定义上下文管理器的简单方法(with)

* with的基本概念
    * with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作。
    * 有了上下文管理器，with 语句才能工作。
    * 上下文管理器（Context Manager）：支持上下文管理协议的对象，这种对象实现了`__enter__()` 和 `__exit__()` 方法。
    * 语句体（with-body）：with 语句包裹起来的代码块，在执行语句体之前会调用上下文管理器的 `__enter__()` 方法，执行完语句体之后会执行 `__exit__()` 方法。
    * with语句遇到错误也会抛出异常，区别是它在遇到异常后仍可以执行清理操作。
* 通常情况下，如果要写一个上下文管理器，你需要定义一个类，里面包含一个 `__enter__()` 和一个`__exit__()` 方法
* 更好的方法是使用`contexlib` 模块中的 `@contextmanager` 装饰器
* `@contextmanager`使用方法
    * yield 之前的代码会在上下文管理器中作为 `__enter__()` 方法执行，
    * yield 之后的代码会作为 `__exit__()` 方法执行。
    * yield 后如果含有值，会返回as后面的内容，类似于return
    * 如果希望执行`__exit__()`方法,就在yield前加`try:`,yield后加`finally`;否则不执行清理操作

### 9.23 在局部变量域中执行代码(exec)

* `exec('func_str')`在全局作用域中可以获取并改变全局作用域中的变量
* `exec('func_str')`在局部作用域中无法改变局部变量或全局变量的值，它获得的时变量的字典拷贝。
* 希望获得`exec('func_str')`在局部作用域中的运行结果，可以在`exec`之前使用`locals_dic = locals()`获得局部变量字典，这个字典的值是exec真正改变的值
* 每次调用`locals()` 会获取局部变量值中的值并覆盖字典中相应的变量。如果在`exec`之后调用`locals()`将无法获得正确结果

```python
# exec在局部作用域中无法改变局部变量或全局变量的值
a = 10
def exec_test():
    locals_dic = locals()
    exec("a += 1")
    print('exec:',locals_dic['a'],'glabal:',a)

exec_test() # exec: 11 glabal: 10
```

### 9.25 拆解Python字节码

## 第十章:模块与包

### 10.1 构建一个模块的层级包

* 一个文件夹内如果存在`__init__.py`,这个文件夹就成为了一个包
* 大部分情况下`__init__.py`文件为空即可
* 如果在子包的`__init__.py`中写入`from . import jpg`父模块便可以自动加载子模块jpg.py了
    * 自动加载是指对于lib/jpg.py：`import lib` 之后,直接使用`lib.jpg`即可
    * 否则需要`from lib import jpg`之后才能使用`lib.jpg`
* 直接使用文件夹内的函数

### 10.2 控制模块被全部导入的内容

* 强烈反对使用 `from module import *`
* 如果你不做任何事, 这样的导入将会导入所有不以下划线开头的。
* 如果在模块中定义了 `__all__` , 那么只有被列举出的东西会被导出:`__all__ = ['spam', 'grok']`

### 10.3 使用相对路径名导入包中子模块

文件结构如下

```
mypackage/
  |-__init__.py
  |-A/
    |-__init__.py
    |-spam.py
    |-grok.py
  |-B/
    |-__init__.py
    |-bar.py
```
在spam中引入grok和bar,只需如此操作：

```python
from . import grok
from ..B import bar
```

### 10.4 将模块分割成多个文件
### 10.5 利用命名空间导入目录分散的代码

* 不同的目录有着相同的模块名称,希望将同名模块统一成唯一的模块直接引入
* 前提是在任何一个目录里都没有`__init__.py`文件。

```python
import sys
sys.path.extend(['foo-package', 'bar-package'])
import spam.blah
import spam.grok
```

### 10.6 重新加载模块
### 10.7 运行目录或压缩文件

* 如果`__main__.py`存在于顶层目录，你可以简单地在顶级目录运行这个文件: `python dirname`

### 10.8 读取位于包中的数据文件

* 可以使用pkgutil.get_data来读取包中的文件
* 在包中尽量不使用I/O操作,1是I/O操作需要使用绝对文件名;二是包通常安装作为.zip或.egg文件,open方法此时不会工作

```python
import pkgutil
data = pkgutil.get_data(__package__, 'somedata.dat')
```

### 10.9 将文件夹加入到sys.path
### 10.10 通过字符串名导入模块

* 你想导入一个模块，但是模块的名字在字符串里。你想对字符串调用导入命令。

```python
import importlib
math = importlib.import_module('math')
```
### 10.11 通过钩子远程加载模块
### 10.12 导入模块的同时修改模块
### 10.13 安装私有的包

* Python有一个用户安装目录，通常类似”~/.local/lib/python3.3/site-packages”。 要强制在这个目录中安装包，可使用安装选项“–user”

```bash
python3 setup.py install --user
# or
pip install --user packagename
```

* 通常包会被安装到系统的site-packages目录中去
    * 路径类似“/usr/local/lib/python3.3/site-packages”。
    * 不过，这样做需要有管理员权限并且使用sudo命令。
    * 就算你有这样的权限去执行命令，使用sudo去安装一个新的，可能没有被验证过的包有时候也不安全。
    * 安装包到用户目录中通常是一个有效的方案，它允许你创建一个自定义安装。

### 10.14 创建新的Python环境
### 10.15 分发包

`install_requires`:指定了在安装这个包的过程中, 需要哪些其他包。 如果条件不满足, 则会自动安装依赖的库。

```python
setup(install_requires=["requests"]) # example1
setup(install_requires=["numpy >= 1.8.1", "pandas >= 0.14.1"]) # example2
```
[python核心 - 打包与发布](https://www.xncoding.com/2015/10/26/python/setuptools.html)

## 第十一章:网络与web编程

### 11.1 作为客户端与HTTP服务交互

对于真的很简单HTTP客户端代码，用内置的 urllib 模块通常就足够了。但是，如果你要做的不仅仅只是简单的GET或POST请求，那就真的不能再依赖它的功能了。这时候就是第三方模块比如 `requests` 大显身手的时候了。

## 第十二章:并发编程

Python是运行在解释器中的语言，查找资料知道，python中有一个全局锁（GIL），在使用多线程Thread)的情况下，不能发挥多核的优势。而使用多进程(Multiprocess)，则可以发挥多核的优势真正地提高效率

[一个实验对比](https://segmentfault.com/a/1190000007495352)

|      操作类型      |  CPU密集型操作 |  IO密集型操作  | 网络请求密集型操作 |
|------------|----------------|----------------|--------------------|
| 线性操作   | 94.91824996469 | 22.46199995279 |       7.3296000004 |
| 多线程操作 | 101.1700000762 |  24.8605000973 |       0.5053332647 |
| 多进程操作 |  53.8899999857 |  12.7840000391 |       0.5045000315 |


* 多线程在IO密集型的操作下似乎也没有很大的优势（也许IO操作的任务再繁重一些就能体现出优势），在CPU密集型的操作下明显地比单线程线性执行性能更差，但是对于网络请求这种忙等阻塞线程的操作，多线程的优势便非常显著了

* 多进程无论是在CPU密集型还是IO密集型以及网络请求密集型（经常发生线程阻塞的操作）中，都能体现出性能的优势。不过在类似网络请求密集型的操作上，与多线程相差无几，但却更占用CPU等资源，所以对于这种情况下，我们可以选择多线程来执行

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



