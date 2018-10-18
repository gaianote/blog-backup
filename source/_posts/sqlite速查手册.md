---
title: sqlite速查手册
date: 2017-04-23 22:07:42
tags: python
---

```python
# 返回数据表的最大行数
sql = 'SELECT count(*) FROM table_name;'
# 选择某列最大或最小值,计算平均值与和
sql = 'SELECT max(coloumn) FROM table_name;'
sql = 'SELECT min(coloumn) FROM table_name;'
sql = 'SELECT avg(coloumn) FROM table_name;'
sql = 'SELECT sum(coloumn) FROM table_name;'

############ 操作数据库 ##############

# 得到所有的表名，使用fetchall
sql = 'select * from sqlite_master'

############ 操作数据表 ##############
# 获得所有列名
sql = "PRAGMA table_info(table_name)"
# 改变表名
sql = 'ALTER TABLE old_table_name RENAME new_table_name 新表名'
# 增加一列
sql = 'ALTER TABLE 表名 ADD COLUMN 列名 数据类型'
```