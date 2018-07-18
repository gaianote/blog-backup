---
title: "avocado自动化测试框架中文文档"
date: 2018-07-18 09:21:04
tags:
---

## 关于Avocado

Avocado是一套帮助自动化测试的工具和库。

人们可以将其称为具有益处的测试框架。 本机测试是用Python编写的，它们遵循unitest模式，但任何可执行文件都可以作为测试。

Avocado由以下组成：

* 一个允许您执行测试的测试运行器。 这些测试可以用您选择的语言编写，也可以用Python编写并使用可用的库。 在这两种情况下，您都可以获得自动日志和系统信息收集等功能。

* 帮助您以简洁，富有表现力和强大的方式编写测试的库。 您可以在库和API中找到有关哪些库适用于测试编写者的更多信息。

* 可以扩展Avocado Framework并为其添加新功能的插件。

Avocado是建立在Autotest积累的经验基础上，同时改善其弱点和缺点。

鳄梨尽可能地遵守标准的Python测试技术。 使用Avocado API编写的测试来自unittest类，同时添加了适用于功能和性能测试的其他方法。 测试运行器旨在帮助人们在提供各种系统和日志记录工具的同时运行他们的测试，并且如果您需要更多功能，那么您可以逐步开始使用API功能。

## 入门

那些喜欢视频介绍的人，请看看其他资源。 无论哪种方式，使用鳄梨的第一步显然是安装它。

### 安装Avocado

Avocado主要是用Python编写的，因此标准的Python安装是可行的，而且通常更可取。

>>>如果您正在寻找特定于虚拟化的测试，请在完成Avocado安装后考虑查看Avocado-VT安装说明。

#### 使用标准Python工具进行安装

最简单的安装方法是通过pip。 在大多数可用Python 2.7和pip的POSIX系统上，只需一个命令即可执行安装：

```bash
pip install --user avocado-framework
```
这将从PyPI存储库中获取Avocado包（可能还有一些依赖项），并尝试将其安装在用户的主目录中（通常在〜/ .local下）。

>>> 如果要执行系统范围的安装，请删除 --user项。

如果您想要更多隔离，Avocado也可以安装在Python虚拟环境中。 除了创建和激活虚拟环境本身之外没有其他步骤：

```bash
python -m virtualenv /path/to/new/virtual_environment
. /path/to/new/virtual_environment/bin/activate
pip install avocado-framework
```

请注意，这将安装Avocado核心功能。

许多Avocado功能都作为非核心插件分发，也可作为PyPI上的附加软件包提供。 你应该能够通过`pip search avocado-framework-plugin | grep avocado-framework-plugin`找到它们。其中一些列在下面：

