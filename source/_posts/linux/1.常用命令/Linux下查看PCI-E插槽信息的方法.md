---
title: Linux下查看PCI-E插槽信息的方法
date: 2019-03-22 12:12:33
tags: linux
---


在 Linux 下要如何得知 PCI-E Bus 使用的是 Gen(Generation) 1 還是 Gen2 還是新一代的 Gen 3 雖然使用 #lspci 只要可以看到目前系統所有的裝置.但是好像看不到 PCI-E Bus 所採用的是哪一代的 PCI-E.

```bash
[root@benjr ~]# lspci
00:00.0 Class 0604: 16c3:abcd
00:01.0 Class 0604: 16c3:abcd
00:02.0 Class 0604: 16c3:abcd
00:03.0 Class 0604: 16c3:abcd
01:00.0 Class 0604: 10b5:8716
0d:00.0 Class 0c04: 1077:2971
0d:00.1 Class 0c04: 1077:2971
0d:00.2 Class 0c04: 1077:2971
0d:00.3 Class 0c04: 1077:2971
```

如果有裝置是 unknown 的,需要更新 `/usr/share/hwdata/pci.ids` 請參考更新方式 http://benjr.tw/node/88

首先我們先來複習一下 PCI-E bus 的速度上限.

### PCI Express 1.1
使用兩對低電壓的差位訊號排線（low-voltage differential signaling pairs），分別各跑2.5GBit/s速度,下面的速度是以單對的速度而言. x1 有兩對 2.5 G x 2 = 5Gbps 的頻寬.

```
x1  2.5Gbps(20% overhead - PCI-e 在每八個位元的資料串上用十位元來加以編碼)   2Gbps (250 MB/sec)
x4  10Gbps  8Gbps (1 GB/sec)
x8  20Gbps  16Gbps (2GB/sec)
x16 40Gbps 32Gbps (4GB/sec)
```
### PCI Express 2.0
PCI-SIG 的 PCI Express 2.0規格，新版每條Lane的單向頻寬從2.5Gbps倍增到5Gbps.

```
x1  5Gbps(20% overhead-PCIe並且在每八個位元的資料串上用十位元來加以編碼)   4Gbps (500 MB/sec)
(5G*0.8)Mb/8=500MB
x4  20Gbps  16Gbps (2 GB/sec)
x8  40Gbps  32Gbps (4 GB/sec)
x16 80Gbps 64Gbps (8 GB/sec)
```

我的系統上有一張 Qlogic Chipset 為 2432 的 4G Fiber Channel HBA,要如何得知目前系統的 PCI-E Bus 的速度呢!!首先要查出這張 HBA 的裝置名稱.

```bash
[root@benjr ~]# lspci -n
00:00.0 0600: 8086:29f0 (rev 01)
00:01.0 0604: 8086:29f1 (rev 01)
00:1a.0 0c03: 8086:2937 (rev 02)
00:1a.1 0c03: 8086:2938 (rev 02)
00:1a.2 0c03: 8086:2939 (rev 02)
00:1a.7 0c03: 8086:293c (rev 02)
00:1c.0 0604: 8086:2948 (rev 02)
00:1c.1 0604: 8086:294a (rev 02)
00:1c.2 0604: 8086:2940 (rev 02)
00:1d.0 0c03: 8086:2934 (rev 02)
00:1d.1 0c03: 8086:2935 (rev 02)
00:1d.2 0c03: 8086:2936 (rev 02)
00:1d.7 0c03: 8086:293a (rev 02)
00:1e.0 0604: 8086:244e (rev 92)
00:1f.0 0601: 8086:2916 (rev 02)
00:1f.2 0106: 8086:2922 (rev 02)
00:1f.3 0c05: 8086:2930 (rev 02)
03:00.0 0200: 14e4:165a
04:03.0 0300: 1002:515e (rev 02)
09:00.0 0c04: 1077:2432 (rev 03)
09:00.1 0c04: 1077:2432 (rev 03)
0c:00.0 0100: 1000:0056 (rev 02)
```

可以看到目前 Qlogic 2432 的 PCI 名稱以及裝置名稱為 09:00.0 0c04: 1077:2432 (rev 03) 先來看看這些數字所代表的意義.
前面的 3 個數字 "09:00.0" 是各代表什麼意思.

在 PCI 的裝置使用三個編號用來當作識別值,個別為:
1. 匯流排(bus number)
2. 裝置(device number)
3. 功能(function number)

所以剛剛的 09:00.0 就是 bus number = 09 ,device number = 00 function = 0 .

這3個編號會組合成一個 16-bits 的識別碼,

匯流排(bus number) 8bits 2^8 至多可連接 256 個匯流排(0 to ff),  
裝置(device number) 5bits 2^5 至多可接 32 種裝置(0 to 1f) 以及  
功能(function number) 3bits 2^3 至多每種裝置可有 8 項功能(0 to 7)

關於更多 #lspci 的資訊請參考 http://benjr.tw/node/543

不過在 Linux 使用 Class ID + Vendor ID + Device ID  來代表裝置,如剛剛的  0c04: 1077:2432 所代表裝置名稱為 (Class ID = 0c04 ,Vendor ID = 1077,Device ID =2432) .

* 0c04 : class 0c04 表示是 "Fiber Channel controller"
* 1077 : vendor ID 1077 製造廠商 "Qlogic Corp"
* 2432 : device ID 2432 產品名稱 "ISP2432-based 4Gb Fiber Channel to PCI Express HBA"

你問我怎麼知道 ID 與名稱是怎麼對應的很簡單直接參考 /usr/share/hwdata/pci.ids 檔案即可.

### 获取PCI-Express速度

接下來透過指令 #lspci -n -d 1077:2432 -vvv |grep -i width 就可以得知 PCI-Express 的速度了.

```bash
[root@benjr ~]# /usr/sbin/lspci -d 1077:2971 -vv grep -i width

LnkCap: Port #0, Speed 2.5GT/s, Width x4, ASPM L0s, Latency L0 <4us, L1 unlimited
LnkSta: Speed 2.5GT/s, Width x1, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
LnkCap: Port #0, Speed 2.5GT/s, Width x4, ASPM L0s, Latency L0 <4us, L1 unlimited
LnkSta: Speed 2.5GT/s, Width x1, TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
```

* **LnkSta :** 目前系統所提供的速度 PCI-Express 1.0 ( 2.5G ) ,如果是 PCI-Express 2.0 那速度是 5G
* **LnkCap :** 裝置目前所採用的速度.

LnkSta 和 LnkCap 這兩個速度有可能不一樣 ,系統所提供的是 PCI Express 是 2.0 但裝置還是使用 1.0 的.
