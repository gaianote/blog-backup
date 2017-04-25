---
title: 入门学习mysql数据库
date: 2017-04-25 21:01:05
tags: mysql
---

## 安装mysql

对于mysql，我们除了在官网下载安装包以外，还可以使用XAMPP建站集成环境进行安装，安装完成后打开MySQL模块即可使用

## 在命令行使用mysql

### 添加环境变量

找到mysql的bin文件夹，将其添加到环境变量路径，方便在cmd中使用mysql

添加方法：使用win自带的搜索功能，搜索环境变量，进入编辑环境变量后选择**用户环境变量**，选择PATH后编辑，选择新建，输入mysql的bin路径，比如我的是 E:\xampp\mysql\bin

编辑PATH完成后，cmd重启生效

### 命令行的基本操作

**连接数据库**

```bash
$ mysql -h localhost -u root -p
```

```
password
```

要求输入password时，假如未设定，直接回车即可

**显示用户名下的所有数据库**

```bash
$ show databases;
```

注意sql语句要求以';'结尾，执行命令后，会输出形如下列的表格

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mynote             |
| mysql              |
| performance_schema |
| phpmyadmin         |
+--------------------+
```

**进入某个数据库**

```bash
$ use databasename
```

**退出mysql**

```bash
$ exit;
```

