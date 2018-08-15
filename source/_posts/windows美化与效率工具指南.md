---
title: windows美化与效率工具指南
date: 2018-08-13 17:20:41
tags:
    - windows
    - 软件
---

Apple 是一家标榜设计的公司，macOS 的桌面美学确实让包括我在内的很多人赞叹。当然，经过 Fluent Design 重新设计的 Windows 10 也相比之前的老一代 Windows 有着巨大的美学改善。进一步借助下面这些小工具，我找回了不输 macOS 的美观桌面。

<!--more-->

## 设计桌面

### ① [TranslucentTB](https://github.com/TranslucentTB/TranslucentTB/)：开源的任务栏透明工具&nbsp;

![img](/images/f6d49af9656b4692a4dff0ea015d6715.png)
美化桌面的步骤中，必不可少修改任务栏，改掉它不透明的生硬效果。有人会选择修改注册表，这不仅很危险，还只能将任务栏半透明化，而另外一些如 StarDock 的美化软件又很占内存。这个开源的 TranslucentTB 则不然，既小巧、不占内存、还可以将任务栏透明、半透明、模糊、或是直接显示纯色，可以说是功能全面了。**显示效果就像上图那样，能够完整的呈现我们的壁纸而不必担心任务栏挡掉一部分。**

TranslucentTB源码文件需要自己编译，所以直接[下载](https://github.com/TranslucentTB/TranslucentTB/releases)release版本即可

### ② [Rainmeter](https://www.rainmeter.net/)：Windows 桌面美化插件

对于深度美化 Windows 桌面的同学来说，Rainmeter 的重要性可想而知。在 Rainmeter 的 [官网](https://www.rainmeter.net/)、[官方用户社区](https://forum.rainmeter.net/)、和 [DeviantArt 设计站点](https://www.deviantart.com/rainmeter)，都有大量设计精美的 Rainmeter 插件，但是我也并不推荐将插件直接堆砌在桌面上，一团糟的样子不仅不美观，还占用了大量的系统资源。**我只小小利用了其桌面时钟、日期的显示。**

![img](/images/0f7320590e9440adb815e7518f4f6954.png)
我目前使用的 Rainmeter 主题在这里可以下载到 → [Rainmeter Elegance 2.0](https://www.deviantart.com/lilshizzy/art/Rainmeter-Elegance-2-244373054)

### ③ [Simple Desktops](http://simpledesktops.com/browse/)：壁纸提供站

美化桌面方面，壁纸可以说是重中之重。一张简单可爱的壁纸可以奠定整个工作的态度。在 Simple Desktops 里我总能找到可爱的壁纸。

![img](/images/8cd18ead307f48bc8b7a2c38382aa1f0.png)Simple Desktop
除此之外，无版权图片社区 [Unsplash](https://unsplash.com/)、免费图片社区 [Pixabay](https://pixabay.com/zh/)、甚至是必应每日壁纸等等都是优秀的壁纸来源。

### ④ 文件管理和日常清理的习惯

简洁的文件管理、不复杂凌乱的桌面和常清理的使用习惯自然会让你的 Windows 使用体验蒸蒸日上。💗

参考：《[每个人都应该学会正确管理文件](https://sspai.com/series/13)》（少数派付费教程）

## 系统工具

### ① [WoX](https://github.com/Wox-launcher/Wox)&nbsp;和 [Everything](https://www.voidtools.com/)：启动器工具

![img](/images/0548a8d950c247989c3e82b19df76240.png)Wox
WoX 是 Windows 上大名鼎鼎的开源启动器，我派对它有详尽的介绍 → 在[这里](https://sspai.com/post/33460)。

WoX 的看家功夫是基于 Everything 的基本文件搜索功能，它能在不到一秒钟的时间内将你想要的文件进行搜索并展现出来，快如闪电，当然这也包括将你要打开的应用快捷方式搜索出来，因而 WoX 可以充当应用程序的快捷启动器。除此之外，WoX 还可以调用计算器、预览颜色、打开控制面板的某项选项、直接调用搜索引擎搜索内容和直接运行 Shell 命令等等，而这些功能都归功于其强大的 Plugin 插件功能。当然 WoX 也提供了外观主题的定制功能。

WoX 和 Everything 两工具的完美结合，在使用体验上可以媲美 macOS 上的 Spotlight、Alfred 等效率启动器。

### ② QuickLook ：空格键预览工具

![img](/images/709b53653f7b437a8cdb53d8f2ad8c6c.png)QuickLook
macOS 上的「一指禅」—— 空格预览文件内容，绝对是一个经典、令人印象深刻的功能。在 Windows 上，QuickLook 可以实现空格预览的功能，并且支持的格式也很丰富，能够预览图片、文本、docx 文档、甚至是各种源码等等一系列文件。macOS 一指禅在 Windows 上也能完美践行了。🦄

![img](/images/2d42ddd29be544ffb8a6ad3997f7719a.png)空格预览图片、文本和 Markdown
QuickLook 可以直接在 Windows 应用商店免费下载得到。

### ③&nbsp;[快贴](http://clipber.com/)：云剪贴板工具

快贴是一个免费的跨平台的剪贴板同步工具，能够在多端设备同步剪贴板，并对剪贴板涉密内容进行自动识别、加密传输。

![img](/images/fc6ad863f85f45c3b66723acc86e4991.jpg)快贴
我在 iOS 和 Windows 端同时下载了快贴，在 iOS 保持后台运行的情况下，我在手机上复制的内容，能够很快的同步到云端，进而在 Windows 端能够粘贴。但是这个过程比 macOS 繁琐的地方在于，我需要通过全局快捷键来手动触发粘贴端的同步，这样的多一步操作虽说影响体验，也肯定不如 macOS 闭源的生态系统好，但是至少我不必用微信、QQ 之流当作我电脑与手机沟通的渠道了。

参考：[好用的全平台剪切板工具，我们为你找到了这&nbsp;3&nbsp;款](https://sspai.com/post/43775)

### ④ [Send Anywhere](https://send-anywhere.com/file-transfer)：文件传输工具

Send Anywhere 将文件上传到一个 p2p 网络上面，并非其服务器上，接受端通过随机六位接收码进行文件接受。这样的传输方式保证了文件的安全性和完整性，又能有相当的上传、下载和传输速度。Send Anywhere 可以说是全平台 Airdrop 了。

![img](/images/4bf75ec071a64da9a53a44d12044d52c.jpg)Send Anywhere
同时 Send Anywhere 有设备记忆功能，在曾经传输过文件的设备上，下一次传输的时候，六位接收码都不必输入。这样的分享文件的特性可以说是跨平台的救命稻草了。我在使用过程中除了在 Windows 平台传输结束之后 Send Anywhere 本身有几次会卡死，其他体验都极佳。

参考：[免费全平台的文件分享利器：SendAnywhere](https://sspai.com/post/40047)

## 效率工具

### ① smpic：sm.ms 图床上传软件

我的博客图片全部都放到了第三方的图床上面，这让我需要有一个便捷的图片上传途径。

smpic 通过 SM.MS 图床的 API 与大名鼎鼎的 AutoHotKey 脚本实现了这样的图片上传利器，我将快捷键绑定为 `Ctrl` + `Alt` + `U`，这样点击图片按下快捷键直接就可以将图片上传至图床，并同时返回相应的图片引用链接，一气呵成。

smpic 同样，是一款开源、免费的软件，可以在其&nbsp;[Github 页面](https://github.com/kookob/smpic)进行下载。

### ② [Typora](https://typora.io/)： Markdown 编辑器

![img](/images/070ed305645b4723af4618409d628f69.png)Typora
Typora&nbsp;不必多说了，基本上是 Windows 上写 Markdown 的必备利器了。我的这篇文章就是在 Windows 的 Typora 上面编写完成的。我派对 Typora 也有详尽的介绍：[让 Markdown 写作更简单，免费极简编辑器：Typora](https://sspai.com/post/30292)

### ③ [Snipaste](https://www.snipaste.com/)：截图工具

![img](/images/6072ccc49efd46d69423a5fcba3dd30b.png)Snipaste
Snipaste&nbsp;着实是 Windows 上最好的截图工具。但 Snipaste 除了我们常见的截图标注、窗口检测、全局快捷键等等简朴必备技能，还有贴图、取色等等高阶可玩性。目前 Snipaste 在 Windows 商店就可以下载得到，并且就在最近几天 Snipaste 也发布了 Pro 版本，增加了更多的玩法。

![img](/images/9e998019d1b647b7b97eb7ad04a9cda1.gif)Snipaste In Action
Snipaste 的开发者对 Snipaste 很是上心，我派单独采访了这位同学，在这里有更加具体的介绍 →&nbsp;[幕后丨他做了最强免费「截图」工具 Snipaste 后，还有上万字的话想说](https://sspai.com/post/35097)

上面介绍的工具中，除了 Typora 和图床上传工具 smpic 以外（smpic 因为免安装，所以不支持开机自启动），剩下的都有幸被我加入开机自启动名单。🎉

### 开发环境

经过近两年的开发，目前 Windows Subsystem For Linux（以下简称 WSL）已经十分完善。我从微软商店下载安装了 Ubuntu 18.04 作为 WSL 的系统，并使用 Ubuntu 下的 `aptitude` 包管理工具链配置了我的开发环境。安装 WSL 的详细步骤在 →&nbsp;[这里](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)。

![img](/images/477c247b59f44314b44031b8318b1dc9.png)Ubuntu WSL
在 WSL 中我安装了我的必备开发工具：

* `git` 代码版本控制
* `ssh` 远程服务器连接 🔗
* `zsh` 与 `oh-my-zsh` Shell 环境

在 Windows 中我通过 Hyper 终端环境进行实战。

Hyper 是一个基于 Election 的终端 Terminal Emulator，是一个插件丰富的、跨平台的终端。我写过一个有关它的详细介绍&nbsp;[HOW TO | 让自己的终端漂亮得不像实力派](https://spencerwoo.com/2018/06/16/Terminal/)。在 Windows 下，可以通过 Hyper 调用 WSL 中的 `bash.exe`，这样就不用面对万恶的小黑框了。😈

![img](/images/caa290646b8a4df39edad3c73443432a.png)我当前的开发环境
这样折腾之后，一套可用的基于命令行的开发环境也处于可用状态了。目前存在的问题是从 Windows 端调用 Linux 内部的指令还是有些问题，比如我在 Visual Studio Code 中试图调用 Linux 环境下的 Python 解释器进行调试就异常麻烦，目前 Visual Studio Code 团队对 C/C++ 和 Node.js 的调试都已经适配完成，至于 Python、Go 等语言，我相信未来的适配也会越来越完善。

参考：[My&nbsp;WSL&nbsp;Setup&nbsp;by&nbsp;lloydstubber](https://github.com/lloydstubber/my-wsl-setup)


## 其它软件

### 解压缩软件

[Bandizip for Windows](https://www.bandisoft.com/bandizip/)

开发这个软件的公司叫 Bandisoft，是一家挺低调的韩国软件公司，正是知名录屏软件 Bandicam 的初开发公司（后来由 Bandicam 公司接手开发）

优点是界面清爽，功能全面，没有广告和弹窗，国内竞品好压之类广告弹窗着实烦人。

![img](/images/176efff0c80546ffa41a1cce0cf602bb.png)

## 参考文档
[Mac To Win | 不完全迁移体验指北](https://sspai.com/post/45742)