---
title: 在windos下使用shell脚本
date: 2017-04-26 23:26:56
tags:
---

## 使用node切换命令行目录问题

因为日常需要，打算使用nodejs写一个更改cmd命令行目录的小程序,保存一下日常使用的目录，方便进行目录切换，预想效果如下

```
> E:\Users\gaian $ go project
> D:\nodejs\demos\project
> D:\nodejs\demos\project $ go blog
> E:\Users\gaian\gaianote.github.io
```

本来以为很简单的几行代码就可以完成，后来发现这个需求居然无法实现，因为node的子进程无法更改父进程的工作目录

## 使用shell脚本进行功能实现

于是打算使用shell进行功能实现，那么什么shell是用户和Linux操作系统之间的接口。Linux中有多种shell，其中缺省使用的是Bash。什么是bash呢? 简单来讲，Linux发行版支持各种各样的GUI（graphical user interfaces），但在某些情况下，Linux的命令行接口(bash)仍然是简单快速的。Bash和Linux Shell需要输入命令来完成任务，因而被称为命令行接口。

windows下具体步骤如下：

1.下载一个支持bash的cmd命令行工具，我一直在使用[cmder](http://cmder.net/)，这款工具美观且功能强大，推荐大家尝试一下,在 cmder 中输入 `bash` ，就可以从 windows 的命令行模式更改为 bash 模式，非常方便

```
# win
E:\Users\gaian
λ bash

# bash
gaian@DESKTOP-OTILKFV  ~
$
```

其实我们可以通过设置 Cmder ，改为默认以 bash 模式启动 Cmder , 如果你不习惯 win 下的命令的话，可以进行以下设置：

以管理员身份运行 Cmder ，在 Cmder 中选择 `Setting` ，然后在 `Startup` -> `Tasks` -> `{cmd::Cmder}` 中输入如下启动方式，这样就可以通过鼠标右键菜单打开 Bash 了，并且是在当前文件夹打开，同时也避免了在 Vim 中方向键失灵的问题。

```
cmd /k "%ConEmuDir%\..\init.bat"  -new_console:p:n%USERPROFILE% &bash
```

这样我们在打开 Cmder 后，便直接进入 Bash 模式

```
gaian@DESKTOP-OTILKFV  ~
$
```
当我们每次关闭 Cmder 时都会弹出提示框提示 Confirm closing console? ，只需要在 `Setting` -> `Main` -> `Confirm` -> `Close confirmations` 中取消 When running process was detected 前面选中状态，就可以关闭提示框的弹出。


2.在user目录下，新建一个 .bashsrc 脚本，写入如下内容用

```bash
go(){
  if [ $1 = "blog" ]; then
    cd "E:\Users\gaian\gaianote.github.io"
  elif [ $1 = "post" ]; then
    cd "E:\Users\gaian\gaianote.github.io\source\_posts"
  fi
}
```

3.更新 .bashrc 使之立即生效

```bash
$ cd ~
$ source .bashrc
```

4.使用定义好的shell脚本

```bash
gaian@DESKTOP-OTILKFV  ~
$ go blog
gaian@DESKTOP-OTILKFV  ~/gaianote.github.io
$ go post
gaian@DESKTOP-OTILKFV  ~/gaianote.github.io/source/_posts
```

## bash基本语法


**变量**

bash变量不需要定义，使用时添加$表示变量

```bash
STR="Hello World"
echo $STR
```

**判断语句**

```bash
if [ "foo" = "foo" ]; then
  echo 'nice'
fi
```

**循环语句**

```bash
n=1
while [ $n -le 10 ]
do
    echo $n
    let n++
done
```

break 语句可以让程序流程从当前循环体中完全跳出，而 continue 语句可以跳过当次循环的剩余部分并直接进入下一次循环

**函数**

bash 的函数不用传入参数，默认以 $1 $2 表示第一个变量，第二个变量...

```bash
foo() {
echo $1
}
```

```bash
$ foo Hello
Hello
```

## bash常用命令

`ls` –List

ls会列举出当前工作目录的内容（文件或文件夹），就跟你在GUI中打开一个文件夹去看里面的内容一样。

`mkdir` –Make Directory

mkdir用于新建一个新目录

`pwd` –Print Working Directory

pwd显示当前工作目录

`cd` –Change Directory

对于当前在终端运行的会中中，cd将给定的文件夹（或目录）设置成当前工作目录。

`rmdir` –Remove Directory

rmdir删除给定的目录。

`rm` –Remove

rm会删除给定的文件或文件夹，可以使用rm -r递归删除文件夹

`cp` –Copy

cp命令对文件或文件夹进行复制，可以使用cp -r选项来递归复制文件夹。

`mv` –MoVe

mv命令对文件或文件夹进行移动，如果文件或文件夹存在于当前工作目录，还可以对文件或文件夹进行重命名。

`cat` –concatenate and print files

cat用于在标准输出（监控器或屏幕）上查看文件内容

`tail` –print TAIL (from last) >

tail默认在标准输出上显示给定文件的最后10行内容，可以使用tail -n N指定在标准输出上显示文件的最后N行内容。

`less` –print LESS

less按页或按窗口打印文件内容。在查看包含大量文本数据的大文件时是非常有用和高效的。你可以使用Ctrl+F向前翻页，Ctrl+B向后翻页。

`grep`

grep ""在给定的文件中搜寻指定的字符串。grep -i ""在搜寻时会忽略字符串的大小写，而grep -r ""则会在当前工作目录的文件中递归搜寻指定的字符串。

`Find`

这个命令会在给定位置搜寻与条件匹配的文件。你可以使用find -name的-name选项来进行区分大小写的搜寻，find -iname来进行不区分大小写的搜寻。
find <folder-to-search> -iname <file-name>

`tar`

tar命令能创建、查看和提取tar压缩文件。tar -cvf是创建对应压缩文件，tar -tvf来查看对应压缩文件，tar -xvf来提取对应压缩文件。

`gzip`

gzip命令创建和提取gzip压缩文件，还可以用gzip -d来提取压缩文件。

`unzip`

unzip对gzip文档进行解压。在解压之前，可以使用unzip -l命令查看文件内容。

`help`

--help会在终端列出所有可用的命令,可以使用任何命令的-h或-help选项来查看该命令的具体用法。

`whatis` –What is this command

whatis会用单行来描述给定的命令。

`man` –Manual

man会为给定的命令显示一个手册页面。

`exit`

exit用于结束当前的终端会话。

`ping`

ping通过发送数据包ping远程主机(服务器)，常用与检测网络连接和服务器状态。

`who` –Who Is logged in

who能列出当前登录的用户名。

`su` –Switch User

su用于切换不同的用户。即使没有使用密码，超级用户也能切换到其它用户。

`uname`

uname会显示出关于系统的重要信息，如内核名称、主机名、内核版本、处理机类型等等，使用uname -a可以查看所有信息。

`free` –Free memory

free会显示出系统的空闲内存、已经占用内存、可利用的交换内存等信息，free -m将结果中的单位转换成KB，而free–g则转换成GB。

`df` –Disk space Free
df查看文件系统中磁盘的使用情况–硬盘已用和可用的存储空间以及其它存储设备。你可以使用df -h将结果以人类可读的方式显示。

`ps` –ProcesseS

ps显示系统的运行进程。

`Top` –TOP processes

top命令会默认按照CPU的占用情况，显示占用量较大的进程,可以使用top -u查看某个用户的CPU使用排名情况。

`shutdown`

shutdown用于关闭计算机，而shutdown -r用于重启计算机。

`start`

以单独窗口运行程序，可以用来打开文件或文件夹,例如 `start .`打开当前文件夹



## 参考资料

[bash编程之if……else条件判断](http://zhaochj.blog.51cto.com/368705/1315581)