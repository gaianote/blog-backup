---
title: python在控制台输出颜色
date: 2018-05-30 10:25:10
tags: python
---

```bash
pip install termcolor
```

## Example

```python
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)

cprint('Hello, World!', 'green', 'on_red')
```

## Text Properties

### 文字颜色:

```
grey
red
green
yellow
blue
magenta
cyan
white
```

### 文字背景颜色:
```
on_grey
on_red
on_green
on_yellow
on_blue
on_magenta
on_cyan
on_white
```

### 文字属性:

```
bold
dark
underline
blink
reverse
concealed
```
