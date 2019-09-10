---
title: python操作文件路径和目录
date: 2018-06-11 17:04:01
tags: python
---

## python获取文件路径 `os.path.abspath(__file__)`

在python文件中使用路径,应该使用`os.path.abspath(__file__)`。永远不要使用`os.path.abspath(.)`或者`os.getpwd()`,因为后者具有不确定性。

* `os.path.abspath(.)`和`os.getcwd()`是等价的，它们表示当前的工作路径，可以被os.chdir()改变
* `os.path.abspath(__file__)`表示当前文件所在路径

它们返回的都是绝对路径。

<!--more-->

例1：

```python
>>> os.path.abspath('.')
'/mnt/c/Users/user/gaianote.github.io'
>>> os.chdir('source')
>>> os.getcwd()
'/mnt/c/Users/user/gaianote.github.io/source'
>>> os.path.abspath('.')
'/mnt/c/Users/user/gaianote.github.io/source'
```

例2:

希望得到工程的根目录BASE_PATH：

```
BASE_PATH
|
|-lib
    |-config.py # 设置文件，定义了path路径
|-main.py # 入口文件
```

在config.py中书写`os.path.abspath(__file__)`,和 `os.path.abspath('.')`,在main.py中执行，第一个得到了config的路径，第二个得到了BASE_PATH的路径

## 路径拼接

**不要用abspath('.')，不要用字符串拼接**

```python
path =os.path.abspath（ os.path.abspath('..') + '\\driver\\chromedriver.exe' ）
```

**正确方法,使用os.path.join进行拼接**

```python
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# BASE_PATH还可以这么写
BASE_PATH = os.path.abspath('.')
path =os.path.join(BASE_PATH,'driver','chromedriver.exe')
```


## os 模块

Python 的 os 模块封装了常见的文件和目录操作，本文只列出部分常用的方法，更多的方法可以查看官方文档。

### 下面是部分常见的用法：

|       方法       |                                         说明                                         |
|------------------|--------------------------------------------------------------------------------------|
| os.name          | 指示你正在使用的工作平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posi |
| os.getcwd()      | 得到当前工作目录，即当前python脚本工作的目录路径。                                   |
| os.listdir()     | 返回指定目录下的所有**文件**和**目录名**                                             |
| os.stat(file)    | 获取文件属性                                                                         |
| os.mkdir()       | 创建目录                                                                             |
| os.rmdir()       | 删除空目录或文件                                                                     |
| os.system(shell) | 运行操作系统命令行                                                                   |
| os.rename        | 重命名                                                                               |
| os.remove        | 删除文件                                                                             |
| os.getcwd        | 获取当前工作路径                                                                     |
| os.walk          | 遍历目录                                                                             |
| os.path.join     | 连接目录与文件名                                                                     |
| os.path.split    | 分割文件名与目录                                                                     |
| os.path.abspath  | 获取绝对路径                                                                         |
| os.path.dirname  | 获取路径(指包含文件的目录)                                                           |
| os.path.basename | 获取文件名或文件夹名                                                                 |
| os.path.splitext | 分离文件名与扩展名                                                                   |
| os.path.isfile   | 判断给出的路径是否是一个文件                                                         |
| os.path.isdir    | 判断给出的路径是否是一个目录                                                         |
| os.path.exits()  | 判断一个路径目录或者文件是否存在                                                     |




## 标准库shutil

### shutil.move(src,dst)

```python
shutil.move('tmp/20180128/new','tmp/20180128/test')   # 移动文件, 重命名等
```

### shutil.copytree(src, dst, symlinks=False, ignore=None)

```python
shutil.copytree("b","c")    # 递归复制。复制一个文件夹及其内容到另一个文件夹，另一个文件夹已存在时报错
#(复制一个文件夹路径，把左边的文件夹路径替换为右边的，而不是作为右边的子文件夹)
#复制过程中跳过后缀名为参数名的文件
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.py'))
```

### shutil.rmtree(path, ignore_errors=False, onerror=None)

```python
shutil.rmtree('tmp/a')   # 递归删除目录树.删除一个文件夹(包括这个文件夹)及其内容(文件夹不存在报错)
```

### shutil.get_archive_formats()

```python
shutil.get_archive_formats()    # 返回支持的 压缩格式列表, 如 [(name,desc),('tar','uncompressed tar file')],
```
### shutil.make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None)

```python
shutil.make_archive('tmp/a/new2','zip',root_dir='/tmp/a')   # 创建压缩文件,
base_name : 压缩包的文件名, 也可以使压缩包的路径.
format : 压缩种类
root_dir : 要压缩的文件夹路径, 默认当前目录
owner : 用户, 默认当前用户
group : 组, 默然当前组
```

### shutil.copy(src, dst)
```python
shutil.copy("a.txt","d.txt")   # 复制文件及权限,文件已存在则覆盖
```

### shutil.copyfileobj(fsrc, fdst, length=16384)
```python
shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))
# 将文件内容拷贝到另一个文件
```

### shutil.copyfile(src, dst)
```python
shutil.copyfile('f1.log', 'f2.log')  # 拷贝文件
```

### shutil.copymode(src, dst)

```python
shutil.copymode('f1.log', 'f2.log')     # 仅拷贝权限,内容,用户,组不变
```

### shutil.copystat(src, dst)
```python
shutil.copystat('f1.log', 'f2.log')     # 仅拷贝状态信息
```
### shutil.copy2(src, dst)

```python
shutil.copy2('f1.log', 'f2.log')     # 拷贝文件和状态信息
```

## 环境变量

在操作系统中定义的环境变量，全部保存在os.environ这个变量中

```python
os.environ
os.environ.get('PATH')
```

## 操作文件和目录

**查看当前目录的绝对路径**

```python
dir = os.path.abspath('.')
```

在当前目录操作一个新目录newdir,首先需要得到这个目录的绝对路径


```python
newdir = os.path.join(dir, 'newdir')
```

路径操作不应使用字符串拼接，而应该使用os.path模块;因为不同操作系统的路径分隔符是不同的

**创建新目录**

```python
os.mkdir(newdir)
```

**删除目录**

```python
os.rmdir(newdir)
```

**得到当前目录下所有的文件夹**

```python
[x for x in os.listdir('.') if os.path.isdir(x)]
```

**得到当前目录下所有的.py文件**

```python
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
```