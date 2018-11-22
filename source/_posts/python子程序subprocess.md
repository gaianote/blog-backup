title: python子程序subprocess
author: 李云鹏
date: 2018-11-01 06:45:05
tags:
---
## python subprocess

用于程序执行时调用子程序，通过stdout,stdin和stderr进行交互。
```
Stdout子程序执行结果返回，如文件、屏幕等
Stdin 子程序执行时的输入，如文件，文件对象
Stderr 错误输出
```

常用的两种方式（以shell程序为例）：

```
subprocess.Popen('脚本/shell', shell=True)   #无阻塞并行
subprocess.call('脚本/shell', shell=True)   #等子程序结束再继续
```

两者的区别是前者无阻塞,会和主程序并行运行,后者必须等待命令执行完毕,如果想要前者编程阻塞加wait()：

```
p = subprocess.Popen('脚本/shell', shell=True)
a=p.wait() # 返回子进程结果
```
## 代码实例

对于diskpart这种命令行交互程序，应该使用Popen

```python
import subprocess
diskpart = subprocess.Popen('diskpart',stdout = subprocess.PIPE, stdin = subprocess.PIPE,stderr = subprocess.PIPE,shell=False)
stdout, stderr = diskpart.communicate(b'RESCAN\r\nLIST DISK\r\n')
print (stdout.decode('gbk'))
```
输出:
```
Microsoft DiskPart 版本 10.0.17134.1

Copyright (C) Microsoft Corporation.
在计算机上: DESKTOP-UI2H32O

DISKPART>
  磁盘 ###  状态           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁盘 0    联机              465 GB  1024 KB        *
```
这是一次性交互，读入是stdin，直接执行完毕后，返回给stdout，communicate通信一次之后即关闭了管道。但如果需要多次交互，频繁地和子线程通信不能使用communicate()， 可以分步进行通信，如下：


```python
p= subprocess.Popen(["ls","-l"], stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=False)  
//输入
p.stdin.write('your command')  
p.stdin.flush() 
//查看输出
p.stdout.readline() 
p.stdout.read()
```


## 参数shell的意义

call()和Popen()都有shell参数，默认为False，可以赋值为True。
参数shell（默认为False）指定是否使用shell来执行程序。如果shell为True，前面会自动加上/bin/sh命令，则建议传递一个字符串（而不是序列）给args，如果为False就必须传列表，分开存储命令内容。比如
```
subprocess.Popen("cat test.txt", shell=True)
```
相当于
```
subprocess.Popen(["/bin/sh", "-c", "cat test.txt"])
```
原因具体是:

在Linux下，shell=False时, Popen调用os.execvp()执行args指定的程序；
在Windows下，Popen调用CreateProcess()执行args指定的外部程序，args传入字符和序列都行，序列会自动list2cmdline()转化为字符串，但需要注意的是，并不是MS Windows下所有的程序都可以用list2cmdline来转化为命令行字符串。

所以，windows下

```
subprocess.Popen("notepad.exe test.txt" shell=True)
```
等同于

```
subprocess.Popen("cmd.exe /C "+"notepad.exe test.txt" shell=True）

```

## shell=True可能引起问题


传递shell=True在与不可信任的输入绑定在一起时可能出现安全问题
警告 执行的shell命令如果来自不可信任的输入源将使得程序容易受到shell注入攻击，一个严重的安全缺陷可能导致执行任意的命令。因为这个原因，在命令字符串是从外部输入的情况下使用shell=True 是强烈不建议的：
```
>>> from subprocess import call
>>> filename = input("What file would you like to display?\n")
What file would you like to display?
non_existent; rm -rf / #
>>> call("cat " + filename, shell=True) # Uh-oh. This will end badly...
```
shell=False禁用所有基于shell的功能，所以不会受此漏洞影响；参见Popen构造函数文档中的注意事项以得到如何使shell=False工作的有用提示。
当使用shell=True时，pipes.quote()可以用来正确地转义字符串中将用来构造shell命令的空白和shell元字符。