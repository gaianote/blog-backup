---
title: git速查手册
date: 2017-05-02 14:28:06
tags:
---

## git-ssh 配置和使用

使用https的方式push文件，每次都需要输入用户名以及密码，使用起来繁琐麻烦，因此可以通过配置ssh的方式快捷进行push操作

1. 设置Git的user name和email：(如果是第一次的话)

```bash
$ git config --global user.name "gaianote"
$ git config --global user.email "gaianote@163.com"
```

2. 生成密钥

```bash
$ ssh-keygen -t rsa -C "gaianote@163.com"
```

连续3个回车。如果不需要密码的话。
最后得到了两个文件：`id_rsa`和`id_rsa.pub`。
如果不是第一次，就选择overwrite.

3. 添加密钥到ssh-agent

确保 ssh-agent 是可用的。ssh-agent是一种控制用来保存公钥身份验证所使用的私钥的程序，其实ssh-agent就是一个密钥管理器，运行ssh-agent以后，使用ssh-add将私钥交给ssh-agent保管，其他程序需要身份验证的时候可以将验证申请交给ssh-agent来完成整个认证过程。

```
# start the ssh-agent in the background
$ eval "$(ssh-agent -s)"
Agent pid 59566
```
添加生成的 SSH key 到 ssh-agent。

```bash
$ ssh-add ~/.ssh/id_rsa
```

4. 登陆Github, 添加 ssh 。

把id_rsa.pub文件里的内容复制到SSH Keys这里


5. 测试：

```bash
$ ssh -T git@github.com
```
你将会看到：

```
The authenticity of host 'github.com (207.97.227.239)' can't be established.
RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)?
```
选择 yes

```
Hi gaianote! You've successfully authenticated, but GitHub does not provide shell access.
```
如果看到Hi后面是你的用户名，就说明成功了。

6. 修改.git文件夹下config中的url。(.git文件夹在项目根目录，它是默认隐藏的)

修改前

```
    [remote "origin"]
    url = https://github.com/gaianote/gaianote.github.io.git
    fetch = +refs/heads/*:refs/remotes/origin/*
```

修改后

```
    [remote "origin"]
    url = git@github.com:gaianote/gaianote.github.io.git
    fetch = +refs/heads/*:refs/remotes/origin/*
```
## 忽略不想提交的文件

当一个文件提交了，但是又更新了 .gitignore 文件，可以使用如下方式删除缓存，再重新提交

```
git rm --cached file_path
```

示例，项目文件结构如下：

```
learn-js
|-node
  |-.gitignore
  |-koa2
  |-node_moudles
```

我未创建 .gitignore 文件便进行提交，之后希望忽略 node_moudles ，只需进行如下操作

```bash
git rm -r --cached node_moudles
```

## git单次push内容过大

http.postBuffer默认上限为1M,当你修改的内容超过这个上限时，git push 就会报错：

```
fatal: The remote end hung up unexpectedly
```

解决方法是在 `.git/config` 文件中加入:

```
[http]
postBuffer = 524288000
```

或者:

```bash
git config http.postBuffer 524288000
```
