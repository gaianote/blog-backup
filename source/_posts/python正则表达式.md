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
## re模块方法

### 字符串替换 sub

将源字符串(`source_string`)符合匹配规则的字符(`pattern`),替换为新字符(`new_str`)

```python
# 第二个参数：替换后的字符串 第三个参数：字符串 count：替换个数,默认为0，表示每个匹配项都替换
pattern.sub(new_str,source_string,count = 0)
```