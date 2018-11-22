title: python在控制台输出颜色
tags: python
date: 2018-05-30 10:25:10
---
首先安装termcolor库

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
## windows支持

termcolor仅支持linux系统，对于windows，需要结合[colorama](https://pypi.org/project/colorama/)库进行使用

```python
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

# then use Termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))
```
