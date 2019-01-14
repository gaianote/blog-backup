title: 为linux增加虚拟内存swap
author: 李云鹏
date: 2019-01-14 06:05:10
tags:
---
使用`hexo g`时，遇到了因vps内存不足而被killed，通过查阅资料，通过以下方法解决了问题:

```bash
free -m 
dd if=/dev/zero of=/swap bs=4096 count=1572864
mkswap /swap
swapon /swap
echo "LABEL=SWAP-sda /swap swap swap defaults 0 0" >> /etc/fstab
```

如果遇到`swapon`命令报错，可以尝试`swapoff -a`, 意思是关闭所有swap,然后重新执行`swapon /swap`即可