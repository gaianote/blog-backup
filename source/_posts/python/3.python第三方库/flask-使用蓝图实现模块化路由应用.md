title: flask 使用蓝图实现模块化路由应用
author: 李云鹏
date: 2018-09-21 02:49:46
tags:
---
## flask蓝图

将所有路由设定在入口文件中，在大型应用中会使项目混乱并难以维护。flask提供了蓝图`Blueprint`对象来解决这个问题。我们可以实例化一个蓝图对象，并在此文件中设定好路由，然后在入口文件中引入并注册此蓝图实例即可。




蓝图文件 admin.py，这个文件设定了admin路由并绑定了相应的方法

```python
from flask import Blueprint,render_template, request,jsonify
# 实例化一个蓝图
admin = Blueprint('admin',__name__)
# 页面路由，这里路由可以不指定前缀路径，最后在入口文件指定
@admin.route("/login")
def login():
    return render_template('login.html')
@admin.route("/regist")
def register():
    return render_template('register.html')
```
入口文件：

```python
from flask import Flask, jsonify, render_template, request
# 1.引入蓝图文件
from admin import admin
app = Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template('index.html')

# 2.注册蓝图
app.register_blueprint(admin,url_prefix='/admin')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 80,debug = True)
```

程序启动后，访问`127.0.0.1/admin/login`和`127.0.0.1/admin/register`便可以访问到在蓝图中的相应页面