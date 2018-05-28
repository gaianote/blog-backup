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

## 超时设置

```python
from selenium import webdriver
d= webdriver.PhantomJS()
#这两种设置都进行才有效

d.set_page_load_timeout(10)
d.set_script_timeout(10)
```

## selenium中运行js

注意两点

1. 希望获得返回值需要js文件含有`return`关键字
2. 希望在已经获取的元素上进行js操作，需要传入第二个参数elem

```python
driver = webdriver.Chrome()
elem = driver.get_element_by_id("input_all")
driver.execute_script('return arguments[0].checked',elem)
```
## 参考文档

[selinium设置请求头](https://www.zhihu.com/question/35547395)
[盘点selenium phantomJS使用的坑](http://www.jianshu.com/p/9d408e21dc3a)
[selenium设置Chrome](http://www.cnblogs.com/TTyb/p/6128323.html)