---
title: grep使用说明
date: 2019-06-26 15:14:37
tags: linux
---

grep的正则表达式生效，需要`''` 括起来。

```bash                             
# zfs list | grep  '/shares/.*/' | wc -l 
132                                      
# zfs list | grep  /shares/.*/ | wc -l   
0   
```