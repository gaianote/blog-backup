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
* `WARN` - PASS的一种变体，用于跟踪最终不会影响测试结果的值得注意的事件。 一个例子可能是dmesg输出中存在的软锁定。 它与测试结果无关，除非测试失败，否则意味着该功能可能按预期工作，但有一些条件可能很好审查。 （某些结果插件不支持此功能并报告PASS）
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


Avocado按照定义的顺序查找数据文件[`DATA_SOURCES`](api/core/avocado.core.html＃avocado.core.test.TestData.DATA_SOURCES)，这是从最具体的一个到最通用的一个。这意味着，如果是变体正在使用，首先使用variant目录。然后测试尝试测试级别目录，最后是文件级目录。

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

## 原文档

[原文档](https://avocado-framework.readthedocs.io/en/63.0/Introduction.html)