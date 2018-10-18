---
title: selenium应用指南
date: 2017-04-23 22:07:42
tags:
- python
- selenium
---

## 安装selenium

1.安装selenium,以管理员身份运行cmd,输入以下命名

```bash
pip install selenium
```

2.下载chromedriver(),放到python.exe同级目录中

## selenium设置请求头

### selenium设置phantomjs请求头：

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.get("https://httpbin.org/get?show_env=1")
driver.get_screenshot_as_file('01.png')
driver.quit()
```

### phantomJS详细配置问题

隐式等待不一定靠谱，所以尽量使用python自身函接口

```python
from selenium import webdriver
# 引入配置对象DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
#从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
dcap["phantomjs.page.settings.userAgent"] = (random.choice(USER_AGENTS))
# 不载入图片，爬页面速度会快很多
dcap["phantomjs.page.settings.loadImages"] = False
# 设置代理
service_args = ['--proxy=127.0.0.1:9999','--proxy-type=socks5']
#打开带配置信息的phantomJS浏览器
driver = webdriver.PhantomJS(phantomjs_driver_path, desired_capabilities=dcap,service_args=service_args)
# 设置10秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项
driver.set_page_load_timeout(10)
# 设置10秒脚本超时时间
driver.set_script_timeout(10)
```

### phantomJS与并发

* IO密集型的程序，多线程/协程比较合适。对于Chrome程序能正常运行，而phantomJS有时有问题
* phantomJS本身在多线程方面还有很多bug，建议使用多进程

```python
from multiprocessing import Pool
pool = Pool(8)
data_list = pool.map(get, url_list)
pool.close()
pool.join()
```

### selenium设置chrome请求头：

```python
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
# 设置header
options.add_argument('user-agent=Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20')
# 设置代理
options.add_argument('--proxy-server=127.0.0.1:9999')
browser = webdriver.Chrome(chrome_options=options)
url = "https://httpbin.org/get?show_env=1"
browser.get(url)
browser.quit()
```

### 携带cookie

```python
from selenium import webdriver
browser = webdriver.Chrome()

url = "https://www.baidu.com/"
browser.get(url)
browser.delete_all_cookies()
browser.add_cookie({'name':'ABC','value':'DEF'})
input("查看效果")
browser.quit()
```

## selenium中运行js

注意

1. 希望获得返回值需要js文件含有`return`关键字
2. 希望在已经获取的元素上进行js操作，需要传入第二个参数elem
3. 在js中，运行后return一个字典或者数组,在python中可以直接使用,selenium已经对此做了处理
4. 如果希望以`'return func(%s)'%param`的方式传入数组等,需要json化处理

```python
driver = webdriver.Chrome()
elem = driver.get_element_by_id("input_all")
driver.execute_script('return arguments[0].checked',elem)
```

## selenium 文件上传

首先，我们要区分出上传按钮的种类，大体上可以分为两种，一种是input框，另外一种就比较复杂，通过js、flash等实现，标签非input

### input标签

众所周知，input标签是可以直接`send_keys`的，这里也不例外，来看代码示例：

示例网址： http://www.sahitest.com/demo/php/fileUpload.htm

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
upload.send_keys('d:\\baidu.py')  # send_keys
print upload.get_attribute('value')  # check value

driver.quit()
```
结果：

```python
baidu.py
```

## selenium 元素是否可点击

## frame

很多人在用selenium定位页面元素的时候会遇到定位不到的问题，明明元素就在那儿，就是定位不到，这种情况很有可能是 frame 在搞鬼。

frame标签有frameset、frame、iframe三种：

* frameset跟其他普通标签没有区别，不会影响到正常的定位
* frame与iframe对selenium定位而言是一样的

selenium有一组方法对frame进行操作：

