---
title: sublime
date: 2017-05-18 00:03:44
tags: tool
---

## 快捷键

### `Ctrl+P` ：Goto Anything

`Ctrl+P` : 查找项目中的文件：

直接输入名称：在不同文件中切换，支持级联的目录模式

`:`：+ 行号：`Ctrl+G` 定位到具体的行。
`@`：+ 符号：`Ctrl+R` 定位到具体的符号，例如：JS函数名，CSS选择器名。
`#`：+ 关键字：`Ctrl+;` 匹配到具体的匹配的关键字。主要是模糊匹配。


## sublime配置文件

个人正在使用的sublime配置文件，解决了文件名中文显示为□□□等问题

```json
{
  "bold_folder_labels": true,
  "dpi_scale": 1.0,
  "font_face": "Consolas",
  "font_size": 16,
  "highlight_line": true,
  "highlight_modified_tabs": true,
  "ignored_packages":
  [
    "Vintage"
  ],
  "line_padding_bottom": 1,
  "line_padding_top": 1,
  "save_on_focus_lost": true,
  "show_encoding": true,
  "tab_size": 2,
  "translate_tabs_to_spaces": true,
  "trim_trailing_white_space_on_save": true,
  "word_wrap": false,
  "hot_exit": false,
  "remember_open_files": false
}
```
## 常用功能


## 插件安装

### 安装插件管理包 Package Control

1. 打开[Package Control的官方网页](https://packagecontrol.io/),点击右侧的 `Install Now` 按钮
2. 复制对应版本 2.0或 3.0的代码段
3. `Ctrl` + `~` 打开Sublime Text控制台，将之前复制的代码粘贴到控制台里，按下“Enter”键
4. 重启程序,点开菜单 `Preferences` 可见 `Package Control` 项，说明插件管理包已安装成功。

### 安装的两种方式

以 `ConvertToUTF8` 插件安装为例：

**功能说明**

 * 对于一些编码格式会导致中文乱码,ConcertToUTF8专为解决该问题而编写
 * ConvertToUTF8 能将除UTF8编码之外的其他编码文件在 Sublime Text 中转换成UTF8编码
 * 在保存文件之后原文件的编码格式不会改变

**安装方法**

通过 Package Control 在线安装

1. 菜单 `Preferences` -> `Package Control` -> `:Install Package`
2. 由于网络等问题,可能会等待数秒或更长时间才会响应,待出现插件搜索框后,输入需要的插件名称
3. 插件会自动安装,安装过程无任何提示,由于网络等问题,可能会等待数秒或更长时间
4. 安装成功后,会弹出Package Control Messages页面,而packag setting中也会出现该插件名称

通过文件夹的方式本地安装

1. 菜单 `Preferences` -> `Brower Package` 打开Package本地文件
2. 将解压好的插件包复制到这个 Packages 目录下

## markdown解决方案

**markdown语法高亮**

首先安装 `Markdown Extended` + `Monokai Extended` 这两个主题

选择 `Preference` > `Color Scheme` > `Monokai Extended` 更换主题颜色为 `Monokai Extended`

打开一个 `markdown` 文件，选择 `View` > `Syntax` > `open all with current ...` > `Markdown Extended` 设置 `markdown` 语法规则为 `Markdown Extended`

## 个人插件和使用方法

### `AdvancedNewFile` : 快速新建文件。

假设有文件夹file。我们正在输入代码，又想在新的子目录下新建html文件的话用传统方式得很多步，新建目录，新建文件，保存等等等。

但是有了该插件之后，事情就变得简单了许多，只需要按下 `Ctrl+ALT+N` ，输入文件夹以及文件名，你就会看到如下效果:（回车，你会发现已经子目录下的文件已经新建完成了！）

### `Terminal` ：在Sublime Text直接打开命令行

默认快捷键 `Ctrl+Shift+T`。

在windows下默认会打开Windows PowerShell，那界面简直丑到不行好吗！！

根据上面的经验同样找到`preference–>package Settings–>Terminal–>Terminal Settings-users`：进行下面的设置：

```json
{
    "terminal": "F:\\Program Files\\cmder\\Cmder.exe",
    "parameters": ["/START", "%CWD%"]
}
```

### 在sublime下运行python程序

sublime 自带运行 python 程序功能，使用快捷键  `ctrl + B` 即可。

更美观的界面或者进入命令行交互模式还需要插件的支持，这里推荐 `sublimeREPL` 插件

在你写好的python文件的界面里(这点需要注意)，点击上方菜单栏的`tools`->`sublimeREPL`->`python`->`python run current file`，即可交互输入

**使用快捷键运行程序**

在 `preferences`--> `key binding`--> `user` 中输入以下内容:

```json
{ "keys": ["f5"], "caption": "Python - RUN current file",
    "command": "repl_open", "args":
    {
      "type": "subprocess",
      "encoding": "utf8",
      "cmd": ["python", "-u", "$file_basename"],
      "cwd": "$file_path",
      "syntax": "Packages/Python/Python.tmLanguage",
      "external_id": "python",
      "extend_env": {"PYTHONIOENCODING": "utf-8"}
    }
}
```
