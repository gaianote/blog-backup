title: 在python中使用代理
author: 李云鹏
date: 2018-10-12 07:17:41
tags:
---
## Urllib

首先我们以最基础的 Urllib 为例，来看一下代理的设置方法，代码如下：

```python
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '127.0.0.1:9743'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

```

运行结果如下：

```python
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.6"
  }, 
  "origin": "106.185.45.153", 
  "url": "http://httpbin.org/get"
}

```

在这里我们需要借助于 ProxyHandler 设置代理，参数是字典类型，键名为协议类型，键值是代理，注意此处代理前面需要加上协议，即 http 或者 https，此处设置了 http 和 https 两种代理，当我们请求的链接是 http 协议的时候，它会调用 http 代理，当请求的链接是 https 协议的时候，它会调用https代理，所以此处生效的代理是：http://127.0.0.1:9743

创建完 ProxyHandler 对象之后，我们需要利用 build_opener() 方法传入该对象来创建一个 Opener，这样就相当于此 Opener 已经设置好代理了，接下来直接调用它的 open() 方法即可使用此代理访问我们所想要的链接。

运行输出结果是一个 Json，它有一个字段 origin，标明了客户端的 IP，此处的 IP 验证一下，确实为代理的 IP，而并不是我们真实的 IP，所以这样我们就成功设置好代理，并可以隐藏真实 IP 了。

如果遇到需要认证的代理，我们可以用如下的方法设置：

```python
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = 'username:password@127.0.0.1:9743'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

```

这里改变的只是 proxy 变量，只需要在代理前面加入代理认证的用户名密码即可，其中 username 就是用户名，password 为密码，例如 username 为foo，密码为 bar，那么代理就是 foo:bar@127.0.0.1:9743。

如果代理是 SOCKS5 类型，那么可以用如下方式设置代理：

```python
import socks
import socket
from urllib import request
from urllib.error import URLError

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9742)
socket.socket = socks.socksocket
try:
    response = request.urlopen('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

```

此处需要一个 Socks 模块，可以通过如下命令安装：

```
pip3 install PySocks

```

本地我有一个 SOCKS5 代理，运行在 9742 端口，运行成功之后和上文 HTTP 代理输出结果是一样的：

```python
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.6"
  }, 
  "origin": "106.185.45.153", 
  "url": "http://httpbin.org/get"
}

```

结果的 origin 字段同样为代理的 IP，设置代理成功。

## Requests

对于 Requests 来说，代理设置更加简单，我们只需要传入 proxies 参数即可。

还是以上例中的代理为例，我们来看下 Requests 的代理的设置：

```python
import requests

proxy = '127.0.0.1:9743'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

```

运行结果：

```python
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.1"
  }, 
  "origin": "106.185.45.153", 
  "url": "http://httpbin.org/get"
}

```

可以发现 Requests 的代理设置比 Urllib 简单很多，只需要构造代理字典即可，然后通过 proxies 参数即可设置代理，不需要重新构建 Opener。

可以发现其运行结果的 origin 也是代理的 IP，证明代理已经设置成功。

如果代理需要认证，同样在代理的前面加上用户名密码即可，代理的写法就变成：

```python
proxy = 'username:password@127.0.0.1:9743'

```

和 Urllib 一样，只需要将 username 和 password 替换即可。

如果需要使用 SOCKS5 代理，则可以使用如下方式：

```python
import requests

proxy = '127.0.0.1:9742'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

```

在这里需要额外安装一个 Socks 模块，命令如下：

```python
pip3 install "requests[socks]"

```

运行结果是完全相同的：

```
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.1"
  }, 
  "origin": "106.185.45.153", 
  "url": "http://httpbin.org/get"
}

```

另外还有一种设置方式，和 Urllib 中的方法相同，使用 socks 模块，也需要像上文一样安装该库，设置方法如下：

```python
import requests
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9742)
socket.socket = socks.socksocket
try:
    response = requests.get('http://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

```

这样也可以设置 SOCKS5 代理，运行结果完全相同，相比第一种方法，此方法是全局设置，不同情况可以选用不同的方法。

## Selenium

Selenium 同样也可以设置代理，在这里分两种介绍，一个是有界面浏览器，以 Chrome 为例介绍，另一种是无界面浏览器，以 PhantomJS 为例介绍。

### Chrome

对于 Chrome 来说，用 Selenium 设置代理的方法也非常简单，设置方法如下：

```python
from selenium import webdriver

proxy = '127.0.0.1:9743'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')

```

在这里我们通过 ChromeOptions 来设置代理，在创建 Chrome 对象的时候通过 chrome_options 参数传递即可。

这样在运行之后便会弹出一个 Chrome 浏览器，访问目标链接之后输出结果如下：

```python
{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "zh-CN,zh;q=0.8", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
  }, 
  "origin": "106.185.45.153", 
  "url": "http://httpbin.org/get"
}

```

可以看到 origin 同样为代理 IP 的地址，代理设置成功。

如果代理是认证代理，则设置方法相对比较麻烦，方法如下：

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import zipfile

ip = '127.0.0.1'
port = 9743
username = 'foo'
password = 'bar'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    }
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%(ip)s",
            port: %(port)s
          }
        }
      }

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%(username)s",
            password: "%(password)s"
        }
    }
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
)
""" % {'ip': ip, 'port': port, 'username': username, 'password': password}

plugin_file = 'proxy_auth_plugin.zip'
with zipfile.ZipFile(plugin_file, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_extension(plugin_file)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')

```

在这里需要在本地创建一个 manifest.json 配置文件和 background.js 脚本来设置认证代理，运行之后本地会生成一个 proxy_auth_plugin.zip 文件保存配置。

运行结果和上例一致，origin 同样为代理 IP。

## PhantomJS

对于 PhantomJS，代理设置方法可以借助于 service_args 参数，也就是命令行参数，代理设置方法如下：

```python
from selenium import webdriver

service_args = [
    '--proxy=127.0.0.1:9743',
    '--proxy-type=http'
]
browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)

```

在这里我们只需要使用 service_args 参数，将命令行的一些参数定义为列表，在初始化的时候传递即可。

运行结果：

```
{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "zh-CN,en,*", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.1.0 Safari/538.1"
  }, 
  "origin": "106.185.45.153", 
  "url": "http://httpbin.org/get"
}

```

运行结果的 origin 同样为代理的 IP，设置代理成功。

如果需要认证，那么只需要再加入 --proxy-auth 选项即可，这样参数就改为：

```python
service_args = [
    '--proxy=127.0.0.1:9743',
    '--proxy-type=http',
    '--proxy-auth=username:password'
]

```

将 username 和 password 替换为认证所需的用户名和密码即可。

## 参考链接

[Python3 中代理使用方法总结](https://zhuanlan.zhihu.com/p/30670193)




​