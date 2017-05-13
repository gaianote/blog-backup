# squid 高匿设置

## 透明代理、匿名代理、混淆代理、高匿代理有什么区别

这4种代理，主要是在代理服务器端的配置不同，导致其向目标地址发送请求时，`REMOTE_ADDR`， `HTTP_VIA`，`HTTP_X_FORWARDED_FOR`三个变量不同。

1、透明代理(Transparent Proxy)

```
REMOTE_ADDR = Proxy IP
HTTP_VIA = Proxy IP
HTTP_X_FORWARDED_FOR = Your IP
```

透明代理虽然可以直接“隐藏”你的IP地址，但是还是可以从HTTP_X_FORWARDED_FOR来查到你是谁。

2、匿名代理(Anonymous Proxy)

```
REMOTE_ADDR = proxy IP
HTTP_VIA = proxy IP
HTTP_X_FORWARDED_FOR = proxy IP
```

匿名代理比透明代理进步了一点：别人只能知道你用了代理，无法知道你是谁。

3、混淆代理(Distorting Proxies)

```
REMOTE_ADDR = Proxy IP
HTTP_VIA = Proxy IP
HTTP_X_FORWARDED_FOR = Random IP address
```

如上，与匿名代理相同，如果使用了混淆代理，别人还是能知道你在用代理，但是会得到一个假的IP地址，伪装的更逼真

4、高匿代理(Elite proxy或High Anonymity Proxy)

```
REMOTE_ADDR = Proxy IP
HTTP_VIA = not determined
HTTP_X_FORWARDED_FOR = not determined
```

可以看出来，高匿代理让别人根本无法发现你是在用代理，所以是最好的选择。

## 环境

```
操作系统：CentOS 6.8
Squid版本：squid-3.1.10-20.el6_5.3.x86_64
```

## 配置（vim /etc/squid/squid.conf，添加以下内容）

**配置文件说明**

```
http_port　3128　　　　　　# 设置监听的IP与端口号

cache_mem 64 MB　　　　　　# 额外提供给squid使用的内存，squid的内存总占用为 X * 10+15+“cache_mem”，其中X为squid的cache占用的容量（以GB为单位），
　　　　　　　　　　 　　　　# 比如下面的cache大小是100M，即0.1GB，则内存总占用为0.1*10+15+64=80M，推荐大小为物理内存的1/3-1/2或更多。
maximum_object_size 4 MB 　　# 设置squid磁盘缓存最大文件，超过4M的文件不保存到硬盘

minimum_object_size 0 KB 　　# 设置squid磁盘缓存最小文件

maximum_object_size_in_memory 4096 KB 　　# 设置squid内存缓存最大文件，超过4M的文件不保存到内存

cache_dir ufs /var/spool/squid 100 16 256 　　# 定义squid的cache存放路径 、cache目录容量（单位M）、一级缓存目录数量、二级缓存目录数量

logformat combined %&gt;a %ui %un [%tl] "%rm %ru HTTP/%rv" %Hs %<st "%{Referer}>h" "%{User-Agent}&gt;h" %Ss:%Sh        # log文件日志格式

access_log /var/log/squid/access.log combined　　# log文件存放路径和日志格式

cache_log /var/log/squid/cache.log 　　# 设置缓存日志

logfile_rotate 60　　 # log轮循 60天

cache_swap_high 95　　# cache目录使用量大于95%时，开始清理旧的cache

cache_swap_low 90　　 # cache目录清理到90%时停止。

acl localnet src 192.168.1.0/24　　# 定义本地网段

http_access allow localnet　　# 允许本地网段使用

http_access deny all　　# 拒绝所有

visible_hostname squid.david.dev　　# 主机名

cache_mgr mchina_tang@qq.com　　# 管理员邮箱
```


**需要添加的内容**

```
http_port 3128　　　　　　　　　　　　　　　　　　#端口
cache_mem 64 MB
maximum_object_size 4 MB
cache_dir ufs /var/spool/squid 100 16 256
access_log /var/log/squid/access.log
acl localnet src 10.60.20.0/24　　　　　　    #定义本地网段
http_access allow localnet
http_access deny all
visible_hostname myserver01.lo              #squid主机名
cache_mgr test@qq.com                       #邮箱
#以下是高匿的设置
request_header_access Via deny all
request_header_access X-Forwarded-For deny all
```
