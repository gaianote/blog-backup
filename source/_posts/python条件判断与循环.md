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
if result == 1 or 2 or 3 or 4:
    print('result is right')
```
当希望result = 1 或者 result = 2时，输出结果，则以上的示例是错误的，它的实际判断为：

```python
if (result == 1) or 2 or 3 or 4:
    print('result is right')
```

这个表达式是恒成立的，如果希望达到所需设想，可以使用如下示例：

```python
if (result == 1) or 2 or 3 or 4:
    print('result is right')
```