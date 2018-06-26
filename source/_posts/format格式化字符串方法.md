---
title: format格式化字符串方法
date: 2018-06-22 13:50:57
tags: python
---

## 使用说明

`base_str.format(new_word)` 要比 `%`字符串操作符的功能更为强大。

在字符串中使用`{NUM}`进行占位,0表示第一个参数,1表示第二个参数。使用`:`, 指定代表元素需要的操作, 如`{0:.3}`小数点三位, `{1:8}`占8个字符空间等;

`:`后可以添加特定的字母, 表示特定的输出格式:

|    操作    |                                             说明                                            |
|------------|---------------------------------------------------------------------------------------------|
| `{0:b}`    | 二进制. 将数字以2为基数进行输出.                                                            |
| `{0:c}`    | 字符. 在打印之前将整数转换成对应的Unicode字符串.                                            |
| `{0:d}`    | 十进制整数. 将数字以10为基数进行输出.                                                       |
| `{0:o}`    | 八进制. 将数字以8为基数进行输出.                                                            |
| `{0:x}`    | 十六进制. 将数字以16为基数进行输出, 9以上的位数用小写字母.                                  |
| `{0:e}`   | 幂符号. 用科学计数法打印数字, 用`e`表示幂.                                                  |
| `{0:g}`    | 一般格式. 将数值以fixed-point格式输出. 当数值特别大的时候, 用幂形式打印.                    |
| `{0:n}`    | 数字. 当值为整数时和`d`相同, 值为浮点数时和`g`相同. 不同的是它会根据区域设置插入数字分隔符. |
| `{0:%}`    | 百分数. 将数值乘以100然后以fixed-point('f')格式打印, 值后面会有一个百分号.                  |
| `{0:0>10}` | 字符串位数为10,靠右对齐，左侧空位以0补全                                                    |
| `{0:0<10}` | 字符串位数为10,靠左对齐，左侧空位以0补全                                                    |
| `{0:0^10}` | 字符串位数为10,居中对齐，左侧空位以0补全                                                    |


format函数可以使用别名的方式替换`{NUM}`，使代码更易于阅读

```python
>>> '{first} is as {second}.'.format(first='Caroline', second='Wendy') #别名替换
'Caroline is as Wendy.'
```
''
## 一些示例：

```python
age = 25
name = 'Caroline'

print('{0} is {1} years old. '.format(name, age)) #输出参数 Caroline is 25 years old.
print('{0} is a girl. '.format(name)) # Caroline is a girl.
print('{0:.3} is a decimal. '.format(1/3)) #小数点后三位 0.333 is a decimal.
print('{0:_^11} is a 11 length.'.format(name)) #使用_补齐空位 _Caroline__ is a 11 length.
print('{0:.2%} is a percent.'.format(0.5)) # '50.00% is a percent.'
print('{first} is as {second}. '.format(first=name, second='Wendy')) #别名替换
print('My name is {0.name}'.format(open('out.txt', 'w'))) #调用方法 My name is out.txt
print('My name is {0:8}.'.format('Fred')) #指定宽度 My name is Fred    .
```

## 转义

可以使用{}对{}进行转义

```python
>>>'{} world{{!}}'.format('hello')
'hello world{!}'
```
然而，在大量存在{}时，比如js函数库的字符替换，这种方法比较繁琐，还要回退到%字符操作符的方式。