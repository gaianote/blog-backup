---
title: nodejs得到本机ip
date: 2017-05-10 14:52:14
tags:
---

通过第三方模块[node-ip](https://github.com/indutny/node-ip)可以快速的得到本机ip

**安装**

```bash
npm install ip
```

**使用**

```javascript
var ip = require('ip');
ip.address()
```
