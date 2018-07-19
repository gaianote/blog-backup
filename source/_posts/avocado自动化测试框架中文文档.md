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

Avocado尽可能地遵守标准的Python测试技术。 使用Avocado API编写的测试来自unittest类，同时添加了适用于功能和性能测试的其他方法。 测试运行器旨在帮助人们在提供各种系统和日志记录工具的同时运行他们的测试，并且如果您需要更多功能，那么您可以逐步开始使用API功能。

## 入门

那些喜欢视频介绍的人，请看看其他资源。 无论哪种方式，使用Avocado的第一步显然是安装它。

### 安装Avocado

Avocado主要是用Python编写的，因此标准的Python安装是可行的，而且通常更可取。

>>>如果您正在寻找特定于虚拟化的测试，请在完成Avocado安装后考虑查看Avocado-VT安装说明。

#### 使用标准Python工具进行安装

最简单的安装方法是通过pip。 在大多数可用Python 2.7和pip的POSIX系统上，只需一个命令即可执行安装：

>>> 译者注:虽然python2.7是可用的，但是已经逐渐被淘汰了，因此建议使用python3.6+以及其相对应的pip进行安装

```bash
pip install --user avocado-framework
```
这将从PyPI存储库中获取Avocado包（可能还有一些依赖项），并尝试将其安装在用户的主目录中（通常在〜/ .local下）。

>>> 如果要执行系统范围的安装，请删除 --user删除。
>>> 译者:如果希望在命令行启用 avocado 命令的话，安装时不能使用 --user 参数

如果您想要更多隔离，Avocado也可以安装在Python虚拟环境中。 除了创建和激活虚拟环境本身之外没有其他步骤：

```bash
python -m virtualenv /path/to/new/virtual_environment
. /path/to/new/virtual_environment/bin/activate
pip install avocado-framework
```

请注意，这将安装Avocado核心功能。

许多Avocado功能都作为非核心插件分发，也可作为PyPI上的附加软件包提供。 你应该能够通过`pip search avocado-framework-plugin | grep avocado-framework-plugin`找到它们。其中一些列在下面：

