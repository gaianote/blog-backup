---
title: git常见问题解决方案
created: '2019-04-12T16:43:13.978Z'
modified: '2019-04-12T16:51:28.240Z'
---

# git常见问题解决方案

## 查看并恢复已删除的某个文件

```
# 1. 获得所有的已删除的文件
$ git log --diff-filter=D --summary
# 2. 恢复删除的文件,$commit为文件被删除的提交hash，比如2682452
$ git checkout $commit~1 path/to/deleted_file
```
示例：

```bash
$ git log --diff-filter=D --summary

commit 2682452a0ae587480b4c96a4f9d5045d371a0e04 (HEAD -> master)
Author: gaianote <gaianote@163.com>
Date:   Sat Apr 13 00:28:12 2019 +0800

    3

 delete mode 100644 test.py

$ git checkout 268245~1 test.py
```
