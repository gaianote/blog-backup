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