---
title: python变量作用域
date: 2018-06-12 15:28:10
tags: python
---

## python作用域

Python的作用域一共有4中，分别是：


* L （Local） 局部作用域
* E （Enclosing） 闭包函数外的函数中
* G （Global） 全局作用域
* B （Built-in） 内建作用域

以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

局部作用域中的变量，无法改变全局作用域变量的值。

Python除了def/class/lambda 外，其他如: if/elif/else/ try/except for/while并不能改变其作用域。定义在他们之内的变量，外部还是可以访问。

```python
>>> if True:
...     a = 'I am A'
...
>>> a
'I am A'
# 定义在if语言中的变量a，外部还是可以访问的。
# 但是需要注意如果if被 def/class/lambda 包裹，在内部赋值，就变成了此 函数/类/lambda 的局部作用域。
```

在 def/class/lambda内进行赋值，就变成了其局部的作用域，局部作用域会覆盖全局作用域，但不会影响全局作用域。

```python
g = 1  #全局的
def fun():
    g = 2 #局部的
    return g

print fun()
# 结果为2
print g
# 结果为1
```

但是要注意，有时候想在函数内部引用全局的变量，疏忽了就会出现错误，比如：

```python
#file1.py
var = 1
def fun():
    print var
    var = 200
print fun()

#file2.py
var = 1
def fun():
    var = var + 1
    return var
print fun()

# 这两个函数都会报错UnboundLocalError: local variable 'var' referenced before assignment
```

在未被赋值之前引用的错误！为什么？因为在函数的内部，解释器探测到var被重新赋值了，所以var成为了局部变量，但是在没有被赋值之前就想使用var，便会出现这个错误。解决的方法是在函数内部添加 globals var 但运行函数后全局的var也会被修改。

## locals() 和 globals()

### globals()

global 和 globals() 是不同的，global 是关键字用来声明一个局部变量为全局变量。globals() 和 locals() 提供了基于字典的访问全局和局部变量的方式

比如：如果函数f1内需要定义一个局部变量，名字另一个函数f2相同，但又要在函数f1内引用这个函数f2。

```python
def f2():
    pass

def f1():
    f2 = 'Just a String'
    f3 = globals()['f2']
    print(f2)
    return type(f3)

print f2()
# Just a String
# <type 'function'>
```

### locals()

如果你使用过Python的Web框架，那么你一定经历过需要把一个视图函数内很多的局部变量传递给模板引擎，然后作用在HTML上。虽然你可以有一些更聪明的做法，还你是仍想一次传递很多变量。先不用了解这些语法是怎么来的，用做什么，只需要大致了解locals()是什么。
可以看到，locals()把局部变量都给打包一起扔去了。

```python
@app.route('/')
def view():
    user = User.query.all()
    article = Article.query.all()
    ip = request.environ.get('HTTP_X_REAL_IP',         request.remote_addr)
    s = 'Just a String'
    return render_template('index.html', user=user,
            article = article, ip=ip, s=s)
    # 等价于 return render_template('index.html', **locals())
```

## 参考资料

(Python 变量作用域)[https://blog.csdn.net/cc7756789w/article/details/46635383]