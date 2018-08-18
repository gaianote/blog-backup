---
title: python实现windows系统下自动拨号
date: 2017-04-23 22:07:42
tags: python
---

```python
class Adsl(object):
  def __init__(self):
    # 分别填写adsl名称，用户名与密码，dsl名称一般为宽带连接
    self.name = "宽带连接"
    self.username = 'adsl_uname'
    self.password = 'adsl_upwd'
  def connect(self):
    cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
    os.system(cmd_str)
    time.sleep(5)
  def disconnect(self):
    cmd_str = "rasdial %s /disconnect" % self.name
    os.system(cmd_str)
    time.sleep(5)
  def reconnect(self):
    self.disconnect()
    self.connect()
```

