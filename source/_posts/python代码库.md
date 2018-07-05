---
title: python代码库
date: 2018-07-02 15:35:37
tags:
---

## 文件IO

### 列出一个文件夹内的文件的名称和文件路径

```python
import os
from collections import namedtuple


def get_file_list(dir_path = '.',file_types = '.*'):
    """
    dir_path 参数接受一个文件路径字符串
    file_types 接受诸如'.py'的字符串或者[.py,.md]的数组
    return 返回一个包含nametuple的列表 nametuple包含文件名,文件绝对路径和文件类型nametuple
    """
    File_data = namedtuple('File_data',['file_name','file_path','file_type'])
    # result_list = [(filename,filepath)]
    result_list = []
    print(dir_path)
    # 得到绝对路径
    dir_path = os.path.abspath(dir_path)
    print(dir_path)
    # 得到文件的文件名，绝对路径，文件类型
    file_data_list = [File_data(file_name,os.path.join(dir_path,file_name),os.path.splitext(file_name)[1]) for file_name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,file_name))]
    # 如果没有传入file_type,默认传入
    if file_types == '.*':
        return file_data_list
    # 筛选出符合条件的文件夹 file_data = (file_name,file_path,file_type)
    # '.gitignore 的filetype为'',特殊处理''
    file_data_list = [File_data(file_name,file_path,file_type) for file_name,file_path,file_type in file_data_list if file_type and file_type in file_types]
    return file_data_list
```

## 数据库

### 封装sqlite3常用方法,使其调用简单

```python
import sqlite3
from functools import wraps

def cursor(func):
    @wraps(func)
    def wrapper(self,*args, **kwargs):
        self.conn = sqlite3.connect(self.tablebase)
        self.cursor = self.conn.cursor()
        result = func(self,*args, **kwargs)
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
        return result
    return wrapper

class SQlite():
    def __init__(self,tablebase):
        self.tablebase = tablebase

    @cursor
    def create_table(self,tablename,**kw):
      header = ','.join(['{0} {1}'.format(key,kw[key]) for key in kw.keys()])
      sql = 'CREATE TABLE {tablename}({header})'.format(tablename = tablename,header = header)
      print(sql)
      self.cursor.execute(sql)

    @cursor
    def insert(self,tablename,**kw):
        header = ','.join(kw.keys())
        value = ','.join(["'{0}'".format(key) if isinstance(key,str) else str(key) for key in kw.values()])
        sql = "INSERT INTO {tablename} ({header}) VALUES ({value})".format(tablename = tablename,header = header,value = value)
        self.cursor.execute(sql)
        print(sql)

    def _select(self,tablename,*keys,where = ''):
        headers = ','.join(keys)
        sql = "SELECT {0} from {1} {2}".format(headers,tablename,where)
        result = self.cursor.execute(sql)
        return result
    @cursor
    def update(self):
        self.cursor.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    @cursor
    def delete(self):
        self.cursor.execute("DELETE from COMPANY where ID=2;")
    @cursor
    def fetchall(self,tablename,*keys,where = ''):
        result = self._select(tablename,*keys,where = where)
        return result.fetchall()
    @cursor
    def fetchone(self,tablename,*keys,where = ''):
        result = self._select(tablename,*keys,where = where)
        return result.fetchone()
```
