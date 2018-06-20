---
title: python正则表达式
date: 2018-06-12 14:08:39
tags: python
---

## re模块的基本使用

python正则表达式整体来讲只需两步即可使用：

```python
import re
# 1.获得pattern对象，pattern = re.compile('正则表达式')
pattern = re.compile('^one')
# 2.使用re方法获得所需内容
pattern.search('one1two2three3four4')
```

实际使用过程中,直接链式调用即可

```python
re.compile('^one').search('one1two2three3four4')
```

### re.compile(pattern[, flags])

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

参数：

* pattern : 一个字符串形式的正则表达式
* flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
    - re.I 忽略大小写
    - re.L 表示特殊字符集 `\w`, `\W`, `\b`, `\B`, `\s`, `\S` 依赖于当前环境
    - re.M 多行模式
    - re.S 即为` . `并且包括换行符在内的任意字符（` . `不包括换行符）
    - re.U 表示特殊字符集 `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, `\S` 依赖于 Unicode 字符属性数据库
    - re.X 为了增加可读性，忽略空格和' # '后面的注释

## re模块方法

### 字符串替换 re.sub(pattern, repl, string, count=0)

将源字符串(`source_string`)符合匹配规则的字符(`pattern`),替换为新字符(`new_str`)

```python
# 第二个参数：替换后的字符串 第三个参数：字符串 count：替换个数,默认为0，表示每个匹配项都替换
pattern.sub(new_str,source_string,count = 0)
```

### re.match与re.search

* `re.search` 扫描整个字符串并返回第一个成功的匹配。匹配成功re.search方法返回一个匹配的对象，否则返回None。
* `re.match` 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

```python
>>> import re
>>> print(re.match('www', 'www.runoob.com')) # 返回Match Object
<_sre.SRE_Match object; span=(0, 3), match='www'>
>>> print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
(0, 3)
>>> print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
None
```

### findall(string[, pos[, endpos]])

在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。

**参数：**

* string 待匹配的字符串。
* pos 可选参数，指定字符串的起始位置，默认为 0。
* endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。

**示例：查找字符串中的所有数字：**

```python
import re

pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)
输出结果：

['123', '456']
['88', '12']
```

**区别：**

match 和 search 是匹配一次 findall 匹配所有。match 和 search 返回的是ReObject，findall返回的是包含匹配字符串的数组

## ReObject对象方法

### REObject.span()

span()方法可以得到匹配结果在字符串中的初始和结尾序号


### REObject.group(num= 0)

* `group(num= 0)` 返回匹配到的字符串
* `groups()` 返回包含所有匹配到的字符串的元组(puple)

```python
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
```

以上实例执行结果如下：

```python
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
```

group()方法可以得到匹配到的字符串，其中group()或group(0)表示整个compile(实例中为`(.*) are (.*?) .*`)匹配到的字符串，group(1)表示第一个()内的正则匹配到的字符串


## 正则表达式模式

模式字符串使用特殊的语法来表示一个正则表达式：

字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。

多数字母和数字前加一个反斜杠时会拥有不同的含义。

标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。

反斜杠本身需要使用反斜杠转义。

由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。

下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。

|     模式     |                                                                                    描述                                                                                   |   |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| ^            | 匹配字符串的开头                                                                                                                                                          |   |
| $            | 匹配字符串的末尾。                                                                                                                                                        |   |
| .            | 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。                                                                                       |   |
| [...]        | 用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'                                                                                                                       |   |
| [^...]       | 不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。                                                                                                                          |   |
| re*          | 匹配0个或多个的表达式。                                                                                                                                                   |   |
| re+          | 匹配1个或多个的表达式。                                                                                                                                                   |   |
| re?          | 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式                                                                                                                      |   |
| re{ n}       | 匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。                                                                                          |   |
| re{ n,}      | 精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。                                            |   |
| re{ n, m}    | 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式                                                                                                                      |   |
| a&#124;b     | 匹配a或b                                                                                                                                                                  |   |
| (re)         | G匹配括号内的表达式，也表示一个组                                                                                                                                         |   |
| (?imx)       | 正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。                                                                                                             |   |
| (?-imx)      | 正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。                                                                                                                  |   |
| (?: re)      | 类似 (...), 但是不表示一个组                                                                                                                                              |   |
| (?imx: re)   | 在括号中使用i, m, 或 x 可选标志                                                                                                                                           |   |
| (?-imx: re)  | 在括号中不使用i, m, 或 x 可选标志                                                                                                                                         |   |
| (?#...)      | 注释.                                                                                                                                                                     |   |
| (?= re)      | 前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。 |   |
| (?! re)      | 前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。                                                                                            |   |
| (?> re)      | 匹配的独立模式，省去回溯。                                                                                                                                                |   |
| \w           | 匹配数字字母下划线                                                                                                                                                        |   |
| \W           | 匹配非数字字母下划线                                                                                                                                                      |   |
| \s           | 匹配任意空白字符，等价于 [\t\n\r\f]。                                                                                                                                     |   |
| \S           | 匹配任意非空字符                                                                                                                                                          |   |
| \d           | 匹配任意数字，等价于 [0-9]。                                                                                                                                              |   |
| \D           | 匹配任意非数字                                                                                                                                                            |   |
| \A           | 匹配字符串开始                                                                                                                                                            |   |
| \Z           | 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。                                                                                                              |   |
| \z           | 匹配字符串结束                                                                                                                                                            |   |
| \G           | 匹配最后匹配完成的位置。                                                                                                                                                  |   |
| \b           | 匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。                                                      |   |
| \B           | 匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。                                                                                            |   |
| \n, \t, 等。 | 匹配一个换行符。匹配一个制表符, 等                                                                                                                                        |   |
| \1...\9      | 匹配第n个分组的内容。                                                                                                                                                     |   |
| \10          | 匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。                                                                                                       |   |

## 参考资料
[菜鸟教程](http://www.runoob.com/python3/python3-reg-expressions.html)