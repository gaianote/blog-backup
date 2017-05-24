## 解决中文显示乱码问题:

打开 `setting` - `Startup` - `Environment` 添加 `set LANG=zh_CN.UTF-8`

## 为 Cmder 设置默认打开目录，并以 bash 模式开启

选择Startup-Task，修改 `{cmd::Cmder}` 项，把:

```
cmd /k "%ConEmuDir%\..\init.bat"  -new_console:d:%USERPROFILE%
```

修改成

```
cmd /k "%ConEmuDir%\..\init.bat"  -new_console:d:D:\ & bash
```
其中

- `D:\` 表示你希望其默认开启的位置

- `& bash` 表示默认以 bash 模式打开程序

## 配置其在 win + r 中打开

把根目录加到系统环境的path变量中即可

## 取消关闭提示框

当我们每次关闭 `Cmder` 时都会弹出提示框提示 Confirm closing console? ，只需要在 `Setting` -> `Main` -> `Confirm` -> `Close confirmations` 中取消 `When running process was detected` 前面选中状态，就可以关闭提示框的弹出。