```python
driver.switch_to.frame(reference)  # 切到指定frame，可用id或name(str)、index(int)、元素(WebElement)定位
driver.switch_to.parent_frame()  # 切到父级frame，如果已是主文档，则无效果
driver.switch_to.default_content()  # 切到主文档，DOM树最开始的<html>标签
```
### 怎么切到frame中(switch_to.frame())

selenium提供了switch_to.frame()方法来切换frame

switch_to.frame(reference)

不得不提到switch_to_frame(reference)，很多人在这样写的时候会发现，这句话被划上了删除线，原因是这个方法已经out了，之后很有可能会不支持，建议的写法是switch_to.frame(reference)

reference是传入的参数，用来定位frame，可以传入id、name、index以及selenium的WebElement对象，假设有如下HTML代码 index.html：

```html
<html lang="en">
<head>
    <title>FrameTest</title>
</head>
<body>
<iframe src="a.html" id="frame1" name="myframe"></iframe>
</body>
</html>
```

想要定位其中的iframe并切进去，可以通过如下代码：

```python
from selenium import webdriver
driver = webdriver.Firefox()
driver.switch_to.frame(0)  # 1.用frame的index来定位，第一个是0
# driver.switch_to.frame("frame1")  # 2.用id来定位
# driver.switch_to.frame("myframe")  # 3.用name来定位
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 4.用WebElement对象来定位
```

通常采用id和name就能够解决绝大多数问题。但有时候frame并无这两项属性，则可以用index和WebElement来定位：

index从0开始，传入整型参数即判定为用index定位，传入str参数则判定为用id/name定位

WebElement对象，即用`find_element`系列方法所取得的对象，我们可以用tag_name、xpath等来定位frame对象

举个栗子：

```html
<iframe src="myframetest.html" />
```

用xpath定位，传入WebElement对象：

```python
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'myframe')]"))
```

### 从frame中切回主文档(`switch_to.default_content()`)

切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档。

driver.switch_to.default_content()

### 嵌套frame的操作(`switch_to.parent_frame()`)

有时候我们会遇到嵌套的frame，如下：

```html
<html>
    <iframe id="frame1">
        <iframe id="frame2" / >
    </iframe>
</html>
```

1.从主文档切到frame2，一层层切进去

```python
driver.switch_to.frame("frame1")  # 先切到frame1
driver.switch_to.frame("frame2")  # 再切到frame2
```

2.从frame2再切回frame1，这里selenium给我们提供了一个方法能够从子frame切回到父frame，而不用我们切回主文档再切进来。

```python
driver.switch_to.parent_frame()  # 如果当前已是主文档，则无效果
```
有了parent_frame()这个相当于后退的方法，我们可以随意切换不同的frame，随意的跳来跳去了。

所以只要善用以下三个方法，遇到frame分分钟搞定：

```python
driver.switch_to.frame(reference)
driver.switch_to.parent_frame()
driver.switch_to.default_content()
```

### frame的学习

[frame,我们来谈一谈](https://www.villainhr.com/page/2016/06/28/frame,%E6%88%91%E4%BB%AC%E6%9D%A5%E8%B0%88%E4%B8%80%E8%B0%88)

## selenium屏幕截图

```python
driver.get_screenshot_as_base64()            截屏保存为base64适用于HTML中嵌入的图片
driver.get_screenshot_as_file(filename)      截屏保存为一个文件，提供路径
driver.get_screenshot_as_png()               截屏保存为一个二进制数据
```

## 参考文档标签

[selinium设置请求头](https://www.zhihu.com/question/35547395)
[盘点selenium phantomJS使用的坑](http://www.jianshu.com/p/9d408e21dc3a)
[selenium设置Chrome](http://www.cnblogs.com/TTyb/p/6128323.html)
[selenium之文件上传所有方法整理总结](https://blog.csdn.net/huilan_same/article/details/52439546)
[Python selenium —— 深刻解析及操作frame、iframe](https://huilansame.github.io/huilansame.github.io/archivers/switch-to-frame)