[avocado-framework-plugin-result-html](https://pypi.python.org/pypi/avocado-framework-plugin-result-html): HTML报告

* [avocado-framework-plugin-resultsdb](https://pypi.python.org/pypi/avocado-framework-plugin-resultsdb): 将作业结果传播到Resultsdb

* [avocado-framework-plugin-runner-remote](https://pypi.python.org/pypi/avocado-framework-plugin-runner-remote): 用于远程执行的运行器

* [avocado-framework-plugin-runner-vm](https://pypi.python.org/pypi/avocado-framework-plugin-runner-vm): 用于libvirt VM执行的运行器

* [avocado-framework-plugin-runner-docker](https://pypi.python.org/pypi/avocado-framework-plugin-runner-docker): Docker容器上执行的Runner

* [avocado-framework-plugin-loader-yaml](https://pypi.python.org/pypi/avocado-framework-plugin-loader-yaml): 从YAML文件加载测试

* [avocado-framework-plugin-robot](https://pypi.python.org/pypi/avocado-framework-plugin-robot): 执行Robot Framework测试

* [avocado-framework-plugin-varianter-yaml-to-mux](https://pypi.python.org/pypi/avocado-framework-plugin-varianter-yaml-to-mux): 将YAML文件解析为变体

#### 从包安装

原文介绍了一些Avocado其它的安装方法，有兴趣可以去[原址](https://avocado-framework.readthedocs.io/en/63.0/GetStartedGuide.html#installing-from-packages)查看

### 使用Avocado

您应首先使用测试运行器体验Avocado，即命令行工具，它将方便地运行您的测试并收集其结果。

#### 运行测试

为此,请使用`run`子命令运行Avocado,`run`后面跟随要进行的测试,它可以是文件的路径，也可以是可识别的名称：

```
$ avocado run /bin/true
JOB ID    : 381b849a62784228d2fd208d929cc49f310412dc
JOB LOG   : $HOME/avocado/job-results/job-2014-08-12T15.39-381b849a/job.log
 (1/1) /bin/true: PASS (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.11 s
JOB HTML  : $HOME/avocado/job-results/job-2014-08-12T15.39-381b849a/html/results.html
```

您可能已经注意到我们使用/ bin / true作为测试，并且根据我们的期望，它通过了！ 这些被称为简单测试，但也有另一种类型的测试，我们称之为仪器测试。 在测试类型中查看更多信息或继续阅读。

>>>虽然在大多数情况下运行Avocado运行 $ test1 $ test3 ...很好，但它可能导致参数与测试名称冲突。 最安全的执行测试的方法是Avocado运行 -  $ argument1  -  $ argument2  -  $ test1 $ test2。 之后的所有内容 - 将被视为位置参数，即测试名称（在Avocado运行的情况下）

#### 列出测试

您有两种方法来检测测试文件。 您可以使用--dry-run参数来模拟执行：

```
avocado run /bin/true --dry-run
JOB ID     : 0000000000000000000000000000000000000000
JOB LOG    : /tmp/avocado-dry-runSeWniM/job-2015-10-16T15.46-0000000/job.log
 (1/1) /bin/true: SKIP
RESULTS    : PASS 0 | ERROR 0 | FAIL 0 | SKIP 1 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.10 s
JOB HTML   : /tmp/avocado-dry-runSeWniM/job-2015-10-16T15.46-0000000/html/results.html
```
它支持所有运行参数，模拟运行甚至列出测试参数。

另一种方法是使用list子命令列出发现的测试如果没有提供参数，Avocado会为每个插件列出“默认”测试。 输出可能如下所示：

```
$ avocado list
INSTRUMENTED /usr/share/doc/avocado/tests/abort.py
INSTRUMENTED /usr/share/doc/avocado/tests/datadir.py
INSTRUMENTED /usr/share/doc/avocado/tests/doublefail.py
INSTRUMENTED /usr/share/doc/avocado/tests/doublefree.py
INSTRUMENTED /usr/share/doc/avocado/tests/errortest.py
INSTRUMENTED /usr/share/doc/avocado/tests/failtest.py
INSTRUMENTED /usr/share/doc/avocado/tests/fiotest.py
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py
INSTRUMENTED /usr/share/doc/avocado/tests/gendata.py
INSTRUMENTED /usr/share/doc/avocado/tests/linuxbuild.py
INSTRUMENTED /usr/share/doc/avocado/tests/multiplextest.py
INSTRUMENTED /usr/share/doc/avocado/tests/passtest.py
INSTRUMENTED /usr/share/doc/avocado/tests/sleeptenmin.py
INSTRUMENTED /usr/share/doc/avocado/tests/sleeptest.py
INSTRUMENTED /usr/share/doc/avocado/tests/synctest.py
INSTRUMENTED /usr/share/doc/avocado/tests/timeouttest.py
INSTRUMENTED /usr/share/doc/avocado/tests/warntest.py
INSTRUMENTED /usr/share/doc/avocado/tests/whiteboard.py
...
```

Avocado认为这些Python文件包含INSTRUMENTED测试。

现在让我们列出可执行的shell脚本：

```
$ avocado list | grep ^SIMPLE
SIMPLE       /usr/share/doc/avocado/tests/env_variables.sh
SIMPLE       /usr/share/doc/avocado/tests/output_check.sh
SIMPLE       /usr/share/doc/avocado/tests/simplewarning.sh
SIMPLE       /usr/share/doc/avocado/tests/failtest.sh
SIMPLE       /usr/share/doc/avocado/tests/passtest.sh
```
这里，如前所述，SIMPLE意味着这些文件是可执行文件，被视为简单测试。 您还可以使用--verbose或-V标志来显示Avocado找到的文件，但不被视为Avocado测试：

```
$ avocado list examples/gdb-prerun-scripts/ -V
Type       Test                                     Tag(s)
NOT_A_TEST examples/gdb-prerun-scripts/README
NOT_A_TEST examples/gdb-prerun-scripts/pass-sigusr1

TEST TYPES SUMMARY
==================
SIMPLE: 0
INSTRUMENTED: 0
MISSING: 0
NOT_A_TEST: 2
```
请注意，详细标志还会添加摘要信息。

#### 写一个简单的测试

这个用shell脚本编写的简单测试的简单例子

```bash
$ echo '#!/bin/bash' > /tmp/simple_test.sh
$ echo 'exit 0' >> /tmp/simple_test.sh
$ chmod +x /tmp/simple_test.sh
```

請注意，該文件具有可執行權限，這是Avocado將其視為簡單測試的要求。 另請注意，腳本以狀態代碼0退出，這表示Avocado成功結果。

## 原文档

[原文档](https://avocado-framework.readthedocs.io/en/63.0/Introduction.html)