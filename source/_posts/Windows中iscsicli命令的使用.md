title: Windows中iscsicli命令的使用
author: 李云鹏
date: 2018-11-01 09:30:50
tags:
---
## 设置msiscsi服务的启动状态

```
sc config msiscsi start= auto

net start msiscsi
```

## 使用iscsicli命令连接Target

```
iscsicli QAddTargetPortal <Portal IP Address>

iscsicli ListTargets
iscsicli QloginTarget <target_iqn>
```

## 示例

```
C:\Users\user>iscsicli QAddTargetPortal 192.168.71.200
Microsoft iSCSI 发起程序版本 10.0 內部版本 17134

操作成功完成。

C:\Users\user>iscsicli ListTargets
Microsoft iSCSI 发起程序版本 10.0 內部版本 17134

目标列表:
    iqn.2001-06.cn.com.lee:disk-array-000d62ac0:dev5.ctr1
操作成功完成。

C:\Users\user>iscsicli QloginTarget iqn.2001-06.cn.com.lee:disk-array-000d62ac0:dev5.ctr1
Microsoft iSCSI 发起程序版本 10.0 內部版本 17134

会话 ID 是 0xffffd001de85b010-0x400001370000001e
连接 ID 是 0xffffd001de85b010-0xb0
操作成功完成。
```