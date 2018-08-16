---
title: win10下linux子系统安装与使用
date: 2018-08-16 09:46:30
tags: windows linux
---

微软大概为了和OS X竞争，在windows环境下加入了一个linux子系统，据说是目前最好用的Linux发行版(滑稽)。我个人看来的话是有学习linux或者某些业务场景需要使用但不想装虚拟机的话wsl确实是一个不错的选择，事实上也确实比虚拟机流畅。

<!--more-->

## linux子系统安装步骤：

**1. 设置 ——> 更新和安全**

![img](/images/2018081600.png)
**2. 开发者选项 ——> 开发人员模式**

![img](/images/2018081601.png)
**3. 程序和功能 ——> 启用和关闭Windows 功能 ——> 勾选最后的Lunix子系统**

![img](/images/2018081602.png)

**4. 在Microsoft Store搜索关键字linux,选择需要的Lunix分发版本**

![img](/images/20180324220413133.png)

**5. 打开cmd，输入bash,进入linux子系统**


## 混合 Windows 和 Linux 的环境

在 Linux 环境里运行 Windows 软件？非常有趣。Windows 已经被挂在到了 `/mnt` 目录里，只需要找到自己需要的 exe 文件就可以执行。

路径中文件名含有空格的话，使用""括起文件路径即可

为了方便使用,可以给程序创建软链接:

```
ln -s "/mnt/c/Program Files/Sublime Text 3/sublime.exe" /bin/sublime
```

当给你需要执行 Windows 上的 Python 时，可以使用以下命令

```python
sublime # 打开sublime
sublime readme.md # 使用sublime打开当前目录的readme.md
```


## zsh 与 antigen

> 目前常用的 Linux 系统和 OS X 系统的默认 Shell 都是 bash，但是真正强大的 Shell 是深藏不露的 zsh， 这货绝对是马车中的跑车，跑车中的飞行车，史称『终极 Shell』，但是由于配置过于复杂，所以初期无人问津，很多人跑过来看看 zsh 的配置指南，什么都不说转身就走了。直到有一天，国外有个穷极无聊的程序员开发出了一个能够让你快速上手的zsh项目，叫做 [oh my zsh](https://github.com/robbyrussell/oh-my-zsh)这玩意就像「X天叫你学会 C++」系列，可以让你神功速成，而且是真的。

> 但是oh my zsh 仍然需要很多配置,如果希望更简单的使用，推荐使用zsh 的包管理器： [antigen](https://github.com/zsh-users/antigen)来管理所有功能

### 安装zsh并启用

```bash
sudo apt-get -y install zsh
```

* 设置终端的 shell 环境默认为 zsh，输入以下命令(需要重启)

```bash
# 加 sudo 是修改 root 帐号的默认 shell
chsh -s `which zsh`
```

* 如果上面命令无效，修改 ~/.bashrc 在开头输入：

```shell
if [ -t 1 ]; then
    exec zsh
fi
```

### 安装antigen并启用

```bash
curl -L git.io/antigen > antigen.zsh
# 使用 zsh 主题 robbyrussell
antigen theme robbyrussell
```

通常我们希望默认启用antigen theme,而不是每次打开终端都需要重新设置,此时只需要`vi ~/.zshrc`:在设置文件`antigen apply`之前添加一行`antigen theme robbyrussell`即可。


```
antigen theme robbyrussell
# Tell Antigen that you're done.
antigen apply
```

### 一些问题

输入zsh,启动zsh时会提示:

zsh compinit: insecure directories, run compaudit for list.
Ignore insecure directories and continue [y] or abort compinit [n]?

在[stackoverflow](https://stackoverflow.com/questions/13762280/zsh-compinit-insecure-directories)中找到了解决办法：

* setting the current user as the owner of all the directories/subdirectories/files in cause:

```bash
compaudit | xargs chown -R "$(whoami)"
```
* removing write permissions for group/others for the files in cause:

```bash
compaudit | xargs chmod go-w
```

## 终端[Hyper](https://hyper.is/)

windows下比较出名的终端当属cmder了，但是我在使用过程中遇到许多问题，最主要的一个就是复制多行文本时,会变成一行。机缘巧合下了解了hyper，尝试几次后便喜欢上了这款终端。


### 设置默认打开bash而不是win cmd

1. 选择`≡` -> `Edit` -> `Prefrence`打开配置文件

2. 找到以下文字，将`shell:''`改为`'C:\\Windows\\System32\\bash.exe'`

```
// Windows
// - Make sure to use a full path if the binary name doesn't work
// - Remove `--login` in shellArgs
//
// Bash on Windows
// - Example: `C:\\Windows\\System32\\bash.exe`
//
// PowerShell on Windows
// - Example: `C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe`
shell: 'C:\\Windows\\System32\\bash.exe',
```

### 设置默认打开路径

在linux系统中，`.bashrc`的第一行添加`cd ~`即可

## 参考文档

[Windows Subsystem for Linux使用全记录](https://github.com/oneone1995/blog/issues/6)