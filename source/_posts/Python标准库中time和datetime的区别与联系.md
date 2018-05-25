---
title: Python 标准库中 time 和 datetime 的区别与联系
date: 2018-05-25 09:39:29
tags: nodejs npm
---

Python 中提供了对时间日期的多种多样的处理方式，主要是在 time 和 datetime 这两个模块里。今天稍微梳理一下这两个模块在使用上的一些区别和联系。

## time

在 Python 文档里，time是归类在Generic Operating System Services中，换句话说， 它提供的功能是更加接近于操作系统层面的。通读文档可知，time 模块是围绕着 Unix Timestamp 进行的。

该模块主要包括一个类 struct_time，另外其他几个函数及相关常量。 需要注意的是在该模块中的大多数函数是调用了所在平台C library的同名函数， 所以要特别注意有些函数是平台相关的，可能会在不同的平台有不同的效果。另外一点是，由于是基于Unix Timestamp，所以其所能表述的日期范围被限定在 1970 - 2038 之间，如果你写的代码需要处理在前面所述范围之外的日期，那可能需要考虑使用datetime模块更好。文档解释比较费劲，具体看看怎么用：

```python
In [1]: import time

In [2]: time.time()
Out[2]: 1414332433.345712
In [3]: timestamp = time.time()

In [4]: time.gmtime(timestamp)
Out[4]: time.struct_time(tm_year=2014, tm_mon=10, tm_mday=26, tm_hour=14, tm_min=7, tm_sec=13, tm_wday=6, tm_yday=299, tm_isdst=0)

In [5]: time.localtime(timestamp)
Out[5]: time.struct_time(tm_year=2014, tm_mon=10, tm_mday=26, tm_hour=22, tm_min=7, tm_sec=13, tm_wday=6, tm_yday=299, tm_isdst=0)
In [6]: struct_time = time.localtime(timestamp)

In [7]: time.ctime(timestamp)
Out[7]: 'Sun Oct 26 22:07:13 2014'

In [8]: time.asctime(struct_time)
Out[8]: 'Sun Oct 26 22:07:13 2014'

In [9]: time.mktime(struct_time)
Out[9]: 1414332433.0

In [10]: time.strftime("%Y-%m-%d_%H-%M-%S")
Out[10]: 2018-05-25_10-04-49

In [11]: time.strptime("30 Nov 00", "%d %b %y")
Out[11]: time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

```
问题不大，可能有时候需要注意一下使用的时区。

## datetime
datetime 比 time 高级了不少，可以理解为 datetime 基于 time 进行了封装，提供了更多实用的函数。在datetime 模块中包含了几个类，具体关系如下:

```python
object
    timedelta     # 主要用于计算时间跨度
    tzinfo        # 时区相关
    time          # 只关注时间
    date          # 只关注日期
        datetime  # 同时有时间和日期
```

名称比较绕口，在实际实用中，用得比较多的是 datetime.datetime 和 datetime.timedelta ，另外两个 datetime.date 和 datetime.time 实际使用和 datetime.datetime 并无太大差别。 下面主要讲讲 datetime.datetime 的使用。使用datetime.datetime.now()可以获得当前时刻的datetime.datetime 实例。 对于一个 datetime.datetime 实例，主要会有以下属性及常用方法，看名称就能理解，应该没有太大问题：

```python
datetime.year
datetime.month
datetime.day
datetime.hour
datetime.minute
datetime.second
datetime.microsecond
datetime.tzinfo

datetime.date() # 返回 date 对象
datetime.time() # 返回 time 对象
datetime.replace(name=value) # 前面所述各项属性是 read-only 的，需要此方法才可更改
datetime.timetuple() # 返回time.struct_time 对象
dattime.strftime(format) # 按照 format 进行格式化输出
```

除了实例本身具有的方法,类本身也提供了很多好用的方法：

```python
datetime.today()a  # 当前时间，localtime
datetime.now([tz]) # 当前时间默认 localtime
datetime.utcnow()  # UTC 时间
datetime.fromtimestamp(timestamp[, tz]) # 由 Unix Timestamp 构建对象
datetime.strptime(date_string, format)  # 给定时间格式解析字符串
```

请注意，上面省略了很多和时区相关的函数，如需使用请查文档。对于日期的计算，使用timedelta也算是比较简单的：

```python
In [1]: import datetime
In [2]: time_now = datetime.datetime.now()
In [3]: time_now
Out[3]: datetime.datetime(2014, 10, 27, 21, 46, 16, 657523)

In [4]: delta1 = datetime.timedelta(hours=25)
In [5]: print(time_now + delta1)
2014-10-28 22:46:16.657523

In [6]: print(time_now - delta1)
2014-10-26 20:46:16.657523
```

甚至两个 datetime 对象直接相减就能获得一个 timedelta 对象。如果有需要计算工作日的需求，可以使用 business_calendar这个库，不需要装其他依赖就可使用。