* [avocado-framework-plugin-result-html](https://pypi.python.org/pypi/avocado-framework-plugin-result-html): HTML报告

* [avocado-framework-plugin-resultsdb](https://pypi.python.org/pypi/avocado-framework-plugin-resultsdb): 将作业结果传播到Resultsdb

* [avocado-framework-plugin-runner-remote](https://pypi.python.org/pypi/avocado-framework-plugin-runner-remote): 用于远程执行的运行器

* [avocado-framework-plugin-runner-vm](https://pypi.python.org/pypi/avocado-framework-plugin-runner-vm): 用于libvirt VM执行的运行器

* [avocado-framework-plugin-runner-docker](https://pypi.python.org/pypi/avocado-framework-plugin-runner-docker): Docker容器上执行的Runner

* [avocado-framework-plugin-loader-yaml](https://pypi.python.org/pypi/avocado-framework-plugin-loader-yaml): 从YAML文件加载测试

* [avocado-framework-plugin-robot](https://pypi.python.org/pypi/avocado-framework-plugin-robot): 执行Robot Framework测试

* [avocado-framework-plugin-varianter-yaml-to-mux](https://pypi.python.org/pypi/avocado-framework-plugin-varianter-yaml-to-mux): 将YAML文件解析为变量

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

>>> 译者: `avocado list .` 列出当前目录的avocado测试,直接使用`avocado list`未返回结果。

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

#### 运行更复杂的测试工作

您可以按任意顺序运行任意数量的测试，以及混合和匹配仪器化测试和简单测试：

```
$ avocado run failtest.py sleeptest.py synctest.py failtest.py synctest.py /tmp/simple_test.sh
JOB ID    : 86911e49b5f2c36caeea41307cee4fecdcdfa121
JOB LOG   : $HOME/avocado/job-results/job-2014-08-12T15.42-86911e49/job.log
 (1/6) failtest.py:FailTest.test: FAIL (0.00 s)
 (2/6) sleeptest.py:SleepTest.test: PASS (1.00 s)
 (3/6) synctest.py:SyncTest.test: PASS (2.43 s)
 (4/6) failtest.py:FailTest.test: FAIL (0.00 s)
 (5/6) synctest.py:SyncTest.test: PASS (2.44 s)
 (6/6) /tmp/simple_test.sh.1: PASS (0.02 s)
RESULTS    : PASS 4 | ERROR 0 | FAIL 2 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 5.98 s
JOB HTML  : $HOME/avocado/job-results/job-2014-08-12T15.42-86911e49/html/results.html
```

#### 在第一次失败的测试中中断作业（failfast）

Avocado运行命令具有选项`--failfast on`以在遇到第一次失败的测试时退出测试,后面的用例不再继续执行：

```
$ avocado run --failfast on /bin/true /bin/false /bin/true /bin/true
JOB ID     : eaf51b8c7d6be966bdf5562c9611b1ec2db3f68a
JOB LOG    : $HOME/avocado/job-results/job-2016-07-19T09.43-eaf51b8/job.log
 (1/4) /bin/true: PASS (0.01 s)
 (2/4) /bin/false: FAIL (0.01 s)
Interrupting job (failfast).
RESULTS    : PASS 1 | ERROR 0 | FAIL 1 | SKIP 2 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.12 s
JOB HTML   : /home/apahim/avocado/job-results/job-2016-07-19T09.43-eaf51b8/html/results.html
```

在重新运行`--failfast on`执行的作业时，也可以使用`--failfast off`强制禁用failfast模式。

#### 忽略缺少的测试引用

当您提供测试参考列表时，Avocado将尝试将所有测试参考解析为测试。如果无法将一个或多个测试引用解析为测试，则不会创建作业。例：

```
$ avocado run passtest.py badtest.py
Unable to resolve reference(s) 'badtest.py' with plugins(s) 'file', 'robot', 'external', try running 'avocado list -V badtest.py' to see the details.
```
但是如果你无论如何都想要执行这项测试，使用可以解决的测试，你可以使用`--ignore-missing-references on`。 UI中将显示相同的消息，但将执行这个测试：

```
$ avocado run passtest.py badtest.py --ignore-missing-references on
Unable to resolve reference(s) 'badtest.py' with plugins(s) 'file', 'robot', 'external', try running 'avocado list -V badtest.py' to see the details.
JOB ID     : 85927c113074b9defd64ea595d6d1c3fdfc1f58f
JOB LOG    : $HOME/avocado/job-results/job-2017-05-17T10.54-85927c1/job.log
 (1/1) passtest.py:PassTest.test: PASS (0.02 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 0
JOB TIME   : 0.11 s
JOB HTML   : $HOME/avocado/job-results/job-2017-05-17T10.54-85927c1/html/results.html
```
#### 使用外部运行器运行测试

在大多数软件项目中使用有机增长的测试套件是很常见的。这些通常包括一个定制的，非常具体的测试运行器，它知道如何查找和运行自己的测试

尽管如此，由于各种原因，在Avocado中运行这些测试可能是一个好主意，包括能够以不同的人机和机器可读格式获得结果，收集系统信息以及这些测试（Avocado的sysinfo功能）等等

Avocado 通过其"external runner"功能实现了这一目标。最基本的使用方法是：

```bash
$ avocado run --external-runner=/path/to/external_runner foo bar baz
```
在此示例中，Avocado将报告测试foo，bar和baz的各个测试结果。实际结果将基于`/path/to/external_runner foo`，`/path/to/external_runner bar`和`/path/to/external_runner baz`的单独执行的返回代码。其中`/path/to/external_runner`是你的外部解释器的路径。


作为另一种解释该功能如何工作的方法，可以将"external runner"视为某种解释器，并将个体测试视为此解释器识别并能够执行的任何内容。一个UNIX shell，比如`/bin/sh`可以被认为是一个外部运行器，带有shell代码的文件可以被认为是测试：

```bash
$ echo "exit 0" > /tmp/pass
$ echo "exit 1" > /tmp/fail
$ avocado run --external-runner=/bin/sh /tmp/pass /tmp/fail
JOB ID     : 4a2a1d259690cc7b226e33facdde4f628ab30741
JOB LOG    : /home/<user>/avocado/job-results/job-<date>-<shortid>/job.log
(1/2) /tmp/pass: PASS (0.01 s)
(2/2) /tmp/fail: FAIL (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 1 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.11 s
JOB HTML   : /home/<user>/avocado/job-results/job-<date>-<shortid>/html/results.html
```

这个例子非常明显，可以通过给/tmp/pass和/tmp/fail "shebangs"（#!/bin/sh）来实现，使它们可执行（chmod+x /tmp/pass /tmp/fail并将它们作为"SIMPLE"测试运行。

#### 但现在考虑以下示例：

```bash
$ avocado run --external-runner=/bin/curl http://local-avocado-server:9405/jobs/ \
                                       http://remote-avocado-server:9405/jobs/
JOB ID     : 56016a1ffffaba02492fdbd5662ac0b958f51e11
JOB LOG    : /home/<user>/avocado/job-results/job-<date>-<shortid>/job.log
(1/2) http://local-avocado-server:9405/jobs/: PASS (0.02 s)
(2/2) http://remote-avocado-server:9405/jobs/: FAIL (3.02 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 1 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 3.14 s
JOB HTML   : /home/<user>/avocado/job-results/job-<date>-<shortid>/html/results.html
```

这有效地使`/bin/curl`成为"外部测试运行器"，负责尝试获取这些URL，并为每个URL报告PASS或FAIL。

### 调试测试

#### 显示测试输出

在开发新测试时，您经常希望直接查看作业日志，而无需切换屏幕或不必“拖尾”作业日志。

为了实现它，你可以使用`avocado --show test run ...` 或者 `avocado run --show-job-log`选项

```bash
$ avocado --show test run examples/tests/sleeptest.py
...
Job ID: f9ea1742134e5352dec82335af584d1f151d4b85

START 1-sleeptest.py:SleepTest.test

PARAMS (key=timeout, path=*, default=None) => None
PARAMS (key=sleep_length, path=*, default=1) => 1
Sleeping for 1.00 seconds
PASS 1-sleeptest.py:SleepTest.test

Test results available in $HOME/avocado/job-results/job-2015-06-02T10.45-f9ea174
```

如您所见，UI输出被抑制，只显示作业日志，这使其成为测试开发和调试的有用功能。


#### 中断测试执行

要中断作业执行，用户可以按`ctrl + c`，在单次按下后将SIGTERM发送到主测试的进程并等待它完成。如果这没有帮助，用户可以再次按`ctrl + c`（2s宽限期后），这会非常有效地破坏测试过程并安全地完成作业执行，始终提供测试结果。

要暂停测试执行，用户可以使用`ctrl + z`将SIGSTOP发送到从测试的PID继承的所有进程。我们尽力停止所有进程，但操作不是原子操作，可能无法停止某些新进程。再次按下`ctrl + z`将SIGCONT发送到测试的PID继承执行的所有进程。请注意，测试执行时间（关于测试超时）仍然在测试进程停止时运行。


Avocado功能也可以中断测试。一个例子是使用GDB调试GDB调试功能。

对于自定义交互，还可以使用其他方法，如pdb或pydevd Avocado开发提示断点。请注意，不能在测试中使用STDIN（除非使用黑暗魔法）。

## 书写Avocado测试

我们将用Python编写Avocado测试，我们将继承avocado.Test。 这使得该测试成为所谓的仪器测试。

### 基本示例

```python
import time

from avocado import Test

class SleepTest(Test):

    def test(self):
        sleep_length = self.params.get('sleep_length', default=1)
        self.log.debug("Sleeping for %.2f seconds", sleep_length)
        time.sleep(sleep_length)
```

这是您可以为Avocado编写的最简单的测试，同时仍然可以利用其API功能。

#### 什么是Avocado测试

从上面的示例中可以看出，Avocado测试是一种从继承自avocado.Test的类开始的测试方法。

#### 多个测试和命名约定

您可以在一个类中进行多个测试。

为此，只需给出以test开头的方法名称，比如`test_foo`，`test_bar`等等。 我们建议您遵循此命名样式，如PEP8函数名称部分中所定义。

对于类名，您可以选择任何您喜欢的名称，但我们也建议它遵循CamelCase约定，也称为CapWords，在类名称下的PEP 8文档中定义。


#### 便利属性

* 可以通过`self.log`访问测试的即用型日志机制。 它允许您记录调试，信息，错误和警告消息。
* 可以通过`self.params`访问的参数传递系统（和提取系统）。 这与Varianter有关，您可以在Testary参数中找到更多信息。
* 还有更多（参见avocado.core.test.Test）

为了最大限度地减少意外冲突，我们将公共冲突定义为属性，因此如果您看到类似`AttributeError: can't set attribute`就不要覆盖这些属性。

### 测试状态

Avocado支持最常见的退出状态:

* `PASS` - 测试通过，没有未经处理的例外情况
* `WARN` - PASS的一种变量，用于跟踪最终不会影响测试结果的值得注意的事件。 一个例子可能是dmesg输出中存在的软锁定。 它与测试结果无关，除非测试失败，否则意味着该功能可能按预期工作，但有一些条件可能很好审查。 （某些结果插件不支持此功能并报告PASS）
* `SKIP` - 测试的先决条件不满足且测试的主体未被执行（也没有执行setUp（）和tearDown）。
* `CANCEL` - 在setUp（），测试方法或tearDown（）期间某处取消了测试。 执行setUp（）和tearDown方法。
* `FAIL` - 测试未达到预期结果。 失败指向测试对象中的（可能的）错误，而不是测试脚本本身。 当测试（及其）执行中断时，报告ERROR而不是FAIL。
* `ERROR` - 这可能（可能）指向测试本身的一个错误，而不是在被测试的对象中。它通常是由未捕获的异常引起的，这种失败需要彻底探索并且应该导致测试修改以避免这种失败或者 使用self.fail以及描述测试中的对象如何无法执行它的任务。
* `INTERRUPTED` - 此结果无法由测试编写者设置，只有在超时或用户在执行此测试时按下`CTRL + C`时才会出现。
* other - 还有其他一些内部测试状态，但你应该不会遇到它们。


正如您所看到的那样，如果正确开发了测试，则FAIL是一个整洁的状态。在编写测试时，总要考虑它的`setUp`应该是什么，`test body`是什么，并且在测试中预计会出错。为了支持您，Avocado支持以下几种方法：


#### 测试方法

设置状态的最简单方法是直接从test中使用`self.fail`，`self.error`或`self.cancel`。

要记录警告，只需写入`self.log.warning`日志即可。这不会中断测试执行，但会记住条件，如果没有失败，则会将测试报告为`WARN`。

#### 将错误转化为失败

Python代码上的错误通常以抛出异常的形式发出信号。当Avocado运行测试时，任何未处理的异常都将被视为测试错误，而不是失败。

尽管如此，依赖库通常会引发自定义（或内置）异常。这些异常通常会导致错误，但如果您确定这是测试对象的奇怪行为，您应该捕获异常并解释self.fail方法中的失败：

```python
try:
    process.run("stress_my_feature")
except process.CmdError as details:
    self.fail("The stress comamnd failed: %s" % details)
```

如果你的测试组件有很多执行而你无法在其他情况下得到这个异常然后预期失败，你可以使用`fail_on`装饰器来简化代码：

```python
@avocado.fail_on(process.CmdError)
def test(self):
    process.run("first cmd")
    process.run("second cmd")
    process.run("third cmd")
```


再次，让您的测试脚本保持最新并区分`FAIL`和`ERROR`的区别,将在查看测试结果时节省大量时间。

### 保存测试生成的（自定义）数据

每个测试实例都提供一个所谓的`whiteboard`。它可以通过self.whiteboard访问。这个`whiteboard`只是一个字符串，在测试结束后会自动保存到测试结果中（在执行过程中没有同步，所以当机器或python严重崩溃时可能不存在，并且应该使用direct io直接输出到关键数据的输出）。如果您选择将二进制数据保存到`whiteboard`，则您有责任首先对其进行编码（base64是显而易见的选择）。

在之前演示的`sleeptest`测试的基础上，假设您想要保存`sleep length`以供其他一些脚本或数据分析工具使用：

```python
def test(self):
    sleep_length = self.params.get('sleep_length', default=1)
    self.log.debug("Sleeping for %.2f seconds", sleep_length)
    time.sleep(sleep_length)
    self.whiteboard = "%.2f" % sleep_length
```

`whiteboard`可以并且应该由可用的测试结果插件生成的文件公开。 results.json文件已包含每个测试的`whiteboard`。此外，为方便起见，我们将`whiteboard`内容的原始副本保存在名为whiteboard的文件中，与result.json文件位于同一级别（也许您希望直接使用基准测试结果与自定义脚本分析特定的基准测试结果）。

如果需要附加多个输出文件，还可以使用`self.outputdir`，它指向`$RESULTS/test-results/$ TEST_ID/data`位置，并保留用于任意测试结果数据。

### 访问测试数据文件

某些测试可能依赖于测试文件本身外部的数据文件。 Avocado提供了一个测试API，可以很容易地访问这些文件：`get_data（）` 。

对于Avocado测试（即INSTRUMENTED测试），`get_data（）`允许从最多三个源访问测试数据文件：

* 文件级数据目录：以测试文件命名但以.data结尾的目录。对于测试文件`/home/user/test.py`，文件级数据目录是`/home/user/test.py.data/`。

* 测试级别数据目录：以测试文件和特定测试名称命名的目录。当同一文件的不同测试部分需要不同的数据文件（具有相同或不同名称）时，这些功能非常有用。考虑到之前的`/home/user/test.py`示例，并假设它包含两个测试，`MyTest.test_foo`和`MyTest.test_bar`，测试级数据目录将是`/home/user/test.py.data/MyTest.test_foo/`和`home/user/test.py.data/MyTest.test_bar/`

* 变量级数据目录：如果在测试期间使用变量执行时，也会考虑以变量命名的目录寻找测试数据文件。对于测试文件`/home/user/test.py`，并测试`MyTest.test_foo`，带有变量`debug-ffff`，数据目录路径将是`/home/user/test.py.data/MyTest.test_foo/debug-ffff/`。

>>> 与INSTRUMENTED测试不同，SIMPLE测试仅定义`file`和`variant` 数据目录，因此是最具体的数据目录可能看起来像`/bin/echo.data/debug-ffff /`。


Avocado按照定义的顺序查找数据文件[`DATA_SOURCES`](api/core/avocado.core.html＃avocado.core.test.TestData.DATA_SOURCES)，这是从最具体的一个到最通用的一个。这意味着，如果是变量正在使用，首先使用variant目录。然后测试尝试测试级别目录，最后是文件级目录。

另外，你可以使用`get_data（filename，must_exist = False）`来获取可能不存在的文件的预期位置，这在当你打算创建它的情况下很有用。

>>> 运行测试时，您可以使用`--log-test-data-directories`命令行选项记录将使用的测试数据目录
对于特定的测试和执行条件（例如使用或没有变种）。在测试日志中查找“测试数据目录”。

>>>以前存在的API`avocado.core.test.Test.datadir`，用于允许基于测试文件访问数据目录仅限位置。此API已被删除。无论出于何种原因，您仍然只需要根据测试文件位置访问数据目录，可以使用`get_data（filename =''，source ='file'，must_exist = False）`。

### 访问测试参数

每个测试都有一组可以访问的参数`self.params.get（$ name，$ path = None，$ default = None）`其中：

* name - 参数名称（键）
* path - 查找此参数的位置（未指定时使用mux-path）
* default - 未找到param时返回的内容

路径是有点棘手。 Avocado使用树来表示参数。 在简单的场景中，您不必担心，您将在默认情况下找到所有值的路径，但最终你可能想要查询Test parameters来理解细节。

假设您的测试收到以下参数（您将在下一节中学习如何执行它们）：

```
$ avocado variants -m examples/tests/sleeptenmin.py.data/sleeptenmin.yaml --variants 2
...
Variant 1:    /run/sleeptenmin/builtin, /run/variants/one_cycle
    /run/sleeptenmin/builtin:sleep_method => builtin
    /run/variants/one_cycle:sleep_cycles  => 1
    /run/variants/one_cycle:sleep_length  => 600
...
```

在测试中你可以通过以下方式访问这些参数：

```python
self.params.get("sleep_method")    # returns "builtin"
self.params.get("sleep_cycles", '*', 10)    # returns 1
self.params.get("sleep_length", "/*/variants/*")  # returns 600
```

>>> 在可能发生冲突的复杂场景中，该路径很重要，因为当存在多个具有相同键匹配值的值时，Avocado会引发异常。如上所述，您可以通过使用特定路径或通过定义允许指定解析层次结构的自定义mux-path来避免这些路径。 更多细节可以在测试参数中找到。

### 运行多个测试变量

在上一节中，我们描述了如何处理参数。 现在，让我们看看如何生成它们并使用不同的参数执行测试。

变量子系统允许创建多个参数变量,并使用这些参数变量执行测试。此子系统是可插入的，因此您可以使用自定义插件来生成变量。为了简单起见，让我们使用Avocado的初步实施，称为`yaml_to_mux`。

`yaml_to_mux`插件接受YAML文件。 这些将创建树状结构，将变量存储为参数并使用自定义标记将位置标记为`multiplex`域。

让我们使用`examples/tests/sleeptenmin.py.data/sleeptenmin.yaml`文件作为例子：

```yaml
sleeptenmin: !mux
    builtin:
        sleep_method: builtin
    shell:
        sleep_method: shell
variants: !mux
    one_cycle:
        sleep_cycles: 1
        sleep_length: 600
    six_cycles:
        sleep_cycles: 6
        sleep_length: 100
    one_hundred_cycles:
        sleep_cycles: 100
        sleep_length: 6
    six_hundred_cycles:
        sleep_cycles: 600
        sleep_length: 1
```

其中产生以下结构和参数：

```bash
$ avocado variants -m examples/tests/sleeptenmin.py.data/sleeptenmin.yaml --summary 2 --variants 2
Multiplex tree representation:
 ┗━━ run
      ┣━━ sleeptenmin
      ┃    ╠══ builtin
      ┃    ║     → sleep_method: builtin
      ┃    ╚══ shell
      ┃          → sleep_method: shell
      ┗━━ variants
           ╠══ one_cycle
           ║     → sleep_length: 600
           ║     → sleep_cycles: 1
           ╠══ six_cycles
           ║     → sleep_length: 100
           ║     → sleep_cycles: 6
           ╠══ one_hundred_cycles
           ║     → sleep_length: 6
           ║     → sleep_cycles: 100
           ╚══ six_hundred_cycles
                 → sleep_length: 1
                 → sleep_cycles: 600

Multiplex variants (8):

Variant builtin-one_cycle-f659:    /run/sleeptenmin/builtin, /run/variants/one_cycle
    /run/sleeptenmin/builtin:sleep_method => builtin
    /run/variants/one_cycle:sleep_cycles  => 1
    /run/variants/one_cycle:sleep_length  => 600

Variant builtin-six_cycles-723b:    /run/sleeptenmin/builtin, /run/variants/six_cycles
    /run/sleeptenmin/builtin:sleep_method => builtin
    /run/variants/six_cycles:sleep_cycles => 6
    /run/variants/six_cycles:sleep_length => 100

Variant builtin-one_hundred_cycles-633a:    /run/sleeptenmin/builtin, /run/variants/one_hundred_cycles
    /run/sleeptenmin/builtin:sleep_method         => builtin
    /run/variants/one_hundred_cycles:sleep_cycles => 100
    /run/variants/one_hundred_cycles:sleep_length => 6

Variant builtin-six_hundred_cycles-a570:    /run/sleeptenmin/builtin, /run/variants/six_hundred_cycles
    /run/sleeptenmin/builtin:sleep_method         => builtin
    /run/variants/six_hundred_cycles:sleep_cycles => 600
    /run/variants/six_hundred_cycles:sleep_length => 1

Variant shell-one_cycle-55f5:    /run/sleeptenmin/shell, /run/variants/one_cycle
    /run/sleeptenmin/shell:sleep_method  => shell
    /run/variants/one_cycle:sleep_cycles => 1
    /run/variants/one_cycle:sleep_length => 600

Variant shell-six_cycles-9e23:    /run/sleeptenmin/shell, /run/variants/six_cycles
    /run/sleeptenmin/shell:sleep_method   => shell
    /run/variants/six_cycles:sleep_cycles => 6
    /run/variants/six_cycles:sleep_length => 100

Variant shell-one_hundred_cycles-586f:    /run/sleeptenmin/shell, /run/variants/one_hundred_cycles
    /run/sleeptenmin/shell:sleep_method           => shell
    /run/variants/one_hundred_cycles:sleep_cycles => 100
    /run/variants/one_hundred_cycles:sleep_length => 6

Variant shell-six_hundred_cycles-1e84:    /run/sleeptenmin/shell, /run/variants/six_hundred_cycles
    /run/sleeptenmin/shell:sleep_method           => shell
    /run/variants/six_hundred_cycles:sleep_cycles => 600
    /run/variants/six_hundred_cycles:sleep_length => 1
```

您可以看到它创建了每个Multiplex域的所有可能变量，这些变量由YAML文件中的！mux标记定义，并在树视图中显示为单行（与具有值的单个节点的双行比较）。 总共它会产生每种测试的8种变量：

```
$ avocado run --mux-yaml examples/tests/sleeptenmin.py.data/sleeptenmin.yaml -- passtest.py
JOB ID     : cc7ef22654c683b73174af6f97bc385da5a0f02f
JOB LOG    : /home/medic/avocado/job-results/job-2017-01-22T11.26-cc7ef22/job.log
 (1/8) passtest.py:PassTest.test;builtin-one_cycle-f659: PASS (0.01 s)
 (2/8) passtest.py:PassTest.test;builtin-six_cycles-723b: PASS (0.01 s)
 (3/8) passtest.py:PassTest.test;builtin-one_hundred_cycles-633a: PASS (0.01 s)
 (4/8) passtest.py:PassTest.test;builtin-six_hundred_cycles-a570: PASS (0.01 s)
 (5/8) passtest.py:PassTest.test;shell-one_cycle-55f5: PASS (0.01 s)
 (6/8) passtest.py:PassTest.test;shell-six_cycles-9e23: PASS (0.01 s)
 (7/8) passtest.py:PassTest.test;shell-one_hundred_cycles-586f: PASS (0.01 s)
 (8/8) passtest.py:PassTest.test;shell-six_hundred_cycles-1e84: PASS (0.01 s)
RESULTS    : PASS 8 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.16 s
```
### 高级日志记录功能

Avocado在测试运行时提供高级日志记录功能。 这些可以在测试中与标准Python库API结合使用。

一个常见的例子是需要在更长或更复杂的测试中遵循特定的进展。 让我们看一个非常简单的测试示例，但在单个测试中有一个多个明确的阶段：

```python
import logging
import time

from avocado import Test

progress_log = logging.getLogger("progress")

class Plant(Test):

    def test_plant_organic(self):
        rows = self.params.get("rows", default=3)

        # Preparing soil
        for row in range(rows):
            progress_log.info("%s: preparing soil on row %s",
                              self.name, row)

        # Letting soil rest
        progress_log.info("%s: letting soil rest before throwing seeds",
                          self.name)
        time.sleep(2)

        # Throwing seeds
        for row in range(rows):
            progress_log.info("%s: throwing seeds on row %s",
                              self.name, row)

        # Let them grow
        progress_log.info("%s: waiting for Avocados to grow",
                          self.name)
        time.sleep(5)

        # Harvest them
        for row in range(rows):
            progress_log.info("%s: harvesting organic avocados on row %s",
                              self.name, row)
```

从现在开始，您可以要求Avocado显示您的日志记录流，无论是独占还是其他内置流：

```bash
$ avocado --show app,progress run plant.py
```
结果应类似于：

```
JOB ID     : af786f86db530bff26cd6a92c36e99bedcdca95b
JOB LOG    : /home/cleber/avocado/job-results/job-2016-03-18T10.29-af786f8/job.log
 (1/1) plant.py:Plant.test_plant_organic: progress: 1-plant.py:Plant.test_plant_organic: preparing soil on row 0
progress: 1-plant.py:Plant.test_plant_organic: preparing soil on row 1
progress: 1-plant.py:Plant.test_plant_organic: preparing soil on row 2
progress: 1-plant.py:Plant.test_plant_organic: letting soil rest before throwing seeds
-progress: 1-plant.py:Plant.test_plant_organic: throwing seeds on row 0
progress: 1-plant.py:Plant.test_plant_organic: throwing seeds on row 1
progress: 1-plant.py:Plant.test_plant_organic: throwing seeds on row 2
progress: 1-plant.py:Plant.test_plant_organic: waiting for Avocados to grow
\progress: 1-plant.py:Plant.test_plant_organic: harvesting organic avocados on row 0
progress: 1-plant.py:Plant.test_plant_organic: harvesting organic avocados on row 1
progress: 1-plant.py:Plant.test_plant_organic: harvesting organic avocados on row 2
PASS (7.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 7.11 s
JOB HTML   : /home/cleber/avocado/job-results/job-2016-03-18T10.29-af786f8/html/results.html
```

自定义`progress`流与应用程序输出结合在一起,可能适合或可能不适合您的需要或喜好。 如果你为了清楚和持久性，想把`progress`流将发送到一个单独的文件，你可以像这样运行Avocado：

```bash
$ avocado run plant.py --store-logging-stream progress
```
结果是，除了通常生成的所有其他日志文件之外，还会在作业结果目录中有另一个名为progress.INFO的日志文件。 在测试运行期间，可以通过以下方式观察进度：

```
$ tail -f ~/avocado/job-results/latest/progress.INFO
10:36:59 INFO | 1-plant.py:Plant.test_plant_organic: preparing soil on row 0
10:36:59 INFO | 1-plant.py:Plant.test_plant_organic: preparing soil on row 1
10:36:59 INFO | 1-plant.py:Plant.test_plant_organic: preparing soil on row 2
10:36:59 INFO | 1-plant.py:Plant.test_plant_organic: letting soil rest before throwing seeds
10:37:01 INFO | 1-plant.py:Plant.test_plant_organic: throwing seeds on row 0
10:37:01 INFO | 1-plant.py:Plant.test_plant_organic: throwing seeds on row 1
10:37:01 INFO | 1-plant.py:Plant.test_plant_organic: throwing seeds on row 2
10:37:01 INFO | 1-plant.py:Plant.test_plant_organic: waiting for Avocados to grow
10:37:06 INFO | 1-plant.py:Plant.test_plant_organic: harvesting organic avocados on row 0
10:37:06 INFO | 1-plant.py:Plant.test_plant_organic: harvesting organic avocados on row 1
10:37:06 INFO | 1-plant.py:Plant.test_plant_organic: harvesting organic avocados on row 2
```

这个非常相似的progress logger，可以跨多个测试方法和多个测试模块使用。在给出的示例中，测试名称用于提供额外的上下文。


### unittest.TestCase继承

由于Avocado测试继承了unittest.TestCase，所以可以使用其父级的所有断言方法。
代码示例使用 assertEqual, assertTrue 和 assertIsInstace:

```python
from avocado import Test

class RandomExamples(Test):
    def test(self):
        self.log.debug("Verifying some random math...")
        four = 2 * 2
        four_ = 2 + 2
        self.assertEqual(four, four_, "something is very wrong here!")

        self.log.debug("Verifying if a variable is set to True...")
        variable = True
        self.assertTrue(variable)

        self.log.debug("Verifying if this test is an instance of test.Test")
        self.assertIsInstance(self, test.Test)
```
#### 在其它单元测试下运行测试脚本

nose是另一个Python测试框架，它也与unittest兼容。
因此，您可以使用nosetest应用程序运行Avocado测试：

```
$ nosetests examples/tests/sleeptest.py
.
----------------------------------------------------------------------
Ran 1 test in 1.004s

OK
```

相反，您也可以使用标准unittest.main()入口点运行Avocado测试。检查下面的代码，以保存为dummy.py：

```python
from avocado import Test
from unittest import main

class Dummy(Test):
    def test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    main()
```

使用:

```python
$ python dummy.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

### Setup和cleanup方法

在测试之前或之后执行setUp操作，您可以使用setUp和tearDown方法,tearDown方法总是在安装失败时执行，所以不要忘记在setUp过程中初始化变量。使用示例在下一节运行第三方测试套件中。

### 运行第三方测试套件

在测试自动化工作负载中使用第三方开发的测试套件非常常见。通过在Avocado测试模块中封装执行代码，您可以访问框架提供的设施和API。假设你想用C写一个测试套件，它在一个tarball中，解压缩它，编译套件代码，然后执行测试。下面是一个例子：

```python
#!/usr/bin/env python

import os

from avocado import Test
from avocado import main
from avocado.utils import archive
from avocado.utils import build
from avocado.utils import process


class SyncTest(Test):

    """
    Execute the synctest test suite.
    """
    def setUp(self):
        """
        Set default params and build the synctest suite.
        """
        sync_tarball = self.params.get('sync_tarball',
                                       default='synctest.tar.bz2')
        self.sync_length = self.params.get('sync_length', default=100)
        self.sync_loop = self.params.get('sync_loop', default=10)
        # Build the synctest suite
        self.cwd = os.getcwd()
        tarball_path = self.get_data(sync_tarball)
        archive.extract(tarball_path, self.workdir)
        self.workdir = os.path.join(self.workdir, 'synctest')
        build.make(self.workdir)

    def test(self):
        """
        Execute synctest with the appropriate params.
        """
        os.chdir(self.workdir)
        cmd = ('./synctest %s %s' %
               (self.sync_length, self.sync_loop))
        process.system(cmd)
        os.chdir(self.cwd)


if __name__ == "__main__":
    main()
```

这里我们有一个setup方法的例子：这里我们通过`avocado.Test.get_data()` 得到测试套件代码（tarball）的位置。然后通过`avocado.utils.archive.extract()`解压缩
一个API会解压缩tarball套件,`avocado.utils.build.make()`会建立则个套件。

在这个例子中，测试方法刚刚进入编译的套件的基本目录，并使用`avocado.utils.process.system()`和适当的参数执行`./synctest`命令。

### 获取资产文件
### 测试输出检查和输出记录模式

在很多情况下，你想变得简单：只需检查给定测试的输出是否匹配预期输出。为了帮助这个常见的用例，Avocado提供了`--output-check-record`选项

如果启用这个选项，Avocado将会将测试生成的内容保存到标准（POSIX）流，即`STDOUT` 和 `STDERR`.根据所选的选项，您可能会记录不同的文件（我们称之为“参考文件”）：

* `stdout`将生成一个名为`stdout.expected`的文件，该文件包含来自测试过程标准输出流（文件描述符1）的内容。
* `stderr`将生成一个名为`stderr.expected`的文件，该文件包含来自测试过程标准错误流（文件描述符2）的内容。
* `both`将生成一个名为`stdout.expected`和一个名为`stderr.expected`的文件
* `combined`将生成一个名为`output.expected`的文件，其中包含测试过程标准输出和错误流（文件描述符1和2）的内容。
* `none`将显式禁用测试生成的输出和生成内容的生成参考文件的所有记录

参考文件将被记录在第一个（最特定的）测试数据文件夹（访问测试数据文件）中。让我们以测试`synctest.py`为例。检查Avocado源代码，您可以找到以下参考文件：

```
examples/tests/synctest.py.data/stderr.expected
examples/tests/synctest.py.data/stdout.expected
```

在这两个文件中，只有stdout.expected有些内容

```
$ cat examples/tests/synctest.py.data/stdout.expected
PAR : waiting
PASS : sync interrupted
```

这意味着，在之前的测试执行期间，用`--output-check-record both`进行输出记录，并且仅在stdout流上生成内容：

```
$ avocado run --output-check-record both synctest.py
JOB ID     : b6306504351b037fa304885c0baa923710f34f4a
JOB LOG    : $JOB_RESULTS_DIR/job-2017-11-26T16.42-b630650/job.log
 (1/1) examples/tests/synctest.py:SyncTest.test: PASS (2.03 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 0
JOB TIME   : 2.26 s
```
在添加参考文件之后，检查过程是透明的，从某种意义上说，您不需要向test runner提供特殊标志。从这一点开始，在测试（一个带有参考文件记录的一个）完成运行之后，鳄梨将检查输出是否与参考文件内容匹配。如果它们不匹配，则测试将以失败状态结束。

当引用文件存在时，你也可以对此测试运行程序禁用自动检查`--output-check=off`对此测试运行程序。

这个过程还可以也可以在简单测试，也就是返回0 (PASSed) or != 0 (FAILed)的程序或或shell脚本工作的很好。让我们考虑例子：

```
$ cat output_record.sh
#!/bin/bash
echo "Hello, world!"
```
让我们记录下这个的输出：

```
$ scripts/avocado run output_record.sh --output-check-record all
JOB ID    : 25c4244dda71d0570b7f849319cd71fe1722be8b
JOB LOG   : $HOME/avocado/job-results/job-2014-09-25T20.49-25c4244/job.log
 (1/1) output_record.sh: PASS (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.11 s
```
完成此操作后，您会注意到测试数据目录出现在我们的shell脚本的同一个级别，包含2个文件：

```
$ ls output_record.sh.data/
stderr.expected  stdout.expected
```
让我们看看它们中的内容：

```
$ cat output_record.sh.data/stdout.expected
Hello, world!
$ cat output_record.sh.data/stderr.expected
$
```

现在，每次测试运行时，程序都会自动对比记录的预期文件，我们不需要做任何其他操作。让我们看看如果把STDUT.期望的文件内容改为Hello,avocado 会发生什么呢？：

```
$ scripts/avocado run output_record.sh
JOB ID    : f0521e524face93019d7cb99c5765aedd933cb2e
JOB LOG   : $HOME/avocado/job-results/job-2014-09-25T20.52-f0521e5/job.log
 (1/1) output_record.sh: FAIL (0.02 s)
RESULTS    : PASS 0 | ERROR 0 | FAIL 1 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.12 s
```

确认失败的原因：

```
$ cat $HOME/avocado/job-results/latest/job.log
    2017-10-16 14:23:02,567 test             L0381 INFO | START 1-output_record.sh
    2017-10-16 14:23:02,568 test             L0402 DEBUG| Test metadata:
    2017-10-16 14:23:02,568 test             L0403 DEBUG|   filename: $HOME/output_record.sh
    2017-10-16 14:23:02,596 process          L0389 INFO | Running '$HOME/output_record.sh'
    2017-10-16 14:23:02,603 process          L0499 INFO | Command '$HOME/output_record.sh' finished with 0 after 0.00131011009216s
    2017-10-16 14:23:02,602 process          L0479 DEBUG| [stdout] Hello, world!
    2017-10-16 14:23:02,603 test             L1084 INFO | Exit status: 0
    2017-10-16 14:23:02,604 test             L1085 INFO | Duration: 0.00131011009216
    2017-10-16 14:23:02,604 test             L0274 DEBUG| DATA (filename=stdout.expected) => $HOME/output_record.sh.data/stdout.expected (found at file source dir)
    2017-10-16 14:23:02,605 test             L0740 DEBUG| Stdout Diff:
    2017-10-16 14:23:02,605 test             L0742 DEBUG| --- $HOME/output_record.sh.data/stdout.expected
    2017-10-16 14:23:02,605 test             L0742 DEBUG| +++ $HOME/avocado/job-results/job-2017-10-16T14.23-8cba866/test-results/1-output_record.sh/stdout
    2017-10-16 14:23:02,605 test             L0742 DEBUG| @@ -1 +1 @@
    2017-10-16 14:23:02,605 test             L0742 DEBUG| -Hello, Avocado!
    2017-10-16 14:23:02,605 test             L0742 DEBUG| +Hello, world!
    2017-10-16 14:23:02,606 stacktrace       L0041 ERROR|
    2017-10-16 14:23:02,606 stacktrace       L0044 ERROR| Reproduced traceback from: $HOME/git/avocado/avocado/core/test.py:872
    2017-10-16 14:23:02,606 stacktrace       L0047 ERROR| Traceback (most recent call last):
    2017-10-16 14:23:02,606 stacktrace       L0047 ERROR|   File "$HOME/git/avocado/avocado/core/test.py", line 743, in _check_reference_stdout
    2017-10-16 14:23:02,606 stacktrace       L0047 ERROR|     self.fail('Actual test sdtout differs from expected one')
    2017-10-16 14:23:02,606 stacktrace       L0047 ERROR|   File "$HOME//git/avocado/avocado/core/test.py", line 983, in fail
    2017-10-16 14:23:02,607 stacktrace       L0047 ERROR|     raise exceptions.TestFail(message)
    2017-10-16 14:23:02,607 stacktrace       L0047 ERROR| TestFail: Actual test sdtout differs from expected one
    2017-10-16 14:23:02,607 stacktrace       L0048 ERROR|
    2017-10-16 14:23:02,607 test             L0274 DEBUG| DATA (filename=stderr.expected) => $HOME//output_record.sh.data/stderr.expected (found at file source dir)
    2017-10-16 14:23:02,608 test             L0965 ERROR| FAIL 1-output_record.sh -> TestFail: Actual test sdtout differs from expected one
```

正如预期的那样，测试失败了，因为我们改变了它的期望，因此记录了一个统一的差异。统一的差异也存在于文件`stdout.diff` 和 `stderr.diff`中，存在于测试结果目录中：

```
$ cat $HOME/avocado/job-results/latest/test-results/1-output_record.sh/stdout.diff
--- $HOME/output_record.sh.data/stdout.expected
+++ $HOME/avocado/job-results/job-2017-10-16T14.23-8cba866/test-results/1-output_record.sh/stdout
@@ -1 +1 @@
-Hello, Avocado!
+Hello, world!
```

>>> 目前，stdout和stder都以文本方式存储。根据当前区域设置无法解码的数据将根据 https://docs.python.org/3/library/codecs.html#codecs.replace_errors 替换
### 在本机Avocado模块中测试日志，stdout和stderr

如果需要，可以直接从原生测试范围写入预期的stdout和stderr文件。区分以下实体是很重要的：

* The test logs
* The test expected stdout 期待的标准输出
* The test expected stderr 期待的标准错误

第一个是用于调试和输出信息的目的。另外，写入`self.log.warning`会导致测试被标记为dirty，当一切顺利时，测试以警告结束。这意味着测试通过了，但是在警告日志中描述了非相关的意外情况。

您可以使用`avocado.test.log`类属性中的方法将一些日志记录到测试日志中。考虑这个例子：

```python
class output_test(Test):

    def test(self):
        self.log.info('This goes to the log and it is only informational')
        self.log.warn('Oh, something unexpected, non-critical happened, '
                      'but we can continue.')
        self.log.error('Describe the error here and don\'t forget to raise '
                       'an exception yourself. Writing to self.log.error '
                       'won\'t do that for you.')
        self.log.debug('Everybody look, I had a good lunch today...')
```

如果您需要直接写入测试stdout和stderr流，Avocado使两个预先配置的日志记录器可用于此目的，名为`avocado.test.stdout`和`avocado.test.stderr`。可以使用Python的标准日志API来对它们进行写入。例子：

```python
import logging

class output_test(Test):

    def test(self):
        stdout = logging.getLogger('avocado.test.stdout')
        stdout.info('Informational line that will go to stdout')
        ...
        stderr = logging.getLogger('avocado.test.stderr')
        stderr.info('Informational line that will go to stderr')
```
Avocado将自动保存测试在STDUT中生成的任何东西到stdout文件中，在测试结果目录中找到。这同样适用于测试在STDRR上生成的任何东西，也就是说，它将被保存到同一个位置的stderr文件中。

此外，当使用runner的输出记录特性，即` --output-check-record `参数值stdout, stderr或者all时，所有给这些记录器的所有内容都将保存到文`stdout.expected`和`stderr.expected`在测试数据目录中（与`job/test results`不同）。

### 设置测试超时

有时您的测试套件/测试可能会被永久卡住，这可能会影响测试网格。您可以解释这种可能性，并为测试设置超时参数。测试超时可以通过测试参数来设置，如下所示。

```
sleep_length: 5
timeout: 3
```

```
$ avocado run sleeptest.py --mux-yaml /tmp/sleeptest-example.yaml
JOB ID     : c78464bde9072a0b5601157989a99f0ba32a288e
JOB LOG    : $HOME/avocado/job-results/job-2016-11-02T11.13-c78464b/job.log
 (1/1) sleeptest.py:SleepTest.test: INTERRUPTED (3.04 s)
RESULTS    : PASS 0 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 1
JOB TIME   : 3.14 s
JOB HTML   : $HOME/avocado/job-results/job-2016-11-02T11.13-c78464b/html/results.html
```

```
$ cat $HOME/avocado/job-results/job-2016-11-02T11.13-c78464b/job.log
2016-11-02 11:13:01,133 job              L0384 INFO | Multiplex tree representation:
2016-11-02 11:13:01,133 job              L0386 INFO |  \-- run
2016-11-02 11:13:01,133 job              L0386 INFO |         -> sleep_length: 5
2016-11-02 11:13:01,133 job              L0386 INFO |         -> timeout: 3
2016-11-02 11:13:01,133 job              L0387 INFO |
2016-11-02 11:13:01,134 job              L0391 INFO | Temporary dir: /var/tmp/avocado_PqDEyC
2016-11-02 11:13:01,134 job              L0392 INFO |
2016-11-02 11:13:01,134 job              L0399 INFO | Variant 1:    /run
2016-11-02 11:13:01,134 job              L0402 INFO |
2016-11-02 11:13:01,134 job              L0311 INFO | Job ID: c78464bde9072a0b5601157989a99f0ba32a288e
2016-11-02 11:13:01,134 job              L0314 INFO |
2016-11-02 11:13:01,345 sysinfo          L0107 DEBUG| Not logging /proc/pci (file does not exist)
2016-11-02 11:13:01,351 sysinfo          L0105 DEBUG| Not logging /proc/slabinfo (lack of permissions)
2016-11-02 11:13:01,355 sysinfo          L0107 DEBUG| Not logging /sys/kernel/debug/sched_features (file does not exist)
2016-11-02 11:13:01,388 sysinfo          L0388 INFO | Commands configured by file: /etc/avocado/sysinfo/commands
2016-11-02 11:13:01,388 sysinfo          L0399 INFO | Files configured by file: /etc/avocado/sysinfo/files
2016-11-02 11:13:01,388 sysinfo          L0419 INFO | Profilers configured by file: /etc/avocado/sysinfo/profilers
2016-11-02 11:13:01,388 sysinfo          L0427 INFO | Profiler disabled
2016-11-02 11:13:01,394 multiplexer      L0166 DEBUG| PARAMS (key=timeout, path=*, default=None) => 3
2016-11-02 11:13:01,395 test             L0216 INFO | START 1-sleeptest.py:SleepTest.test
2016-11-02 11:13:01,396 multiplexer      L0166 DEBUG| PARAMS (key=sleep_length, path=*, default=1) => 5
2016-11-02 11:13:01,396 sleeptest        L0022 DEBUG| Sleeping for 5.00 seconds
2016-11-02 11:13:04,411 stacktrace       L0038 ERROR|
2016-11-02 11:13:04,412 stacktrace       L0041 ERROR| Reproduced traceback from: $HOME/src/avocado/avocado/core/test.py:454
2016-11-02 11:13:04,412 stacktrace       L0044 ERROR| Traceback (most recent call last):
2016-11-02 11:13:04,413 stacktrace       L0044 ERROR|   File "/usr/share/doc/avocado/tests/sleeptest.py", line 23, in test
2016-11-02 11:13:04,413 stacktrace       L0044 ERROR|     time.sleep(sleep_length)
2016-11-02 11:13:04,413 stacktrace       L0044 ERROR|   File "$HOME/src/avocado/avocado/core/runner.py", line 293, in sigterm_handler
2016-11-02 11:13:04,413 stacktrace       L0044 ERROR|     raise SystemExit("Test interrupted by SIGTERM")
2016-11-02 11:13:04,414 stacktrace       L0044 ERROR| SystemExit: Test interrupted by SIGTERM
2016-11-02 11:13:04,414 stacktrace       L0045 ERROR|
2016-11-02 11:13:04,414 test             L0459 DEBUG| Local variables:
2016-11-02 11:13:04,440 test             L0462 DEBUG|  -> self <class 'sleeptest.SleepTest'>: 1-sleeptest.py:SleepTest.test
2016-11-02 11:13:04,440 test             L0462 DEBUG|  -> sleep_length <type 'int'>: 5
2016-11-02 11:13:04,440 test             L0592 ERROR| ERROR 1-sleeptest.py:SleepTest.test -> TestError: SystemExit('Test interrupted by SIGTERM',): Test interrupted by SIGTERM
```

YAML文件定义了一个测试参数超时，它在运行程序结束之前，通过发送一个类`:signal.SIGTERM`到测试，raise错误`avocado.core.exceptions.TestTimeoutError`，从而提高了测试速度。

### 跳过测试

要在Avocado中跳过测试，必须使用Avocado跳过装饰器中的一种：

* `@avocado.skip(reason)`: 跳过测试.
* `@avocado.skipIf(condition, reason)`: 跳过测试如果条件为`True`.
* `@avocado.skipUnless(condition, reason)`: 跳过测试如果条件为 `False`

这些装饰器可以同时使用`setup`方法和`Test*()`方法中使用。测试如下：

```python
import avocado

class MyTest(avocado.Test):

    @avocado.skipIf(1 == 1, 'Skipping on True condition.')
    def test1(self):
        pass

    @avocado.skip("Don't want this test now.")
    def test2(self):
        pass

    @avocado.skipUnless(1 == 1, 'Skipping on False condition.')
    def test3(self):
        pass
```
将产生以下结果：

```python
$ avocado run  test_skip_decorators.py
JOB ID     : 59c815f6a42269daeaf1e5b93e52269fb8a78119
JOB LOG    : $HOME/avocado/job-results/job-2017-02-03T17.41-59c815f/job.log
 (1/3) test_skip_decorators.py:MyTest.test1: SKIP
 (2/3) test_skip_decorators.py:MyTest.test2: SKIP
 (3/3) test_skip_decorators.py:MyTest.test3: PASS (0.02 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 2 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.13 s
JOB HTML   : $HOME/avocado/job-results/job-2017-02-03T17.41-59c815f/html/results.html
```
注意，由于提供的条件不是false，所以没有跳过Test3。

使用跳过装饰器，实际上没有执行任何操作。我们将跳过`setup`方法、测试方法和`teardown`方法。

>>> 任何skip装饰器都不能在teardown方法上使用,否则会出现错误,状态吗为`ERROR`

### 取消测试
您可以在测试的任何阶段（`setup()`、测试方法或`teardown`）中调用`self.cancel()`取消测试。测试将以取消状态结束，并且不会使job以非0状态退出。例子：

```python
from avocado import Test
from avocado import main

from avocado.utils.process import run
from avocado.utils.software_manager import SoftwareManager


class CancelTest(Test):

    """
    Example tests that cancel the current test from inside the test.
    """

    def setUp(self):
        sm = SoftwareManager()
        self.pkgs = sm.list_all(software_components=False)

    def test_iperf(self):
        if 'iperf-2.0.8-6.fc25.x86_64' not in self.pkgs:
            self.cancel('iperf is not installed or wrong version')
        self.assertIn('pthreads',
                      run('iperf -v', ignore_status=True).stderr)

    def test_gcc(self):
        if 'gcc-6.3.1-1.fc25.x86_64' not in self.pkgs:
            self.cancel('gcc is not installed or wrong version')
        self.assertIn('enable-gnu-indirect-function',
                      run('gcc -v', ignore_status=True).stderr)

if __name__ == "__main__":
    main()
```

在缺少IPRF包但系统安装在正确版本中的系统中，结果将是：

```
JOB ID     : 39c1f120830b9769b42f5f70b6b7bad0b1b1f09f
JOB LOG    : $HOME/avocado/job-results/job-2017-03-10T16.22-39c1f12/job.log
 (1/2) /home/apahim/avocado/tests/test_cancel.py:CancelTest.test_iperf: CANCEL (1.15 s)
 (2/2) /home/apahim/avocado/tests/test_cancel.py:CancelTest.test_gcc: PASS (1.13 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 1
JOB TIME   : 2.38 s
JOB HTML   : $HOME/avocado/job-results/job-2017-03-10T16.22-39c1f12/html/results.html
```

注意，使用`self.cancel()`将从该点取消其余的测试，但是`teardown()`仍将被执行。

根据您所提到的结果格式，取消状态被映射到相应格式的有效状态。见下表：

| Format | Corresponding Status |
|--------|----------------------|
| json   | cancel               |
| xunit  | skipped              |
| tap    | ok                   |
| html   | CANCEL (warning)     |

### Docstring指令

一些Avododo特性，通常只适用于仪器化测试，依赖于在测试类的DoScord中设置指令。DOXString指令由标记（`:avocado:`）组成，接着是自定义内容本身，如`:avocado: directive`。

这与DoScript指令类似，例如`:param my_param: description`对于大多数Python开发人员来说，这应该不是一个意外。

Avocado使用这些DOSCRON指令（而不是真正的Python代码）的原因是，在寻找测试时进行的检查不涉及代码的任何执行。

有关DoScript格式的有效性的详细解释，请参阅我们关于DOSCSHIPE指令规则的章节。

现在让我们继续使用一些DoScript指令示例。

#### 显式启用或禁用测试

如果您的测试是直接从`avocado.Test`继承的类中的一个方法，那么avocado会像预期的那样找到它。

现在，可能需要更复杂的测试，使用更先进的Python特性，例如继承。对于那些不直接从`avocado.Test`中继承的测试，Avocado可能需要你的帮助，因为Avocado只使用静态分析来检查文件。

例如，假设您定义了一个新的测试类，该类继承了avocado基础测试类，即`avocado.Test`，并将其放入`mylibrary.py`：

```python
from avocado import Test


class MyOwnDerivedTest(Test):
    def __init__(self, methodName='test', name=None, params=None,
                 base_logdir=None, job=None, runner_queue=None):
        super(MyOwnDerivedTest, self).__init__(methodName, name, params,
                                               base_logdir, job,
                                               runner_queue)
        self.log('Derived class example')
```
然后在`mytest.py`中使用该派生类实现实际测试：

```python
import mylibrary


class MyTest(mylibrary.MyOwnDerivedTest):

    def test1(self):
        self.log('Testing something important')

    def test2(self):
        self.log('Testing something even more important')
```

如果您试图列出该文件中的测试，这将是您将得到的：

```
scripts/avocado list mytest.py -V
Type       Test      Tag(s)
NOT_A_TEST mytest.py

TEST TYPES SUMMARY
==================
ACCESS_DENIED: 0
BROKEN_SYMLINK: 0
EXTERNAL: 0
FILTERED: 0
INSTRUMENTED: 0
MISSING: 0
NOT_A_TEST: 1
SIMPLE: 0
VT: 0
```

你需要通过添加一个docstring指令来给Avocado一点帮助。docstring指令是：`:avocado: enable`。它告诉Avocado安全测试检测代码，将其视为Avocado试验，而不管检测代码对它的看法如何。让我们看看效果如何。添加docstring，如下所示：

```python
import mylibrary

class MyTest(mylibrary.MyOwnDerivedTest):
    """
    :avocado: enable
    """
    def test1(self):
        self.log('Testing something important')

    def test2(self):
        self.log('Testing something even more important')
```
再次尝试列出该文件中的测试：

```
scripts/avocado list mytest.py -V
Type         Test                   Tag(s)
INSTRUMENTED mytest.py:MyTest.test1
INSTRUMENTED mytest.py:MyTest.test2

TEST TYPES SUMMARY
==================
ACCESS_DENIED: 0
BROKEN_SYMLINK: 0
EXTERNAL: 0
FILTERED: 0
INSTRUMENTED: 2
MISSING: 0
NOT_A_TEST: 0
SIMPLE: 0
VT: 0
```

您还可以使用：`avocado:disable`的docstring指令，相反的工作方式：将被一个Avocado测试强制视为非avocado测试。

`:avocado: disable`指令首先被Avocado评估,这意味着，如果`:avocado: disable` 和 `:avocado: enable`同时出现的话，测试将不会被列出。


#### 递归发现测试

除了`:avocado: disable` 和 `:avocado: enable`指令，Avocado还支持`:avocado: recursive`
#### 分类测试

### Python unittest兼容性限制和警告

### 测试的环境变量

Avocado将一些信息（包括测试参数）作为环境变量导出到正在运行的测试中。

虽然这些变量可用于所有测试，但它们通常对SIMPLE测试更有意义。 原因是SIMPLE测试无法直接使用Avocado API。 INSTRUMENTED测试通常会有更强大的方法来访问相同的信息。

* `AVOCADO_VERSION`: Avocado测试运行器的版本
* `VOCADO_TEST_BASEDIR`:Avocado测试的基本目录
* `AVOCADO_TEST_WORKDIR`:测试的工作目录
* `AVOCADO_TESTS_COMMON_TMPDIR`:teststmpdir插件创建的临时目录。该目录在同一个Job中的整个测试中是持久的
* `AVOCADO_TEST_LOGDIR`：日志目录
* `AVOCADO_TEST_LOGFILE`: 测试的日志文件
* `AVOCADO_TEST_OUTPUTDIR`:测试的输出目录
* `AVOCADO_TEST_SYSINFODIR`：系统信息目录
* `***`: 来自-mux-yaml的所有变量
>>> `AVOCADO_TEST_SRCDIR`存在于早期版本中，但在版本60.0上已弃用，在版本62.0上已删除。请改用`AVOCADO_TEST_WORKDIR`。

>>> `AVOCADO_TEST_DATADIR`存在于早期版本中，但在版本60.0上已弃用，在版本62.0上已删除。现在，测试数据文件（和目录）已动态评估，不可用作环境变量

### SIMPLE测试BASH扩展

用shell编写的SIMPLE测试可以使用一些Avocado实用程序。 在shell代码中，检查库是否可用，例如：

```
AVOCADO_SHELL_EXTENSIONS_DIR=$(avocado exec-path 2>/dev/null)
```
如果可用，将包含这些实用程序的目录注入shell使用的PATH，使这些实用程序易于访问：

```
if [ $? == 0 ]; then
  PATH=$AVOCADO_SHELL_EXTENSIONS_DIR:$PATH
fi
```
有关实用程序的完整列表，请查看目录返回通过`avocado exec-path`（如果有的话）。 另外，示例测试`examples/tests/ simplewarning.sh`可以提供进一步的灵感。

>>> 这些扩展可以作为单独的包提供。 对于RPM包，请查找bash子包。

### 简单的测试状态

通过SIMPLE测试，Avocado会检查测试的退出代码，以确定测试是否已通过或已失败。

如果您的测试以退出代码0退出，但您仍希望在某些条件下设置不同的测试状态，则Avocado可以在测试输出中搜索给定的正则表达式，并在此基础上将状态设置为WARN或SKIP。

要使用该功能，您必须在配置文件中设置正确的密钥。 例如，当测试输出类似：'11：08：24 Test Skipped'：所示的行时，将测试状态设置为SKIP

```
[simpletests.output]
skip_regex = ^\d\d:\d\d:\d\d Test Skipped$
```
该配置将使Avocado在stdout和stderr上搜索Python正则表达式。 如果您只想限制其中一个搜索，那么该配置还有另一个键：

```
[simpletests.output]
skip_regex = ^\d\d:\d\d:\d\d Test Skipped$
skip_location = stderr
```

WARN状态存在相同的设置。 例如，如果要在测试输出以字符串WARNING开头的行时将测试状态设置为WARN，则配置文件将如下所示：

```
[simpletests.output]
skip_regex = ^\d\d:\d\d:\d\d Test Skipped$
skip_location = stderr
warn_regex = ^WARNING:
warn_location = all
```

### 本文小节

我们建议您查看一下中的示例测试`examples/tests`目录，这个目录包含一些样本以从中获取灵感。。 除了包含示例之外，该目录也被使用Avocado自测套件可对Avocado进行功能测试。
也可以查看[https://github.com/avocado-framework-tests](https://github.com/avocado-framework-tests),它允许人们分享他们的基本系统测试,以从中获取灵感。

## 原文档

[原文档](https://avocado-framework.readthedocs.io/en/63.0/Introduction.html)