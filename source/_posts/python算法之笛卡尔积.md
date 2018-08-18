---
title: python算法之笛卡尔积
date: 2018-05-25 14:44:42
tags: python
---

## 什么是笛卡尔积

笛卡尔乘积是指在数学中，两个集合X和Y的笛卡尓积（Cartesian product），又称直积

假设集合A={a, b}，集合B={0, 1, 2}，则两个集合的笛卡尔积为{(a, 0), (a, 1), (a, 2), (b, 0), (b, 1), (b, 2)}

## 笛卡尔积的python实现

python内置了itertools库，直接引入即可，无需第三方依赖

```python
import itertools 
a = [1,2,3]
b = [4,5,6] 
print ("a,b的笛卡尔乘积：") 
for x in itertools.product(a,b):  
    print (x) 
```

输出结果为:

```
a,b的笛卡尔乘积：
(1, 4)
(1, 5)
(1, 6)
(2, 4)
(2, 5)
(2, 6)
(3, 4)
(3, 5)
(3, 6)
```