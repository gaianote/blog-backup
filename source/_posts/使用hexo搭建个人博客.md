title: 使用hexo搭建博客并托管在github
tags: tool
date: 2017-04-23 00:03:44
---
## Hexo简介

Hexo 是一个简单地、轻量地、基于Node的一个静态博客框架，可以方便的生成静态网页托管在github和Heroku上。

使用Hexo之前，你首先需要做好准备工作:一个github账号，安装好nodejs，安装好git，当你完成上述内容后，就可以开始安装hexo了。

<!--more-->

### 快速开始(本项目)

1. 安装最新版本的 node.js ，注意安装时必须勾选 `add to path`
2. 运行`npm install hexo-cli -g` 安装命令行工具
3. 运行`git clone git@github.com:gaianote/gaianote.github.io.git`，将source分支clone到本地
4. cd到项目根目录，运行 `npm install` 安装相关依赖
5. `hexo server` 启动服务器，可以在本地浏览blog
6. 使用http://localhost:4000/admin/访问管理平台，在线编辑blog

### 云端推送

当我们需要更新blog时，运行以下命令即可完成推送本地blog到github中

```bash
$ hexo generate
$ hexo deploy
```

通过以上命令，系统会自动执行以下操作：

1. 生成html静态文件
2. 将生成的静态文件发布到master分支上(无需使用git切换到master分支)
3. 将blog源文件分支提交到source分支上(shelljs实现)

### 注意事项

本博客程序中的package依赖固定的版本号，当你直接更新某个主题或者依赖包时，可能会导致运行故障。因此，在博客展示正常的情况下，不建议对版本进行更新。

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
|-source # 资源文件夹是存放用户资源的地方，Markdown 和 HTML 文件会被解析并放到 public 文件夹，而其他文件会被拷贝过去
| |-_post # 文件箱，新建的文章存放在这里,除 _posts 文件夹之外，开头命名为 _ (下划线)的文件/ 文件夹和隐藏的文件将会被忽略
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

**使用git管理source分支**

在github上新建一个分支source，并将source设置为默认分支，通过source分支使用git管理源文件

配置好 .gitnore 文件，添加规则 public，因为public使用hexo deploy管理，无需重复添加

将远程仓库克隆到本地，然后连接远程仓库

```bash
git clone https://github.com/gaianote/gaianote.github.io
git remote add origin https://github.com/gaianote/gaianote.github.io
```

以后每次使用时，直接键入以下命令即可

```bash
git add .
git commit -m "update"
git push origin source
```

**使用 hexo deploy 管理master分支**

使用 hexo deploy 管理master分支，直接将静态文件发布到master分支上(无需使用git切换到master分支)

```bash
hexo deploy
```

## 实现流程自动化

hexo写博客非常享受，但是有可以改进的地方，比如每次新建文章时，都需要在post文件中查找新建立的文档，并且每次写完文章需要使用hexo和git备份两次，比较繁琐，我们可以使用shelljs实现自动化备份

通过查阅Hexo文档 ，找到了Hexo的主要事件，见下表：

|事件名         |事件发生时间         |
|---------------|---------------------|
|deployBefore   |在部署完成前发布     |
|deployAfter    |在部署成功后发布     |
|exit           |在 Hexo 结束前发布   |
|generateBefore |在静态文件生成前发布 |
|generateAfter  |在静态文件生成后发布 |
|new            |在文章文件建立后发布 |

于是我们就可以通过监听Hexo的 deployAfter 事件，待上传完成之后自动运行Git备份命令，从而达到自动备份的目的。

通过监听Hexo 的 new 事件，新建文章同时使用编辑器打开文档

首先，我们需要安装模块shelljs

```bash
npm install --save shelljs
```

待到模块安装完成，在博客根目录的 scripts 文件夹下新建一个js文件，文件名随意取；如果没有 scripts 目录，请新建一个。

然后在脚本内键入以下内容

```javascript
require('shelljs/global');

var path = require('path');

/* hexo deploy 时自动执行git push */

try {
  hexo.on('deployAfter', function() {//当deploy完成后执行备份
    run();
  });
} catch (e) {
  console.log("产生了一个错误<(￣3￣)> !，错误详情为：" + e.toString());
}

function run() {

  if (!which('git')) {
    echo('Sorry, this script requires git');
    exit(1);
  } else {
    echo("======================Auto Backup Begin===========================");
    cd(process.cwd());
    if (exec('git add --all').code !== 0) {
      echo('Error: Git add failed');
      exit(1);

    }
    if (exec('git commit -m "update"').code !== 0) {
      echo('Error: Git commit failed');
      exit(1);

    }
    if (exec('git push origin source').code !== 0) {
      echo('Error: Git push failed');
      exit(1);

    }
    echo("==================Auto Backup Complete============================")
  }
}

/* 新建文章自动打开编辑器 */

try {
  hexo.on('new', function(data) {
    exec(data.path)
  });
} catch (e) {
  console.log("产生了一个错误<(￣3￣)> !，错误详情为：" + e.toString());
}
```

