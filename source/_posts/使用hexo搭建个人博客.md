---
title: 使用hexo搭建博客并托管在github
date: 2017-04-23 00:03:44
tags: tool
---

## Hexo简介

Hexo 是一个简单地、轻量地、基于Node的一个静态博客框架，可以方便的生成静态网页托管在github和Heroku上。

使用Hexo之前，你首先需要做好准备工作:一个github账号，安装好nodejs，安装好git，当你完成上述内容后，就可以开始安装hexo了。

<!--more-->

## 安装hexo

打开cmd，依次执行以下命令

```bash
npm install hexo-cli -g
hexo init blog
cd blog
npm install
```

## 基本使用

**新建文章**

```bash
hexo new 文章标题
```

**启动服务器**

```bash
hexo server
```

执行`hexo server`后,可以在 http://localhost:4000/ 查看hexo创建好的博客

**发布到github**

* 发布到服务器前，需要通过`hexo generate`命令对所有的文章做静态化处理，生成html，css，js等文件
* 推送到github需要安装hexo-deployer，并且配置好_config.yml中的Deployment项，然后使用`hexo deploy`推送到github

```bash
npm install hexo-deployer-git -S
```

```bash
hexo generate
hexo deploy
```

**常用命令总结**

```bash
hexo n == hexo new
hexo g == hexo generate
hexo s == hexo server
hexo d == hexo deploy
```
## Hexo的配置

### 文件结构

```
gaianote.github.io
|
|-public # 存放hexo生成的html文件
|-dcaffolds # 模板文件夹，新建文章时，Hexo 会根据 scaffold 来建立文件
| |-draft.md
| |-page.md
| |-post.md # 默认模板post
|-source # 资源文件夹是存放用户资源的地方
| |-_post # 文件箱，新建的文章存放在这里
|-themes # 存放主题文件，Hexo 会根据主题来生成静态页面
| |-landscape ：默认的主题文件夹
|-_config.yml # 全局配置文件，每次更改要重启服务
|
```


## 配置文件 _config.yml

```yml
# Site 站点配置
title: 李云鹏的个人博客 # 网站标题
subtitle:
description:
author: 李云鹏
language: zh-CN
timezone:

# URL 链接配置
url: http://gaianote.github.io
root: /
permalink: :year/:month/:day/:title/
permalink_defaults:

# Directory 目录配置
source_dir: source # 资源文件夹，这个文件夹用来存放内容
public_dir: public # 公共文件夹，这个文件夹用于存放生成的站点文件
tag_dir: tags # 标签文件夹
archive_dir: archives # 归档文件夹
category_dir: categories # 分类文件夹
code_dir: downloads/code # Include code 文件夹
i18n_dir: :lang # 国际化文件夹
skip_render:  # 跳过指定文件的渲染，您可使用 glob 来配置路径

# Writing 写作配置
new_post_name: :title.md # 新文章的文件名称
default_layout: # 默认布局
titlecase: false # Transform title into titlecase
external_link: true # Open external links in new tab
filename_case: 0 # 把文件名称转换为 1 小写或 2 大写
render_drafts: false # 显示草稿
post_asset_folder: false  # 是否启动资源文件夹
relative_link: false # 把链接改为与根目录的相对位址
future: true
highlight: # 代码块的设置
  enable: true
  line_number: true
  auto_detect: false
  tab_replace:

# Category & Tag # 分类 & 标签
default_category: uncategorized # 默认分类
category_map: # 分类别名
tag_map: # 标签别名

# Date / Time format 时间和日期
date_format: YYYY-MM-DD
time_format: HH:mm:ss

# Pagination 分页
per_page: 10 # 每页显示的文章量 (0 = 关闭分页功能)
pagination_dir: page # 分页目录

# Extensions 扩展
theme: hexo-theme-yilia # 当前主题名称

# Deployment # 部署到github
deploy:
  type: git
  repo: https://github.com/gaianote/gaianote.github.io.git
  branch: master
```

## 主题配置

```
gaianote.github.io
|
|-themes # 存放主题文件，Hexo 会根据主题来生成静态页面
| |-landscape # 默认的主题文件夹
| |-hexo-theme-yilia # 笔者使用的主题
|   |-languages
|   |-layout
|   |-source
|   |-source-src
|   |-_config.yml # 主题的全局配置
|   |-README.md # 主题的使用说明
|
```

在使用主题过程中，我们结合 _config.yml和README.md 对主题进行设置即可

头像与favoicon放在public文件夹内即可生效

## 文章与草稿

### 属性

文章可以拥有如下属性,在文章的开头使用 ===== 与正文分隔

```
===========
layout      Layout ：post或page
title       文章的标题
date        创建日期 ：文件的创建日期
updated     修改日期 ：文件的修改日期
comments    是否开启评论 ：true|false
tags        标签
categories  分类
permalink   url中的名字 : 文件名
===========
```

分类和标签

```
===========
categories:
- 日记
tags:
- Hexo
- node.js
===========
```

### 草稿

当你撰写好一篇文章，并未打算发布时，需要使用草稿功能

**新建草稿**

```bash
hexo new draft "new draft"
```

新建草稿会在source/_drafts目录下生成一个new-draft.md文件。但是这个文件不被显示在页面上，链接也访问不到。

**预览草稿**

```bash
hexo server --drafts
```

**发布草稿**

```bash
 hexo publish [layout] <filename>
```

## 保存 Hexo 博客源码到 GitHub

因为 master 分支只保存了public 文件夹中的静态文件，所以需要创建一个分支来保存你的博客的源代码


## 参考资料

[hexo官网](https://hexo.io/)
[Hexo 入门指南](http://www.kancloud.cn/wizardforcel/markdown-simple-world/97380)
[简洁轻便的博客平台: Hexo详解](http://www.tuicool.com/articles/ueI7naV)
[20分钟教你使用hexo搭建github博客](http://www.jianshu.com/p/e99ed60390a8)
[有哪些好看的 Hexo 主题？](https://www.zhihu.com/question/24422335)

