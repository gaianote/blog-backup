---
title: 如何去掉Linux终端输出的颜色
tags: linux
date: 2019-02-17 03:45:02
---

## 1. 问题

一般我们都会输出一些带颜色的日志或者标准输出,但现在我们想获取的这部分正好是有颜色的,就出现问题了.

例如:

```
#grep 2.6.9_5-9-0-0 kernel.list |awk '{print $2}' | xargs -i ssh {}
Pseudo-terminal will not be allocated because stdin is not a terminal.
ssh: \033[34mbj-xxx.db: Name or service not known
xargs: ssh: exited with status 255; aborting
```

这里面的bj-xxx.db是需要处理的host,但是因为 kernel.list里面是有颜色的,所以ssh的时候报错,提示"\033[34m"+"真实的host"出错.

该如何去掉这些颜色字符呢?

## 2.回答

```bash
grep --color=never
```

如果是源数据里包含颜色转义符，用`sed`可以去掉：

```sh
sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g"
```

