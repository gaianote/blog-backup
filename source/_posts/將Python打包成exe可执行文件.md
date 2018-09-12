title: 將Python打包成 exe可执行文件
author: 李云鹏
date: 2018-09-10 02:22:06
tags:
---

利用Python寫了一個小腳本想要傳給使用**Windows**但沒有裝Python的朋友執行，這時候就可以利用將檔案包裝成exe檔案，讓沒有Python的朋友也可以執行。本篇將介紹利用套件「PyInstaller」製作exe檔。

<!--more-->


## 安裝方法

```
# 安裝pyinstaller
pip install pyinstaller
# 安装依赖
pip install pywin32-ctypes
```

## 常用参数介绍

* **pyinstaller -h 來查看參數**
* -F 打包成一個exe文件
* -i 圖標路徑
* -w 使用視窗，無控制台
* -c 使用控制台，無視窗
* -D 創建一個目錄，包含exe以及其他一些依賴性文件

编译文件时，我们通常使用如下命令:

```
pyinstaller -F -w -i favo.ico main.py
```

## 静态文件

对于python所依赖的图片,`config.yaml`等静态文件，pyinstall不会自动打包，需要手动在`main.py`(所需要打包的入口文件)的相同目录中寻找`main.spec`，修改datas依赖，才可以自动打包到exe的相同目录下，然后执行即可

datas是一个数组，每个子项是一个tuple，其中tuple的第一个参数是你要打包的源路径，第二个参数是打包后的名字

```
# -*- mode: python -*-

block_cipher = None


a = Analysis(['ui.py'],
             pathex=['C:\\Users\\user\\Desktop\\resilio\\toyou\\code\\zeus_board_test'],
             binaries=[],
             datas=[('C:\\Users\\user\\Desktop\\resilio\\toyou\\code\\zeus_board_test\\images','images'),('C:\\Users\\user\\Desktop\\resilio\\toyou\\code\\zeus_board_test\\question.yaml','question.yaml')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
```

然后执行：

```
pyinstaller -F main.spec
```
## 示例

如下圖所示，我們編寫一個輸出 helow pyinstaller 的Python程式，並利用input()使程式可以暫時停在輸出畫面。

```
print('helow pyinstaller')
input('please wait:')
```

编译python为exe,编译过程中会自动安装相关依赖

```bash
pyinstaller -F hello.py
```

编译过程中会产生如下输出:

```
...
6942 INFO: checking PYZ
6944 INFO: Building because toc changed
6944 INFO: Building PYZ (ZlibArchive) C:\Users\user\Desktop\test\build\test\PYZ-00.pyz
7559 INFO: Building PYZ (ZlibArchive) C:\Users\user\Desktop\test\build\test\PYZ-00.pyz completed successfully.
7568 INFO: checking PKG
7569 INFO: Building because toc changed
7569 INFO: Building PKG (CArchive) PKG-00.pkg
9407 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
9409 INFO: Bootloader c:\users\user\appdata\local\programs\python\python36\lib\site-packages\PyInstaller\bootloader\Windows-64bit\run.exe9409 INFO: checking EXE
9411 INFO: Building because toc changed
9411 INFO: Building EXE from EXE-00.toc
9412 INFO: Appending archive to EXE C:\Users\user\Desktop\test\dist\test.exe
9455 INFO: Building EXE from EXE-00.toc completed successfully.

```

### 通过输出可以看出pyinstaller进行了如下操作:

* 會先建立一個 hello.spec
* 建立「build」 資料夾
* 建立 log紀錄檔與工作檔案於資料夾 build 中
* 建立 「dist 」資料夾
* 建立執行檔(.exe)在 「dist」 資料夾



### 注意事項

執行檔案可在win8/win10,64位元的電腦運行，但win7 x64和其餘所有32位失敗，會提示不兼容，若要能32位元與64位元皆可運行，就要在Python 32位元的環境下編譯PyInstaller打包exe，才能在32位元與64位元成功。