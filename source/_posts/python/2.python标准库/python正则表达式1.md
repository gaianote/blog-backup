---
title: python正则表达式
date: 2018-06-12 14:08:39
tags: python 终稿
---

正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。

<!-- more -->


## 1. re模块的基本使用

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
>>> import re
>>> re.compile('^one').search('one1two2three3four4').group()
one
```

## 2. re.compile(pattern[, flags])

compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供、`match()` 和 `search()` 等函数使用。

参数：

* `pattern` : 一个字符串形式的正则表达式
* `flags` 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
  
    - `re.I` 忽略大小写
    - `re.L` 表示特殊字符集 `\w`, `\W`, `\b`, `\B`, `\s`, `\S` 依赖于当前环境
    - `re.M` 多行模式
    - `re.S` 即为` . `并且包括换行符在内的任意字符（` . `不包括换行符）
    - `re.U` 表示特殊字符集 `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, `\S` 依赖于 Unicode 字符属性数据库
    - `re.X` 为了增加可读性，忽略空格和' # '后面的注释
    
    



## 3. re模块方法



### 1. 字符串搜索



#### 1.1 `re.compile(pattern[, flags]).match(string)`

`re.match` 尝试**从字符串的起始位置**匹配一个模式，如果不是起始位置匹配成功的话，`match()`就返回`none`。



| 匹配对象方法   | 描述                                                         |
| :------------- | :----------------------------------------------------------- |
| `group(num=0)` | 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。 |
| `groups()`     | 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。     |
| `span()`       | 返回匹配项所在的起始与终止位置，例如(0，3）表示从0位开始，长度为3 |

```python
import re
 
line = "Cats are smarter than dogs"
matchObj = re.compile( r'(.*) are (.*?) .*',re.M|re.I).match(line)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
   
# OUTPUT
matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
```


#### 1.2 `re.compile(pattern[, flags]).search(string)`

re.search 扫描整个字符串并返回第一个成功的匹配,如果没有匹配项就返回None。


**实例**
```python
import re   
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配 print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
# OUTPUT
(0, 3)
(11, 14)
```



###  2.检索和替换

Python 的re模块提供了`re.sub`用于替换字符串中的匹配项。

语法：

```python
re.compile(pattern[, flags]).sub(repl, string, count=0)
```

参数：

- repl : 替换的字符串，也可为一个函数。
- string : 要被查找替换的原始字符串。
- count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。


## 实例

```python
import re   
phone = "2004-959-559 # 这是一个电话号码"   
# 删除注释 
num = re.compile(r'#.*$').sub("", phone) 
print ("电话号码 : ", num)   
# 移除非数字的内容 
num = re.compile(r'\D').sub("", phone) 
print ("电话号码 : ", num)

# OUTPUT
电话号码 :  2004-959-559 
电话号码 :  2004959559
```

repl 参数是一个函数时，可以接受匹配的结果作为参数，进行操作，返回新的替换值

以下实例中将字符串中的匹配的数字乘于 2：


```python
import re   
# 将匹配的数字乘于 2 
def double(matched):     
  value = int(matched.group('value'))
  return str(value * 2)   
s = 'A23G4HFD567' 
print(re.compile('(?P<value>\d+)').sub( double, s))

# OUTPUT
A46G8HFD1134
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

## 贪婪模式与非贪婪模式

### 贪婪模式：(.*)
* 如果没有限制(匹配分组后面接字符),贪婪模式会匹配到字符串的末尾
* 如果有限制,贪婪模式会匹配到最后一个符合要求的字符

### 非贪婪模式(.*?)

* 如果没有限制,非贪婪模式不匹配任何内容 re.compile().search('hello world')
* 如果有限制,贪婪模式会匹配到第一个符合要求的字符

由于两种模式的区别,正确的使用匹配模式非常重要，示例如下:

```python
import re
site = 'https://www.google.com'
result_a = re.compile(r'(.*?):(.*)').search(site).group()
result_b = re.compile(r'(.*?):(.*?)').search(site).group()
print('贪婪:{0}\n非贪婪:{1}'.format(result_a,result_b))
# 贪婪:https://www.google.com
# 非贪婪:https:
```
## 正则表达式模式

模式字符串使用特殊的语法来表示一个正则表达式：

字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。

多数字母和数字前加一个反斜杠时会拥有不同的含义。

标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。

反斜杠本身需要使用反斜杠转义。

由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。

下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。


![img](/images/2018070501.png)

## 参考资料
[菜鸟教程](http://www.runoob.com/python3/python3-reg-expressions.html)
```