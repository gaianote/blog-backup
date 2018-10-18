title: Python中logging模块的基本用法
author: 李云鹏
date: 2018-09-13 03:05:00
tags:
---
## logging模块的基本用法

```python
import logging
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
 
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
```
在这里我们首先引入了 logging 模块，然后进行了一下基本的配置，这里通过 basicConfig 配置了 level 信息和 format 信息，这里 level 配置为 INFO 信息，即只输出 INFO 级别的信息，另外这里指定了 format 格式的字符串，包括 asctime、name、levelname、message 四个内容，分别代表运行时间、模块名称、日志级别、日志内容，这样输出内容便是这四者组合而成的内容了，这就是 logging 的全局配置。

<!--more-->

## basicConfig 的参数

* `filename`：即日志输出的文件名，如果指定了这个信息之后，实际上会启用 FileHandler，而不再是 StreamHandler，这样日志信息便会输出到文件中了。
* `filemode`：这个是指定日志文件的写入方式，有两种形式，一种是 w，一种是 a，分别代表清除后写入和追加写入。
* `format`：指定日志信息的输出格式，即上文示例所示的参数，部分参数如下所示：
  * `%(levelno)s`：打印日志级别的数值。
  * `%(levelname)s`：打印日志级别的名称。
  * `%(pathname)s`：打印当前执行程序的路径，其实就是sys.argv[0]。
  * `%(filename)s`：打印当前执行程序名。
  * `%(funcName)s`：打印日志的当前函数。
  * `%(lineno)d`：打印日志的当前行号。
  * `%(asctime)s`：打印日志的时间。
  * `%(thread)d`：打印线程ID。
  * `%(threadName)s`：打印线程名称。
  * `%(process)d`：打印进程ID。
  * `%(processName)s`：打印线程名称。
  * `%(module)s`：打印模块名称。
  * `%(message)s`：打印日志信息。
* `datefmt`：指定时间的输出格式。
* `style`：如果 format 参数指定了，这个参数就可以指定格式化时的占位符风格，如 %、{、$ 等。
* `level`：指定日志输出的类别，程序会输出大于等于此级别的信息。
* `stream`：在没有指定 filename 的时候会默认使用 StreamHandler，这时 stream 可以指定初始化的文件流。
* `handlers`：可以指定日志处理时所使用的 Handlers，必须是可迭代的。

## Level

首先我们来了解一下输出日志的等级信息，logging 模块共提供了如下等级，每个等级其实都对应了一个数值，列表如下：

* CRITICAL: 50
* FATAL: 50
* ERROR: 40
* WARNING: 30
* WARN: 30
* INFO: 20
* DEBUG: 10
* NOTSET: 0

这里最高的等级是 CRITICAL 和 FATAL，两个对应的数值都是 50，另外对于 WARNING 还提供了简写形式 WARN，两个对应的数值都是 30。

我们设置了输出 level，系统便只会输出 level 数值大于或等于该 level 的的日志结果，例如我们设置了输出日志 level 为 INFO，那么输出级别大于等于 INFO 的日志，如 WARNING、ERROR 等，DEBUG 和 NOSET 级别的不会输出。


## Handler

下面我们先来了解一下 Handler 的用法，看下面的实例：

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 设置handler的输出文件，格式并应用该handler
handler = logging.FileHandler('output.log')
handler.setFormatter(formatter)
logger.addHandler(handler)
# 输出日志
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
```

这里我们没有再使用 basicConfig 全局配置，而是先声明了一个 Logger 对象，然后指定了其对应的 Handler 为 FileHandler 对象，然后 Handler 对象还单独指定了 Formatter 对象单独配置输出格式，最后给 Logger 对象添加对应的 Handler 即可，最后可以发现日志就会被输出到 output.log 中，内容如下：

```
2018-06-03 14:53:36,467 - __main__ - INFO - This is a log info
2018-06-03 14:53:36,468 - __main__ - WARNING - Warning exists
2018-06-03 14:53:36,468 - __main__ - INFO - Finish
```
另外我们还可以使用其他的 Handler 进行日志的输出，logging 模块提供的 Handler 有：

* StreamHandler：`logging.StreamHandler`；日志输出到流，可以是 sys.stderr，sys.stdout 或者文件。
* FileHandler：`logging.FileHandler`；日志输出到文件。
* BaseRotatingHandler：`logging.handlers.BaseRotatingHandler`；基本的日志回滚方式。
* RotatingHandler：`logging.handlers.RotatingHandler`；日志回滚方式，支持日志文件最大数量和日志文件回滚。
* TimeRotatingHandler：`logging.handlers.TimeRotatingHandler`；日志回滚方式，在一定时间区域内回滚日志文件。
* SocketHandler：`logging.handlers.SocketHandler`；远程输出日志到TCP/IP sockets。
* DatagramHandler：`logging.handlers.DatagramHandler`；远程输出日志到UDP sockets。
* SMTPHandler：`logging.handlers.SMTPHandler`；远程输出日志到邮件地址。
* SysLogHandler：`logging.handlers.SysLogHandler`；日志输出到syslog。
* NTEventLogHandler：`logging.handlers.NTEventLogHandler`；远程输出日志到Windows NT/2000/XP的事件日志。
* MemoryHandler：`logging.handlers.MemoryHandler`；日志输出到内存中的指定buffer。
* HTTPHandler：`logging.handlers.HTTPHandler`；通过”GET”或者”POST”远程输出到HTTP服务器。

下面我们使用三个 Handler 来实现日志同时输出到控制台、文件、HTTP 服务器：

```python
import logging
from logging.handlers import HTTPHandler
import sys

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger.addHandler(stream_handler)

# FileHandler
file_handler = logging.FileHandler('output.log')
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# HTTPHandler
http_handler = HTTPHandler(host='localhost:8001', url='log', method='POST')
logger.addHandler(http_handler)

# Log
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
```
## Formatter

在进行日志格式化输出的时候，我们可以不借助于 basicConfig 来全局配置格式化输出内容，可以借助于 Formatter 来完成，下面我们再来单独看下 Formatter 的用法：

```python
import logging
 
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARN)
formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
 
