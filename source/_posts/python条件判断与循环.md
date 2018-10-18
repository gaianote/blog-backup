---
title: python条件判断与循环
date: 2018-05-29 16:35:18
tags: python
---

## 条件判断if

### if和执行可以写入一行内

```python
is_fat = True
if is_fat: print('fat')
```

### 三元运算符，if和else可以写入一行

```python
is_fat = True
state = "fat" if is_fat else "not fat"
```

### or在if中的使用

```python
result = 5
if result == 1 or 2 or 3 or 4:
    print('result is right')
```
输出结果为'result is right',可能与你的预期不符，它的实际判断为：

```python
if (result == 1) or 2 or 3 or 4:
    print('result is right')
```

这个表达式是恒成立的，如果希望达到所需设想，可以使用如下示例：

```python
if result in [1,2,3,4]:
    print('result is right')
```

## 循环

### break和continue语句及循环中的else子句

break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止（使用break），任何对应的循环 else 块将不执行。 否则在正常执行完毕后，会继续执行else后的语句,实例如下：

```python
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```

输出结果:

```
循环数据 Baidu
循环数据 Google
菜鸟教程!
完成循环!
```

```python
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```
```
循环数据 Baidu
循环数据 Google
循环数据 Runoob
循环数据 Taobao
没有循环数据!
完成循环!
```

