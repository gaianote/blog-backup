{}
date: 2018-09-20 03:21:57
---

---
AutoHotkey是一个windows下的开源、免费、自动化软件工具。它由最初旨在提供键盘快捷键的脚本语言驱动(称为：热键)，随着时间的推移演变成一个完整的脚本语言。但你不需要把它想得太深，你只需要知道它可以简化你的重复性工作，一键自动化启动或运行程序等等；以此提高我们的工作效率，改善生活品质；通过按键映射，鼠标模拟，定义宏等。

## 下载安装AutoHotkey

进入[AutoHotkey官网](http://www.autohotkey.com/)，点击“download”下载即可将AutoHotkey保存到本地磁盘。接着双击点击安装就可以了。

## 建立AutoHotkey脚本

安装完成后默认会在系统盘的“本地文档”下创建一个”AutoHotkey.ahk”脚本，双击以后我们会看到任务栏右下角有个图标，就表示它在运行了。如果你选择绿色安装方式，点击.ahk脚本后，运行方式选择AutoHotkeyU64.exe即可。我们在里面写入相应的映射代码然后右击选择”reload this script“执行它就可以开始使用AutoHotkey里面设置好的功能了。

如果我们想在其他地方放置脚本怎么办呢？很简单，只要新建一个文本文档，将其后缀名改为.ahk然后执行它就行了。所以，在同一台电脑中，你甚至可以存放多个脚本。当用不到该脚本了只需要，鼠标移到该图标处，右键选择exit即可，很是方便。

为了方便修改该脚本，你可以将其放置于你觉得方便的位置，丝毫不影响，双击可运行之。我们还可以为该脚本设置开机自启动，只需要将该脚本生成一个“快捷方式”，然后将此快捷方式放置到程序自启动文件夹之下即可,一般都在这儿:`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`

如此一开机，就可以使用脚本中所配置的功能，大为便捷。

这里简单说明下脚本中常用符号代表的含义：

## 简单实用的实例

```
# 号代表 Win 键；
! 号代表 Alt 键；
^ 号代表 Ctrl 键；
+ 号代表 shift 键；
:: 号(两个英文冒号)起分隔作用；
run，非常常用 的 AHK 命令之一;
; 号代表 注释后面一行内容；
```

run它的后面是要运行的程序完整路径（比如我的Sublime的完整路径是：D:\Program Files (x86)\Sublime Text 3\sublime_text.exe）或网址。为什么第一行代码只是写着“notepad”，没有写上完整路径？因为“notepad”是“运行”对话框中的命令之一。


## 常用功能实现

**激活/打开/隐藏程序**

```
#c::
IfWinNotExist ahk_class Chrome_WidgetWin_1
{
    Run chrome
    WinActivate
}
Else IfWinNotActive ahk_class Chrome_WidgetWin_1
{
    WinActivate
}
Else
{
    WinMinimize
}
Return
```

以上这段脚本可以做到，使得Chrome的各种状态灵活切换：Win+C,Chrome没打开状态时候 –> 打开；打开没激活状态时候 –> 激活；打开处在激活状态时候 —> 隐藏。


