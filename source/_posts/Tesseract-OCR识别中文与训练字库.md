---
title: Tesseract-OCR识别中文与训练字库
date: 2017-04-23 21:19:05
tags: nodejs
---

## 准备工作

1. 下载最新版Tesseract-OCR引擎，安装时勾选 chi_sim 字库以及path 加入到系统变量
2. 下载jTessBoxEditor，这个是用来训练字库的。
3. 下载java虚拟机用以支持jTessBoxEditor

## 开始



```bash
# 生成box文件
tesseract langyp.fontyp.exp0.tif langyp.fontyp.exp0 -l eng -psm 7 batch.nochop makebox
```

2. 使用jTessBoxEditor进行编辑

```bash
# 生成font_properties
echo fontyp 0 0 0 0 0 >font_properties
# 生成训练文件
tesseract langyp.fontyp.exp0.tif langyp.fontyp.exp0 -l eng -psm 7 nobatch box.train
# 生成字符集文件
unicharset_extractor langyp.fontyp.exp0.box
# 生成shape文件
shapeclustering -F font_properties -U unicharset -O langyp.unicharset langyp.fontyp.exp0.tr
# 生成聚集字符特征文件
mftraining -F font_properties -U unicharset -O langyp.unicharset langyp.fontyp.exp0.tr
# 生成字符正常化特征文件
cntraining langyp.fontyp.exp0.tr
# 更名
rename normproto fontyp.normproto
rename inttemp fontyp.inttemp
rename pffmtable fontyp.pffmtable
rename unicharset fontyp.unicharset
rename shapetable fontyp.shapetable
# 合并训练文件
combine_tessdata fontyp.
```

将fontyp.traineddata拷贝到tesseract安装目录的tessdata目录下。


参考链接：
[Tesseract-OCR识别中文与训练字库](http://www.cnblogs.com/wzben/p/5930538.html)
[利用jTessBoxEditor工具进行Tesseract3.02.02样本训练，提高验证码识别率](http://www.tuicool.com/articles/zY7jQbM)
I dont know why the Tesseract-OCR is good