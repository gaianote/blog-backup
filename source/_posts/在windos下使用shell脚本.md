---
title: 在windos下使用shell脚本
date: 2017-04-26 23:26:56
tags:
---

尝试使用nodejs写一个更改cmd命令行目录的小程序,保存一下日常使用的目录，方便进行目录切换，预想效果如下

```
> E:\Users\gaian $ go project
> D:\nodejs\demos\project
> D:\nodejs\demos\project $ go blog
> E:E:\Users\gaian\gaianote.github.io
```

本来以为很简单的几行代码就可以完成，后来发现这个需求无法实现，因为node的子进程无法更改父进程的工作目录

于是决定使用shell脚本进行实现，步骤如下：

1. 下载一个支持shell脚本的cmd命令行工具，我一直在使用cmder，这款工具强大且美观，推荐大家使用,在cmder中输入 `bash` ，就可以从windos的命令行更改为bash模式，非常方便

```
# win
E:\Users\lee
λ bash

# bash
gaian@DESKTOP-OTILKFV  ~
$
```
2. 在user目录下，新建一个 .bashsr 脚本，写入如下内容用

```bash
blog() {
  cd "E:\Users\gaian\gaianote.github.io"
}
```

3. 更新 .bashrc 使之立即生效

```bash
$ cd ~
$ source .bashrc
```

4.使用定义好的shell脚本

```bash
gaian@DESKTOP-OTILKFV  ~
$ blog
gaian@DESKTOP-OTILKFV  ~/gaianote.github.io
$
```
