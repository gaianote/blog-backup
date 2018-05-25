---
title: Python字典
date: 2018-05-25 09:39:29
tags: python
---

## 知道value如何找到key值

```
>>> dic = {'a': {'c':'001'}, 'b':'002'}
>>> list(dic.keys())[list(dic.values()).index("001")]
'a'
>>>
```

dic = {'a':'001', 'b':'002'}
引用一段Python3文档里面的原话。

If keys, values and items views are iterated over with no intervening modifications to the dictionary, the order of items will directly correspond.

也就是说，在你迭代的过程中如果没有发生对字典的修改，那么.keys() and .values 这两个函数返回的 dict-view对象总是保持对应关系。