# Log
logger.debug('Debugging')
logger.critical('Critical Something')
logger.error('Error Occurred')
logger.warning('Warning exists')
logger.info('Finished')
```

在这里我们指定了一个 Formatter，并传入了 fmt 和 datefmt 参数，这样就指定了日志结果的输出格式和时间格式，然后 handler 通过 setFormatter() 方法设置此 Formatter 对象即可，输出结果如下：

```
2018/06/03 15:47:15 - __main__ - CRITICAL - Critical Something
2018/06/03 15:47:15 - __main__ - ERROR - Error Occurred
2018/06/03 15:47:15 - __main__ - WARNING - Warning 
```

这样我们可以每个 Handler 单独配置输出的格式，非常灵活。



## 异常处理

另外在进行异常处理的时候，通常我们会直接将异常进行字符串格式化，但其实可以直接指定一个参数将 traceback 打印出来，示例如下：

```python
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

try:
    result = 5 / 0
except Exception as e:
    # bad
    logging.error('Error: %s', e)
    # good
    logging.error('Error', exc_info=True)
    # good
    logging.exception('Error')
```

如果我们直接使用字符串格式化的方法将错误输出的话，是不会包含 Traceback 信息的，但如果我们加上 exc_info 参数或者直接使用 exception() 方法打印的话，那就会输出 Traceback 信息了。

运行结果如下：

```
2018-06-03 22:24:31,927 - root - ERROR - Error: division by zero
2018-06-03 22:24:31,927 - root - ERROR - Error
Traceback (most recent call last):
  File "/private/var/books/aicodes/loggingtest/demo9.py", line 6, in <module>
    result = 5 / 0
ZeroDivisionError: division by zero
2018-06-03 22:24:31,928 - root - ERROR - Error
Traceback (most recent call last):
  File "/private/var/books/aicodes/loggingtest/demo9.py", line 6, in <module>
    result = 5 / 0
ZeroDivisionError: division by zero
```


