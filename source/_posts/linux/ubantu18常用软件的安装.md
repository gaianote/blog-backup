---
title: ubantu18使用apt-get安装软件
tags:
  - linux
  - ubantu
categories: []
date: 2018-08-17 09:45:00
---
对于软件而言，软件厂商自己编译好了很多二进制文件，只要系统和环境对应，下载之后就能直接安装即可。

但是安装过程中还是会遇到很多痛点:

* 下载了很多软件想要管理怎么办?
* 下载一个软件还需要依赖很多别的软件怎么办?
* 想要及时更新怎么办?

因此我们需要把自己下载的历史信息记录下来，软件也记录自己的版本信息和依赖包。并且服务器也记录这些信息，这就是软件管理器了。

对于软件管理器,redhat主要是`rpm`和更高级的`yum`，debian主要是`dpkg`和更高级的`apt`。

<!--more-->

## apt-get

### 软件源

源和软件仓库实际上是一个意思，厂商将编译后的二进制文件和软件信息存放至服务器，用户需要安装软件时，包管理器自动分析本机和容器（repository）内的信息，下载需要的包并自动安装，安装后将新安装的软件信息存放至本地数据库。如果有前置软件没有安装，rpm和dpkg会提示安装失败，也可以强制安装，yum和apt会自动安装全部需要的依赖包。更新和卸载也同理。这些源的位置记录在`/etc/apt/sources.list`，我们可以手动修改这些文件，但是修改重要系统配置前先备份是一个好习惯。

### apt-get相关目录

**/var/lib/dpkg/available**

文件的内容是软件包的描述信息, 该软件包括当前系统所使用的 ubunt 安装源中的所有软件包,其中包括当前系统中已安装的和未安装的软件包.

**/var/cache/apt/archives**

目录是在用 apt-get install 安装软件时，软件包的临时存放路径

**/etc/apt/sources.list**

存放的是软件源站点

**/var/lib/apt/lists**

使用apt-get update命令会从/etc/apt/sources.list中下载软件列表，并保存到该目录

### 安装位置

|      位置      |      信息      |
|----------------|----------------|
| /usr/bin       | 二进制文件     |
| /usr/lib       | 动态函数库文件 |
| /usr/share/doc | 使用手册       |
| /usr/share/man | man page       |


### apt-get update

**sudo apt-get update 执行这条命令后计算机做了什么？**

无论用户使用哪些手段配置APT软件源，只是修改了配置文件——/etc/apt/sources.list，目的只是告知软件源镜像站点的地址。但那些所指向的镜像站点所具有的软件资源并不清楚，需要将这些资源列个清单，以便本地主机知晓可以申请哪些资源。

用户可以使用“apt-get update”命令刷新软件源，建立更新软件包列表。在Ubuntu Linux中，“apt-get update”命令会扫描每一个软件源服务器，并为该服务器所具有软件包资源建立索引文件，存放在本地的/var/lib/apt/lists/目录中。 使用apt-get执行安装、更新操作时，都将依据这些索引文件，向软件源服务器申请资源。因此，在计算机设备空闲时，经常使用“apt-get update”命令刷新软件源，是一个好的习惯。

### apt-get install

**sudo apt-get install XXX 后计算机做了什么？**

使用“apt-get install”下载软件包大体分为4步：

* 扫描本地存放的软件包更新列表（由“apt-get update”命令刷新更新列表，也就是/var/lib/apt/lists/），找到最新版本的软件包；
* 进行软件包依赖关系检查，找到支持该软件正常运行的所有软件包；
* 从软件源所指 的镜像站点中，下载相关软件包，并存放在/var/cache/apt/archive；
* 第四步，解压软件包，并自动完成应用程序的安装和配置。

### apt-get upgrade

**sudo apt-get upgrade 后计算机做了什么?**

使用“apt-get install”命令能够安装或更新指定的软件包。而在Ubuntu Linux中，只需一条命令就可以轻松地将系统中的所有软件包一次性升级到最新版本，这个命令就是“apt-get upgrade”，它可以很方便的完成在相同版本号的发行版中更新软件包。

在依赖关系检查后，命令列出了目前所有需要升级的软件包，在得到用户确认后，便开始更新软件包的下载和安装。当然，apt- get upgrade命令会在最后以合理的次序，安装本次更新的软件包。系统更新需要用户等待一段时间。

## 软件安装

对于新的系统而言,首先需要升级apt-get,否则很多软件是找不到的

```bash
sudo apt-get update
```

## 安装nodejs和npm

```bash
sudo apt-get -y install nodejs
sudo apt-get -y install npm
```

### 运行node提示错误

```
run npm command gives error "/usr/bin/env: node: No such file or directory"
```

```bash
ln -s /usr/bin/nodejs /usr/bin/node 
```

### 系统node无法更新


我遇到了一个问题，即在我的ubantu16 上安装nodejs无法更新，始终显示4.2版本，通过以下方法解决了问题


```bash
sudo apt-get install curl
sudo apt autoremove
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install nodejs
```

运行完成后，查看版本号，已经是第10版了，至此升级成功

```bash
nodejs -v
```
