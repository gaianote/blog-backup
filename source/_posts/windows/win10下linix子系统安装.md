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


## [WSL与Windows的互操作性](https://docs.microsoft.com/en-us/windows/wsl/interop)

Windows的Linux子系统（WSL）不断改进Windows和Linux之间的集成。
您可以：

* 从Linux控制台调用Windows二进制文件。
* 从Windows控制台调用Linux二进制文件。
* **Windows Insiders**在Linux和Windows之间**构建17063+**共享环境变量。

这提供了Windows和WSL之间的无缝体验。技术细节在[WSL博客](https://blogs.msdn.microsoft.com/wsl/2016/10/19/windows-and-ubuntu-interoperability/)上

### 从WSL运行Windows程序

WSL可以使用直接从WSL命令行调用Windows二进制文件`[binary name].exe`。例如，`notepad.exe`。为了使Windows可执行文件更易于运行

比如运行安装在windows中的sublime:

```bash
# 路径中文件名含有空格的话，要使用""括起文件路径即可
$ '/mnt/c/Program Files/Sublime Text 3/sublime.exe'
```
如果`sublime`在你的系统路径中的话，直接调用sublime.exe即可

```bash
$ sublime.exe
```

为了方便的运行sublime,我们需要给它创建一个软连接

```bash
$ ln -s "/mnt/c/Program Files/Sublime Text 3/sublime.exe" /bin/sublime
$ sublime
```

### 从WSL修改Windows文件

> 首先了解一点，不支持使用WSL中的Windows应用程序修改位于VolF（不在`/mnt/`下）的文件.

使用sublime打开位于/mnt/下的某个文件,修改后保存,然后使用(linux的)python执行它,这是一个完美的无缝工作流，非常了不起。

```python
$ sublime "/mnt/c/simple.py"
$ python simple.py
```

### 安装并使用autojump

由于windows挂在到mnt路径下，你的项目路径一般比较深，cd转换目录非常的麻烦，利用autojump可以解决这个问题。

autojump的工作方式很简单：它会在你每次启动命令时记录你当前位置，并把它添加进它自身的数据库中。这样，某些目录比其它一些目录添加的次数多，这些目录一般就代表你最重要的目录，而它们的“权重”也会增大。

#### 在Linux上安装autojump

在Ubuntu或Debian上安装autojump：

```bash
$ sudo apt-get install autojump
```

要在CentOS或Fedora上安装autojump，请使用yum命令。在CentOS上，你需要先启用EPEL仓库才行。

```bash
$ sudo yum install autojump
```

在Archlinux上安装autojump：

```bash
$ sudo pacman -S autojump
```

如果你找不到适合你的版本的包，你可以从GitHub上下载源码包来编译。

#### 启用autojump

```bash
chmod 755 /usr/share/autojump/autojump.bash

# 如果使用bash:
echo "source /usr/share/autojump/autojump.bash" >> ~/.bashrc && source ~/.bashrc
# 如果使用zsh:
echo "source /usr/share/autojump/autojump.zsh" >> ~/.zshrc && source ~/.zshrc
```

#### 使用autojump

假如我曾经访问过`/mnt/c/Users/user/gaianote.github.io`，那么直接执行：

```bash
j gaianote # 全称或者部分名称
```
便可以快捷的跳转到相应的目录了

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
# 修改配置 ~/.zshrc（如果切换帐号后无法使用 zsh 则把该用户的配置文件再配一遍）
curl -L https://raw.githubusercontent.com/skywind3000/vim/master/etc/zshrc.zsh > ~/.zshrc
# 使用 zsh 主题 robbyrussell
antigen theme robbyrussell
```

通常我们希望默认启用antigen theme,而不是每次打开终端都需要重新设置,此时只需要`vi ~/.zshrc`:在设置文件`antigen apply`之前添加一行`antigen theme robbyrussell`即可。


```
antigen theme robbyrussell
# Tell Antigen that you're done.
antigen apply
```
更多的主题可以到[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/wiki/themes)项目中查看

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

### windows子系统下ls难看的底色问题

ls 颜色设置一个在实际使用中一个比较困扰我的问题是在bash on windows这边，使用ls显示的目录大都有很难看的底色；而对于正常的linux环境下，则没有这个问题；

这个的原因其实是因为windows的目录在linux这边的权限不同，导致windows的目录在ls的默认颜色中就应该有那种底色；所以只要修改环境变量`$LS_COLORS`就可以了

具体的不同：在windows下，目录都是`ow`，即`Directory that is other-writable (o+w) and not sticky`；而正常linux系统下的目录都是`di`
默认的`$LS_COLORS`如下：

```
rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lz=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.rar=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.axa=00;36:*.oga=00;36:*.spx=00;36:*.xspf=00;36:

```

可以看到其中`ow`的配色是`34;42`,其中那个42就是指定颜色的底色的意思，我们只要在配置中删掉它就可以啦~修改方式，还是在`~/.bashrc`文件里加上相关设置，把它放到开头,然后执行source命令就可以了=，=我的修改示例：

```
# for ls colors
LS_COLORS="rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=01;34:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.axa=00;36:*.oga=00;36:*.spx=00;36:*.xspf=00;36:"
export LS_COLORS
```
#### 样式列表

**样式**：

00 — Normal (no color, no bold)
01 — Bold    //粗体

**文字颜色**

30 — Black   //黑色
31 — Red     //红色
32 — Green   //绿色
33 — Yellow  //黄色
34 — Blue    //蓝色
35 — Magenta //洋红色
36 — Cyan    //蓝绿色
37 — White   //白色

**背景颜色**

40 — Black
41 — Red
42 — Green
43 — Yellow
44 — Blue
45 — Magenta
46 — Cyan
47 – White

白色：    表示普通文件
蓝色：    表示目录
绿色：    表示可执行文件
红色：    表示压缩文件
蓝绿色：  链接文件
红色闪烁：表示链接的文件有问题
黄色：    表示设备文件
灰色：    表示其他文件

### 文字大小

最新版本(截止至1808月)的hyper有个bug,使用插件verminal的时候无法改变fontSize，字体显得非常小，删掉它之后就可以正常工作了。

![img](/images/2018-08-16_19-46-48.png)

## 参考文档

[Windows Subsystem for Linux使用全记录](https://github.com/oneone1995/blog/issues/6)
[windows命令行工具 Hyper全面介绍](https://cibifang.com/win10%E7%BB%88%E7%AB%AF%E4%BC%98%E5%8C%96-%E9%AB%98%E9%A2%9C%E5%80%BCwindows%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7hyper%E5%85%A8%E9%9D%A2%E4%BB%8B%E7%BB%8D/)