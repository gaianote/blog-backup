* re模块的基本使用
* python正则表达式规则
* re模块方法

## re模块的基本使用
python正则表达式整体来讲只需两步即可使用：

```python
import re
# 1.获得pattern对象，pattern = re.compile('正则表达式')
pattern = re.compile('^\d{0,2}')
# 2.使用re方法获得所需内容
pattern.split('one1two2three3four4')
```

## re模块方法

字符串替换 sub

```python
# 第一个参数：规则 第二个参数：替换后的字符串 第三个参数：字符串 第四个参数：替换个数。默认为0，表示每个匹配项都替换
re.sub(pattern, replace, string, count=0)
```