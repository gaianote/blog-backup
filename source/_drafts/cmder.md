## 解决 `ls` 中文显示乱码问题:

打开 `setting` - `Startup` - `Environment` 添加 `set LANG=zh_CN.UTF-8`

## Cmder 设置默认打开目录，并以 bash 模式开启

选择Startup-Task，修改{cmd::Cmder}项，把:

```
cmd /k "%ConEmuDir%\..\init.bat"  -new_console:d:%USERPROFILE%
```

修改成

```
cmd /k "%ConEmuDir%\..\init.bat"  -new_console:d:D:\ & bash
```

`D:\` 表示你希望其默认开启的位置

`& bash` 表示默认以 bash 模式打开程序

