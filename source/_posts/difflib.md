---
title: difflib字符串相似性对比
date: 2017-04-23 22:07:42
tags: python
---

```python
import difflib
str1 = '拥有一拳就能打倒任何怪人设定的斗篷光头男的名字是'
str2 = '拥有quit拳q^it就能打倒任何怪人设定的斗篷光头男的名字是'
result = difflib.SequenceMatcher(None, str1, str2).ratio()
print(result)
```