这样，我们在使用Hexo命令时就可以自动触发git以及打开文章的操作了！

## 集成搜索服务

Next官网–>第三方服务–>搜索服务 中已经有详细的介绍了,主题内置了4种搜索方式:

- Swiftype
- 微搜索
- Local Search
- Algolia

由于自己的博客主要用于工作日志的记录,以及工作时的快速定位查询,因此选择了第三种方式Local Search,即本地搜索.

### 安装搜索插件

在Hexo根目录执行如下命令

```
$ npm install hexo-generator-searchdb --save
```

编辑**站点配置**文件
在站点配置文件(Hexo根目录的配置文件)_config.yml中添加

```yaml
search:
  path: search.xml
  field: post
  format: html
  limit: 10000
```

编辑**主题配置**文件,启用本地搜索
在主题配置文件(Next主题根目录的配置文件)_config.yml中启用

### Local search

```yaml
local_search:
  enable: true
```

注:以上内容在Next官网本地搜索模块有详细介绍,在此只为记录.

## hexo yilia主题添加文章访问量统计

hexo添加访问量统计功能可以用**百度的站长统计**、**leancloud**，还有**不蒜子**，这里我用的不蒜子，感觉挺简单的。

### 引入[不蒜子](http://busuanzi.ibruce.info/)

```html
<script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
```

这段代码可以写在footer.ejs里或者header.ejs里或者layout.ejs里，我用的yilia主题，放在/themes/yilia/layout/_partial/footer.ejs

### 添加站点访问量

通常站点的总访问量会显示在footer的位置，所以我们可以在footer.ejs里加上如下标签：

```html
<span id="busuanzi_container_site_uv">   本站访客数<span id="busuanzi_value_site_uv"></span>人次</span>
```

计算访问量的方法有两种：算法a：pv的方式，单个用户连续点击n篇文章，记录n次访问量。算法b：uv的方式，单个用户连续点击n篇文章，只记录1次访客数。我用的是uv的方式，大家自行选择即可。

### 添加文章访问量

文章的访问量显示在文章里面，所以在article.ejs里加上文章访问量的标签：

```html
<span id="busuanzi_container_page_pv">   本文总阅读量<span id="busuanzi_value_page_pv"></span>次</span>
```

我们直接就这样放在yilia主题中，首页也会显示该网页的访问量，没法正常使用，所以我加一个判断，如果是首页不显示该文章的访问量，下面这段代码添加在/themes/yilia/layout/_partial/article.ejs的header的日期后面：

```html
<%if ( !index ){ %>

<span class="archive-article-date">

   阅读量 <span id="busuanzi_value_page_pv"></span>

</span>

<%
 }
%>
```

### VPS gengrator 命令导致 hexo 被 killed 解决方案

```
free -m 
dd if=/dev/zero of=/swap bs=4096 count=1572864
mkswap /swap
swapon /swap
echo "LABEL=SWAP-sda /swap swap swap defaults 0 0" >> /etc/fstab
```
这样会在根目录建立一个 swap 文件,用于虚拟内存使用

`dd if=/dev/zero of=/swap bs=4096 count=1572864`命令时,会卡一会,等待即可,然后就可以正常使用 `hexo g` 命令了


## 参考资料

[hexo官网](https://hexo.io/)
[next官网](http://theme-next.iissnan.com/)
[Hexo 入门指南](http://www.kancloud.cn/wizardforcel/markdown-simple-world/97380)
[简洁轻便的博客平台: Hexo详解](http://www.tuicool.com/articles/ueI7naV)
[20分钟教你使用hexo搭建github博客](http://www.jianshu.com/p/e99ed60390a8)
[自动备份Hexo博客源文件](http://www.tuicool.com/articles/EnaqAvV)
[hexo-yilia主题添加文章访问量统计](http://www.lookk.cn/2017/12/09/hexo-yilia%E4%B8%BB%E9%A2%98%E6%B7%BB%E5%8A%A0%E6%96%87%E7%AB%A0%E8%AE%BF%E9%97%AE%E9%87%8F%E7%BB%9F%E8%AE%A1/)