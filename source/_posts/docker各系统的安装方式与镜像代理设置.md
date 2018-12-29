title: docker各系统的安装方式与镜像代理设置
author: 李云鹏
date: 2018-12-28 17:10:26
tags:
---
## centos

### 安装docker

```bash
$ yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
$ curl -fsSL get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh --mirror Aliyun
```
### centos7为docker设置代理

```bash
# 创建目录
mkdir /etc/systemd/system/docker.service.d
# 创建文件
touch /etc/systemd/system/docker.service.d/http-proxy.conf
# 配置http-proxy.conf文件增加以下内容
[Service]
Environment="HTTP_PROXY=http://192.168.71.60:1080"
# daemon重新reload 并重启docker
systemctl daemon-reload
systemctl restart docker
# 检查变量是否加载
systemctl show docker --property Environment
```