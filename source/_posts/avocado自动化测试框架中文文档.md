---
title: "avocado自动化测试框架中文文档"
date: 2018-07-18 09:21:04
tags: 测试
---

## [关于Avocado](https://avocado-framework.readthedocs.io/en/63.0/Introduction.html)

Avocado是一套帮助自动化测试的工具和库。

人们可以将其称为具有益处的测试框架。 本机测试是用Python编写的,它们遵循unitest模式,但任何可执行文件都可以作为测试。

<!-- more -->

Avocado由以下组成：

* 一个允许您执行测试的测试运行器。 这些测试可以用您选择的语言编写,也可以用Python编写并使用可用的库。 在这两种情况下,您都可以获得自动日志和系统信息收集等功能。

* 帮助您以简洁,富有表现力和强大的方式编写测试的库。 您可以在库和API中找到有关哪些库适用于测试编写者的更多信息。

* 可以扩展Avocado Framework并为其添加新功能的插件。

Avocado是建立在Autotest积累的经验基础上,同时改善其弱点和缺点。

Avocado尽可能地遵守标准的Python测试技术。 使用Avocado API编写的测试来自unittest类,同时添加了适用于功能和性能测试的其他方法。 测试运行器旨在帮助人们在提供各种系统和日志记录工具的同时运行他们的测试,并且如果您需要更多功能,那么您可以逐步开始使用API功能。



## [入门](https://avocado-framework.readthedocs.io/en/63.0/GetStartedGuide.html)

那些喜欢视频介绍的人,请看看其他资源。 无论哪种方式,使用Avocado的第一步显然是安装它。

### 安装Avocado

Avocado主要是用Python编写的,因此标准的Python安装是可行的,而且通常更可取。

>如果您正在寻找特定于虚拟化的测试,请在完成Avocado安装后考虑查看Avocado-VT安装说明。

#### 使用标准Python工具进行安装

最简单的安装方法是通过pip。 在大多数可用Python 2.7和pip的POSIX系统上,只需一个命令即可执行安装：

> 译者注:虽然python2.7是可用的,但是已经逐渐被淘汰了,因此建议使用python3.6+以及其相对应的pip进行安装

```bash
pip install --user avocado-framework
```
这将从PyPI存储库中获取Avocado包(可能还有一些依赖项),并尝试将其安装在用户的主目录中(通常在〜/ .local下)。

> 如果要执行系统范围的安装,请删除 --user删除。
> 译者:如果希望在命令行启用 avocado 命令的话,安装时不能使用 --user 参数

如果您想要更多隔离,Avocado也可以安装在Python虚拟环境中。 除了创建和激活虚拟环境本身之外没有其他步骤：

```bash
python -m virtualenv /path/to/new/virtual_environment
. /path/to/new/virtual_environment/bin/activate
pip install avocado-framework
```

请注意,这将安装Avocado核心功能。

许多Avocado功能都作为非核心插件分发,也可作为PyPI上的附加软件包提供。 你应该能够通过`pip search avocado-framework-plugin | grep avocado-framework-plugin`找到它们。其中一些列在下面：

* [avocado-framework-plugin-result-html](https://pypi.python.org/pypi/avocado-framework-plugin-result-html): HTML报告

* [avocado-framework-plugin-resultsdb](https://pypi.python.org/pypi/avocado-framework-plugin-resultsdb): 将job结果传播到Resultsdb

* [avocado-framework-plugin-runner-remote](https://pypi.python.org/pypi/avocado-framework-plugin-runner-remote): 用于远程执行的运行器

* [avocado-framework-plugin-runner-vm](https://pypi.python.org/pypi/avocado-framework-plugin-runner-vm): 用于libvirt VM执行的运行器

* [avocado-framework-plugin-runner-docker](https://pypi.python.org/pypi/avocado-framework-plugin-runner-docker): Docker容器上执行的Runner

* [avocado-framework-plugin-loader-yaml](https://pypi.python.org/pypi/avocado-framework-plugin-loader-yaml): 从YAML文件加载测试

* [avocado-framework-plugin-robot](https://pypi.python.org/pypi/avocado-framework-plugin-robot): 执行Robot Framework测试

* [avocado-framework-plugin-varianter-yaml-to-mux](https://pypi.python.org/pypi/avocado-framework-plugin-varianter-yaml-to-mux): 将YAML文件解析为变量

#### 从包安装

原文介绍了一些Avocado其它的安装方法,有兴趣可以去[原址](https://avocado-framework.readthedocs.io/en/63.0/GetStartedGuide.html#installing-from-packages)查看

### 使用Avocado

您应首先使用测试运行器体验Avocado,即命令行工具,它将方便地运行您的测试并收集其结果。

#### 运行测试

为此,请使用`run`子命令运行Avocado,`run`后面跟随要进行的测试,它可以是文件的路径,也可以是可识别的名称：

```
$ avocado run /bin/true
JOB ID    : 381b849a62784228d2fd208d929cc49f310412dc
JOB LOG   : $HOME/avocado/job-results/job-2014-08-12T15.39-381b849a/job.log
 (1/1) /bin/true: PASS (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.11 s
JOB HTML  : $HOME/avocado/job-results/job-2014-08-12T15.39-381b849a/html/results.html
```

您可能已经注意到我们使用/ bin / true作为测试,并且根据我们的期望,它通过了！ 这些被称为简单测试,但也有另一种类型的测试,我们称之为仪器测试。 在测试类型中查看更多信息或继续阅读。

> 虽然在大多数情况下运行Avocado运行 $ test1 $ test3 ...很好,但它可能导致参数与测试名称冲突。 最安全的执行测试的方法是Avocado运行 -  $ argument1  -  $ argument2  -  $ test1 $ test2。 之后的所有内容 - 将被视为位置参数,即测试名称(在Avocado运行的情况下)

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
它支持所有运行参数,模拟运行甚至列出测试参数。

另一种方法是使用list子命令列出发现的测试如果没有提供参数,Avocado会为每个插件列出“默认”测试。 输出可能如下所示：

> 译者: `avocado list .` 列出当前目录的avocado测试,直接使用`avocado list`未返回结果。

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
这里,如前所述,SIMPLE意味着这些文件是可执行文件,被视为简单测试。 您还可以使用--verbose或-V标志来显示Avocado找到的文件,但不被视为Avocado测试：

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
请注意,详细标志还会添加摘要信息。

#### 写一个简单的测试

这个用shell脚本编写的简单测试的简单例子

```bash
$ echo '#!/bin/bash' > /tmp/simple_test.sh
$ echo 'exit 0' >> /tmp/simple_test.sh
$ chmod +x /tmp/simple_test.sh
```

請注意,該文件具有可執行權限,這是Avocado將其視為簡單測試的要求。 另請注意,腳本以狀態代碼0退出,這表示Avocado成功結果。

#### 运行更复杂的测试工作

您可以按任意顺序运行任意数量的测试,以及混合和匹配仪器化测试和简单测试：

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

#### 在第一次失败的测试中中断job(failfast)

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

在重新运行`--failfast on`执行的job时,也可以使用`--failfast off`强制禁用failfast模式。

#### 忽略缺少的测试引用

当您提供测试参考列表时,Avocado将尝试将所有测试参考解析为测试。如果无法将一个或多个测试引用解析为测试,则不会创建job。例：

```
$ avocado run passtest.py badtest.py
Unable to resolve reference(s) 'badtest.py' with plugins(s) 'file', 'robot', 'external', try running 'avocado list -V badtest.py' to see the details.
```
但是如果你无论如何都想要执行这项测试,使用可以解决的测试,你可以使用`--ignore-missing-references on`。 UI中将显示相同的消息,但将执行这个测试：

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

在大多数软件项目中使用逐渐增加的测试套件是很常见的。这些通常包括一个定制的,非常具体的测试运行器,它知道如何查找和运行自己的测试

尽管如此,由于各种原因,在Avocado中运行这些测试可能是一个好主意,包括能够以不同的人机和机器可读格式获得结果,收集系统信息以及这些测试(Avocado的sysinfo功能)等等

Avocado 通过其"external runner"功能实现了这一目标。最基本的使用方法是：

```bash
$ avocado run --external-runner=/path/to/external_runner foo bar baz
```
在此示例中,Avocado将报告测试foo,bar和baz的各个测试结果。实际结果将基于`/path/to/external_runner foo`,`/path/to/external_runner bar`和`/path/to/external_runner baz`的单独执行的返回代码。其中`/path/to/external_runner`是你的外部解释器的路径。


作为另一种解释该功能如何工作的方法,可以将"external runner"视为某种解释器,并将个体测试视为此解释器识别并能够执行的任何内容。一个UNIX shell,比如`/bin/sh`可以被认为是一个外部运行器,带有shell代码的文件可以被认为是测试：

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

这个例子非常明显,可以通过给/tmp/pass和/tmp/fail "shebangs"(#!/bin/sh)来实现,使它们可执行(chmod+x /tmp/pass /tmp/fail并将它们作为"SIMPLE"测试运行。

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

这有效地使`/bin/curl`成为"外部测试运行器",负责尝试获取这些URL,并为每个URL报告PASS或FAIL。

### 调试测试

#### 显示测试输出

在开发新测试时,您经常希望直接查看job日志,而无需切换屏幕或不必“拖尾”job日志。

为了实现它,你可以使用`avocado --show test run ...` 或者 `avocado run --show-job-log`选项

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

如您所见,UI输出被抑制,只显示job日志,这使其成为测试开发和调试的有用功能。


#### 中断测试执行

要中断job执行,用户可以按`ctrl + c`,在单次按下后将SIGTERM发送到主测试的进程并等待它完成。如果这没有帮助,用户可以再次按`ctrl + c`(2s宽限期后),这会非常有效地破坏测试过程并安全地完成job执行,始终提供测试结果。

要暂停测试执行,用户可以使用`ctrl + z`将SIGSTOP发送到从测试的PID继承的所有进程。我们尽力停止所有进程,但操作不是原子操作,可能无法停止某些新进程。再次按下`ctrl + z`将SIGCONT发送到测试的PID继承执行的所有进程。请注意,测试执行时间(关于测试超时)仍然在测试进程停止时运行。


Avocado功能也可以中断测试。一个例子是使用GDB调试GDB调试功能。

对于自定义交互,还可以使用其他方法,如pdb或pydevd Avocado开发提示断点。请注意,不能在测试中使用STDIN(除非使用黑暗魔法)。

## [书写Avocado测试](https://avocado-framework.readthedocs.io/en/63.0/WritingTests.html)

我们将用Python编写Avocado测试,我们将继承avocado.Test。 这使得该测试成为所谓的仪器测试。

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

这是您可以为Avocado编写的最简单的测试,同时仍然可以利用其API功能。

#### 什么是Avocado测试

从上面的示例中可以看出,Avocado测试是一种从继承自avocado.Test的类开始的测试方法。

#### 多个测试和命名约定

您可以在一个类中进行多个测试。

为此,只需给出以test开头的方法名称,比如`test_foo`,`test_bar`等等。 我们建议您遵循此命名样式,如PEP8函数名称部分中所定义。

对于类名,您可以选择任何您喜欢的名称,但我们也建议它遵循CamelCase约定,也称为CapWords,在类名称下的PEP 8文档中定义。


#### 便利属性

* 可以通过`self.log`访问测试的即用型日志机制。 它允许您记录调试,信息,错误和警告消息。
* 可以通过`self.params`访问的参数传递系统(和提取系统)。 这与Varianter有关,您可以在Testary参数中找到更多信息。
* 还有更多(参见avocado.core.test.Test)

为了最大限度地减少意外冲突,我们将公共冲突定义为属性,因此如果您看到类似`AttributeError: can't set attribute`就不要覆盖这些属性。

### 测试状态

Avocado支持最常见的退出状态:

* `PASS` - 测试通过,没有未经处理的例外情况
* `WARN` - PASS的一种变量,用于跟踪最终不会影响测试结果的值得注意的事件。 一个例子可能是dmesg输出中存在的软锁定。 它与测试结果无关,除非测试失败,否则意味着该功能可能按预期工作,但有一些条件可能很好审查。 (某些结果插件不支持此功能并报告PASS)
* `SKIP` - 测试的先决条件不满足且测试的主体未被执行(也没有执行setUp()和tearDown)。
* `CANCEL` - 在setUp(),测试方法或tearDown()期间某处取消了测试。 执行setUp()和tearDown方法。
* `FAIL` - 测试未达到预期结果。 失败指向测试对象中的(可能的)错误,而不是测试脚本本身。 当测试(及其)执行中断时,报告ERROR而不是FAIL。
* `ERROR` - 这可能(可能)指向测试本身的一个错误,而不是在被测试的对象中。它通常是由未捕获的异常引起的,这种失败需要彻底探索并且应该导致测试修改以避免这种失败或者 使用self.fail以及描述测试中的对象如何无法执行它的任务。
* `INTERRUPTED` - 此结果无法由测试编写者设置,只有在超时或用户在执行此测试时按下`CTRL + C`时才会出现。
* other - 还有其他一些内部测试状态,但你应该不会遇到它们。


正如您所看到的那样,如果正确开发了测试,则FAIL是一个整洁的状态。在编写测试时,总要考虑它的`setUp`应该是什么,`test body`是什么,并且在测试中预计会出错。为了支持您,Avocado支持以下几种方法：


#### 测试方法

设置状态的最简单方法是直接从test中使用`self.fail`,`self.error`或`self.cancel`。

要记录警告,只需写入`self.log.warning`日志即可。这不会中断测试执行,但会记住条件,如果没有失败,则会将测试报告为`WARN`。

#### 将错误转化为失败

Python代码上的错误通常以抛出异常的形式发出信号。当Avocado运行测试时,任何未处理的异常都将被视为测试错误,而不是失败。

尽管如此,依赖库通常会引发自定义(或内置)异常。这些异常通常会导致错误,但如果您确定这是测试对象的奇怪行为,您应该捕获异常并解释self.fail方法中的失败：

```python
try:
    process.run("stress_my_feature")
except process.CmdError as details:
    self.fail("The stress comamnd failed: %s" % details)
```

如果你的测试组件有很多执行而你无法在其他情况下得到这个异常然后预期失败,你可以使用`fail_on`装饰器来简化代码：

```python
@avocado.fail_on(process.CmdError)
def test(self):
    process.run("first cmd")
    process.run("second cmd")
    process.run("third cmd")
```


再次,让您的测试脚本保持最新并区分`FAIL`和`ERROR`的区别,将在查看测试结果时节省大量时间。

### 保存测试生成的(自定义)数据

每个测试实例都提供一个所谓的`whiteboard`。它可以通过self.whiteboard访问。这个`whiteboard`只是一个字符串,在测试结束后会自动保存到测试结果中(在执行过程中没有同步,所以当机器或python严重崩溃时可能不存在,并且应该使用direct io直接输出到关键数据的输出)。如果您选择将二进制数据保存到`whiteboard`,则您有责任首先对其进行编码(base64是显而易见的选择)。

在之前演示的`sleeptest`测试的基础上,假设您想要保存`sleep length`以供其他一些脚本或数据分析工具使用：

```python
def test(self):
    sleep_length = self.params.get('sleep_length', default=1)
    self.log.debug("Sleeping for %.2f seconds", sleep_length)
    time.sleep(sleep_length)
    self.whiteboard = "%.2f" % sleep_length
```

`whiteboard`可以并且应该由可用的测试结果插件生成的文件公开。 results.json文件已包含每个测试的`whiteboard`。此外,为方便起见,我们将`whiteboard`内容的原始副本保存在名为whiteboard的文件中,与result.json文件位于同一级别(也许您希望直接使用基准测试结果与自定义脚本分析特定的基准测试结果)。

如果需要附加多个输出文件,还可以使用`self.outputdir`,它指向`$RESULTS/test-results/$ TEST_ID/data`位置,并保留用于任意测试结果数据。

### 访问测试数据文件

某些测试可能依赖于测试文件本身外部的数据文件。 Avocado提供了一个测试API,可以很容易地访问这些文件：`get_data()` 。

对于Avocado测试(即INSTRUMENTED测试),`get_data()`允许从最多三个源访问测试数据文件：

* 文件级数据目录：以测试文件命名但以.data结尾的目录。对于测试文件`/home/user/test.py`,文件级数据目录是`/home/user/test.py.data/`。

* 测试级别数据目录：以测试文件和特定测试名称命名的目录。当同一文件的不同测试部分需要不同的数据文件(具有相同或不同名称)时,这些功能非常有用。考虑到之前的`/home/user/test.py`示例,并假设它包含两个测试,`MyTest.test_foo`和`MyTest.test_bar`,测试级数据目录将是`/home/user/test.py.data/MyTest.test_foo/`和`home/user/test.py.data/MyTest.test_bar/`

* 变量级数据目录：如果在测试期间使用变量执行时,也会考虑以变量命名的目录寻找测试数据文件。对于测试文件`/home/user/test.py`,并测试`MyTest.test_foo`,带有变量`debug-ffff`,数据目录路径将是`/home/user/test.py.data/MyTest.test_foo/debug-ffff/`。

> 与INSTRUMENTED测试不同,SIMPLE测试仅定义`file`和`variant` 数据目录,因此是最具体的数据目录可能看起来像`/bin/echo.data/debug-ffff /`。


Avocado按照定义的顺序查找数据文件[`DATA_SOURCES`](api/core/avocado.core.html＃avocado.core.test.TestData.DATA_SOURCES),这是从最具体的一个到最通用的一个。这意味着,如果是变量正在使用,首先使用variant目录。然后测试尝试测试级别目录,最后是文件级目录。

另外,你可以使用`get_data(filename,must_exist = False)`来获取可能不存在的文件的预期位置,这在当你打算创建它的情况下很有用。

> 运行测试时,您可以使用`--log-test-data-directories`命令行选项记录将使用的测试数据目录
对于特定的测试和执行条件(例如使用或没有变种)。在测试日志中查找“测试数据目录”。

>以前存在的API`avocado.core.test.Test.datadir`,用于允许基于测试文件访问数据目录仅限位置。此API已被删除。无论出于何种原因,您仍然只需要根据测试文件位置访问数据目录,可以使用`get_data(filename ='',source ='file',must_exist = False)`。

### 访问测试参数

每个测试都有一组可以访问的参数`self.params.get($ name,$ path = None,$ default = None)`其中：

* name - 参数名称(键)
* path - 查找此参数的位置(未指定时使用mux-path)
* default - 未找到param时返回的内容

路径是有点棘手。 Avocado使用树来表示参数。 在简单的场景中,您不必担心,您将在默认情况下找到所有值的路径,但最终你可能想要查询Test parameters来理解细节。

假设您的测试收到以下参数(您将在下一节中学习如何执行它们)：

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

> 在可能发生冲突的复杂场景中,该路径很重要,因为当存在多个具有相同键匹配值的值时,Avocado会引发异常。如上所述,您可以通过使用特定路径或通过定义允许指定解析层次结构的自定义mux-path来避免这些路径。 更多细节可以在测试参数中找到。

### 运行多个测试变量

在上一节中,我们描述了如何处理参数。 现在,让我们看看如何生成它们并使用不同的参数执行测试。

变量子系统允许创建多个参数变量,并使用这些参数变量执行测试。此子系统是可插入的,因此您可以使用自定义插件来生成变量。为了简单起见,让我们使用Avocado的初步实施,称为`yaml_to_mux`。

`yaml_to_mux`插件接受YAML文件。 这些将创建树状结构,将变量存储为参数并使用自定义标记将位置标记为`multiplex`域。

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

您可以看到它创建了每个Multiplex域的所有可能变量,这些变量由YAML文件中的！mux标记定义,并在树视图中显示为单行(与具有值的单个节点的双行比较)。 总共它会产生每种测试的8种变量：

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

一个常见的例子是需要在更长或更复杂的测试中遵循特定的进展。 让我们看一个非常简单的测试示例,但在单个测试中有一个多个明确的阶段：

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

从现在开始,您可以要求Avocado显示您的日志记录流,无论是独占还是其他内置流：

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

自定义`progress`流与应用程序输出结合在一起,可能适合或可能不适合您的需要或喜好。 如果你为了清楚和持久性,想把`progress`流将发送到一个单独的文件,你可以像这样运行Avocado：

```bash
$ avocado run plant.py --store-logging-stream progress
```
结果是,除了通常生成的所有其他日志文件之外,还会在job结果目录中有另一个名为progress.INFO的日志文件。 在测试运行期间,可以通过以下方式观察进度：

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

这个非常相似的progress logger,可以跨多个测试方法和多个测试模块使用。在给出的示例中,测试名称用于提供额外的上下文。


### unittest.TestCase继承

由于Avocado测试继承了unittest.TestCase,所以可以使用其父级的所有断言方法。
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

nose是另一个Python测试框架,它也与unittest兼容。
因此,您可以使用nosetest应用程序运行Avocado测试：

```
$ nosetests examples/tests/sleeptest.py
.
----------------------------------------------------------------------
Ran 1 test in 1.004s

OK
```

相反,您也可以使用标准unittest.main()入口点运行Avocado测试。检查下面的代码,以保存为dummy.py：

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

在测试之前或之后执行setUp操作,您可以使用setUp和tearDown方法,tearDown方法总是在安装失败时执行,所以不要忘记在setUp过程中初始化变量。使用示例在下一节运行第三方测试套件中。

### 运行第三方测试套件

在测试自动化工作负载中使用第三方开发的测试套件非常常见。通过在Avocado测试模块中封装执行代码,您可以访问框架提供的设施和API。假设你想用C写一个测试套件,它在一个tarball中,解压缩它,编译套件代码,然后执行测试。下面是一个例子：

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

这里我们有一个setup方法的例子：这里我们通过`avocado.Test.get_data()` 得到测试套件代码(tarball)的位置。然后通过`avocado.utils.archive.extract()`解压缩
一个API会解压缩tarball套件,`avocado.utils.build.make()`会建立则个套件。

在这个例子中,测试方法刚刚进入编译的套件的基本目录,并使用`avocado.utils.process.system()`和适当的参数执行`./synctest`命令。

### 获取资产文件
### 测试输出检查和输出记录模式

在很多情况下,你想变得简单：只需检查给定测试的输出是否匹配预期输出。为了帮助这个常见的用例,Avocado提供了`--output-check-record`选项

如果启用这个选项,Avocado将会将测试生成的内容保存到标准(POSIX)流,即`STDOUT` 和 `STDERR`.根据所选的选项,您可能会记录不同的文件(我们称之为“参考文件”)：

* `stdout`将生成一个名为`stdout.expected`的文件,该文件包含来自测试过程标准输出流(文件描述符1)的内容。
* `stderr`将生成一个名为`stderr.expected`的文件,该文件包含来自测试过程标准错误流(文件描述符2)的内容。
* `both`将生成一个名为`stdout.expected`和一个名为`stderr.expected`的文件
* `combined`将生成一个名为`output.expected`的文件,其中包含测试过程标准输出和错误流(文件描述符1和2)的内容。
* `none`将显式禁用测试生成的输出和生成内容的生成参考文件的所有记录

参考文件将被记录在第一个(最特定的)测试数据文件夹(访问测试数据文件)中。让我们以测试`synctest.py`为例。检查Avocado源代码,您可以找到以下参考文件：

```
examples/tests/synctest.py.data/stderr.expected
examples/tests/synctest.py.data/stdout.expected
```

在这两个文件中,只有stdout.expected有些内容

```
$ cat examples/tests/synctest.py.data/stdout.expected
PAR : waiting
PASS : sync interrupted
```

这意味着,在之前的测试执行期间,用`--output-check-record both`进行输出记录,并且仅在stdout流上生成内容：

```
$ avocado run --output-check-record both synctest.py
JOB ID     : b6306504351b037fa304885c0baa923710f34f4a
JOB LOG    : $JOB_RESULTS_DIR/job-2017-11-26T16.42-b630650/job.log
 (1/1) examples/tests/synctest.py:SyncTest.test: PASS (2.03 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 0
JOB TIME   : 2.26 s
```
在添加参考文件之后,检查过程是透明的,从某种意义上说,您不需要向test runner提供特殊标志。从这一点开始,在测试(一个带有参考文件记录的一个)完成运行之后,Avocado将检查输出是否与参考文件内容匹配。如果它们不匹配,则测试将以失败状态结束。

当引用文件存在时,你也可以对此测试运行程序禁用自动检查`--output-check=off`对此测试运行程序。

这个过程还可以也可以在简单测试,也就是返回0 (PASSed) or != 0 (FAILed)的程序或或shell脚本工作的很好。让我们考虑例子：

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
完成此操作后,您会注意到测试数据目录出现在我们的shell脚本的同一个级别,包含2个文件：

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

现在,每次测试运行时,程序都会自动对比记录的预期文件,我们不需要做任何其他操作。让我们看看如果把STDUT.期望的文件内容改为Hello,avocado 会发生什么呢？：

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

正如预期的那样,测试失败了,因为我们改变了它的期望,因此记录了一个统一的差异。统一的差异也存在于文件`stdout.diff` 和 `stderr.diff`中,存在于测试结果目录中：

```
$ cat $HOME/avocado/job-results/latest/test-results/1-output_record.sh/stdout.diff
--- $HOME/output_record.sh.data/stdout.expected
+++ $HOME/avocado/job-results/job-2017-10-16T14.23-8cba866/test-results/1-output_record.sh/stdout
@@ -1 +1 @@
-Hello, Avocado!
+Hello, world!
```

> 目前,stdout和stder都以文本方式存储。根据当前区域设置无法解码的数据将根据 https://docs.python.org/3/library/codecs.html#codecs.replace_errors 替换
### 在本机Avocado模块中测试日志,stdout和stderr

如果需要,可以直接从原生测试范围写入预期的stdout和stderr文件。区分以下实体是很重要的：

* The test logs
* The test expected stdout 期待的标准输出
* The test expected stderr 期待的标准错误

第一个是用于调试和输出信息的目的。另外,写入`self.log.warning`会导致测试被标记为dirty,当一切顺利时,测试以警告结束。这意味着测试通过了,但是在警告日志中描述了非相关的意外情况。

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

如果您需要直接写入测试stdout和stderr流,Avocado使两个预先配置的日志记录器可用于此目的,名为`avocado.test.stdout`和`avocado.test.stderr`。可以使用Python的标准日志API来对它们进行写入。例子：

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
Avocado将自动保存测试在STDUT中生成的任何东西到stdout文件中,在测试结果目录中找到。这同样适用于测试在STDRR上生成的任何东西,也就是说,它将被保存到同一个位置的stderr文件中。

此外,当使用runner的输出记录特性,即` --output-check-record `参数值stdout, stderr或者all时,所有给这些记录器的所有内容都将保存到文`stdout.expected`和`stderr.expected`在测试数据目录中(与`job/test results`不同)。

### 设置测试超时

有时您的测试套件/测试可能会被永久卡住,这可能会影响测试网格。您可以解释这种可能性,并为测试设置超时参数。测试超时可以通过测试参数来设置,如下所示。

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

YAML文件定义了一个测试参数超时,它在运行程序结束之前,通过发送一个类`:signal.SIGTERM`到测试,raise错误`avocado.core.exceptions.TestTimeoutError`,从而提高了测试速度。

### 跳过测试

要在Avocado中跳过测试,必须使用Avocado跳过装饰器中的一种：

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
注意,由于提供的条件不是false,所以没有跳过Test3。

使用跳过装饰器,实际上没有执行任何操作。我们将跳过`setup`方法、测试方法和`teardown`方法。

> 任何skip装饰器都不能在teardown方法上使用,否则会出现错误,状态吗为`ERROR`

### 取消测试
您可以在测试的任何阶段(`setup()`、测试方法或`teardown`)中调用`self.cancel()`取消测试。测试将以取消状态结束,并且不会使job以非0状态退出。例子：

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

在缺少IPRF包但系统安装在正确版本中的系统中,结果将是：

```
JOB ID     : 39c1f120830b9769b42f5f70b6b7bad0b1b1f09f
JOB LOG    : $HOME/avocado/job-results/job-2017-03-10T16.22-39c1f12/job.log
 (1/2) /home/apahim/avocado/tests/test_cancel.py:CancelTest.test_iperf: CANCEL (1.15 s)
 (2/2) /home/apahim/avocado/tests/test_cancel.py:CancelTest.test_gcc: PASS (1.13 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 1
JOB TIME   : 2.38 s
JOB HTML   : $HOME/avocado/job-results/job-2017-03-10T16.22-39c1f12/html/results.html
```

注意,使用`self.cancel()`将从该点取消其余的测试,但是`teardown()`仍将被执行。

根据您所提到的结果格式,取消状态被映射到相应格式的有效状态。见下表：

| Format | Corresponding Status |
|--------|----------------------|
| json   | cancel               |
| xunit  | skipped              |
| tap    | ok                   |
| html   | CANCEL (warning)     |

### Docstring指令

一些Avododo特性,通常只适用于仪器化测试,依赖于在测试类的DoScord中设置指令。DOXString指令由标记(`:avocado:`)组成,接着是自定义内容本身,如`:avocado: directive`。

这与DoScript指令类似,例如`:param my_param: description`对于大多数Python开发人员来说,这应该不是一个意外。

Avocado使用这些DOSCRON指令(而不是真正的Python代码)的原因是,在寻找测试时进行的检查不涉及代码的任何执行。

有关DoScript格式的有效性的详细解释,请参阅我们关于DOSCSHIPE指令规则的章节。

现在让我们继续使用一些DoScript指令示例。

#### 显式启用或禁用测试

如果您的测试是直接从`avocado.Test`继承的类中的一个方法,那么avocado会像预期的那样找到它。

现在,可能需要更复杂的测试,使用更先进的Python特性,例如继承。对于那些不直接从`avocado.Test`中继承的测试,Avocado可能需要你的帮助,因为Avocado只使用静态分析来检查文件。

例如,假设您定义了一个新的测试类,该类继承了avocado基础测试类,即`avocado.Test`,并将其放入`mylibrary.py`：

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

如果您试图列出该文件中的测试,这将是您将得到的：

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

你需要通过添加一个docstring指令来给Avocado一点帮助。docstring指令是：`:avocado: enable`。它告诉Avocado安全测试检测代码,将其视为Avocado试验,而不管检测代码对它的看法如何。让我们看看效果如何。添加docstring,如下所示：

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

您还可以使用：`avocado:disable`的docstring指令,相反的工作方式：将被一个Avocado测试强制视为非avocado测试。

`:avocado: disable`指令首先被Avocado评估,这意味着,如果`:avocado: disable` 和 `:avocado: enable`同时出现的话,测试将不会被列出。


#### 递归发现测试

除了`:avocado: disable` 和 `:avocado: enable`指令,Avocado还支持`:avocado: recursive`
#### 分类测试

### Python unittest兼容性限制和警告

### 测试的环境变量

Avocado将一些信息(包括测试参数)作为环境变量导出到正在运行的测试中。

虽然这些变量可用于所有测试,但它们通常对SIMPLE测试更有意义。 原因是SIMPLE测试无法直接使用Avocado API。 INSTRUMENTED测试通常会有更强大的方法来访问相同的信息。

* `AVOCADO_VERSION`: Avocado测试运行器的版本
* `VOCADO_TEST_BASEDIR`:Avocado测试的基本目录
* `AVOCADO_TEST_WORKDIR`:测试的工作目录
* `AVOCADO_TESTS_COMMON_TMPDIR`:teststmpdir插件创建的临时目录。该目录在同一个Job中的整个测试中是持久的
* `AVOCADO_TEST_LOGDIR`：日志目录
* `AVOCADO_TEST_LOGFILE`: 测试的日志文件
* `AVOCADO_TEST_OUTPUTDIR`:测试的输出目录
* `AVOCADO_TEST_SYSINFODIR`：系统信息目录
* `***`: 来自-mux-yaml的所有变量
> `AVOCADO_TEST_SRCDIR`存在于早期版本中,但在版本60.0上已弃用,在版本62.0上已删除。请改用`AVOCADO_TEST_WORKDIR`。

> `AVOCADO_TEST_DATADIR`存在于早期版本中,但在版本60.0上已弃用,在版本62.0上已删除。现在,测试数据文件(和目录)已动态评估,不可用作环境变量

### SIMPLE测试BASH扩展

用shell编写的SIMPLE测试可以使用一些Avocado实用程序。 在shell代码中,检查库是否可用,例如：

```
AVOCADO_SHELL_EXTENSIONS_DIR=$(avocado exec-path 2>/dev/null)
```
如果可用,将包含这些实用程序的目录注入shell使用的PATH,使这些实用程序易于访问：

```
if [ $? == 0 ]; then
  PATH=$AVOCADO_SHELL_EXTENSIONS_DIR:$PATH
fi
```
有关实用程序的完整列表,请查看目录返回通过`avocado exec-path`(如果有的话)。 另外,示例测试`examples/tests/ simplewarning.sh`可以提供进一步的灵感。

> 这些扩展可以作为单独的包提供。 对于RPM包,请查找bash子包。

### 简单的测试状态

通过SIMPLE测试,Avocado会检查测试的退出代码,以确定测试是否已通过或已失败。

如果您的测试以退出代码0退出,但您仍希望在某些条件下设置不同的测试状态,则Avocado可以在测试输出中搜索给定的正则表达式,并在此基础上将状态设置为WARN或SKIP。

要使用该功能,您必须在配置文件中设置正确的密钥。 例如,当测试输出类似：'11：08：24 Test Skipped'：所示的行时,将测试状态设置为SKIP

```
[simpletests.output]
skip_regex = ^\d\d:\d\d:\d\d Test Skipped$
```
该配置将使Avocado在stdout和stderr上搜索Python正则表达式。 如果您只想限制其中一个搜索,那么该配置还有另一个键：

```
[simpletests.output]
skip_regex = ^\d\d:\d\d:\d\d Test Skipped$
skip_location = stderr
```

WARN状态存在相同的设置。 例如,如果要在测试输出以字符串WARNING开头的行时将测试状态设置为WARN,则配置文件将如下所示：

```
[simpletests.output]
skip_regex = ^\d\d:\d\d:\d\d Test Skipped$
skip_location = stderr
warn_regex = ^WARNING:
warn_location = all
```

### 本文小节

我们建议您查看一下中的示例测试`examples/tests`目录,这个目录包含一些样本以从中获取灵感。。 除了包含示例之外,该目录也被使用Avocado自测套件可对Avocado进行功能测试。
也可以查看[https://github.com/avocado-framework-tests](https://github.com/avocado-framework-tests),它允许人们分享他们的基本系统测试,以从中获取灵感。

## [结果格式化](https://avocado-framework.readthedocs.io/en/63.0/ResultFormats.html)

测试脚本必须提供各种方法来清晰地将结果传达给相关方,无论是人还是机器。

> 有几个可选的结果插件,你可以在Result Plugins中找到它们。

### 人类可读结果

Avocado有两种不同的结果格式,供人类使用：

* 默认UI,它在命令行上显示基于文本UI的实况测试执行结果。
* HTML报告,它是在测试任务完成后生成的。

Avocado的命令行界面

定期运行Avocado将以生动的方式呈现测试结果,也就是说,工作和测试结果不断更新：

```
$ avocado run sleeptest.py failtest.py synctest.py
JOB ID    : 5ffe479262ea9025f2e4e84c4e92055b5c79bdc9
JOB LOG   : $HOME/avocado/job-results/job-2014-08-12T15.57-5ffe4792/job.log
 (1/3) sleeptest.py:SleepTest.test: PASS (1.01 s)
 (2/3) failtest.py:FailTest.test: FAIL (0.00 s)
 (3/3) synctest.py:SyncTest.test: PASS (1.98 s)
RESULTS    : PASS 1 | ERROR 1 | FAIL 1 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 3.27 s
JOB HTML  : $HOME/avocado/job-results/job-2014-08-12T15.57-5ffe4792/html/results.html
```
最重要的是要记住,程序不需要分析人的输出来确定测试工作运行的情况。

### 机器可读结果

另一种类型的结果是那些被其他应用程序解析的结果。测试社区中存在若干标准,Avocado在理论上可以支持几乎所有的结果标准。

非常好,Avocado支持一些机器可读的结果。它们总是生成并存储在结果目录中。$Type文件,但是您也可以要求不同的位置。

#### xunit

Avocado默认的机器可读输出是xunit

xunit是以结构化形式包含测试结果的XML格式,并由其他测试自动化项目(Jenkins)使用。如果你想让Avocado在runner的标准输出中生成xunit作为输出,可以简单地使用：

```
$ avocado run sleeptest.py failtest.py synctest.py --xunit -
<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="avocado" tests="3" errors="0" failures="1" skipped="0" time="3.5769162178" timestamp="2016-05-04 14:46:52.803365">
        <testcase classname="SleepTest" name="1-sleeptest.py:SleepTest.test" time="1.00204920769"/>
        <testcase classname="FailTest" name="2-failtest.py:FailTest.test" time="0.00120401382446">
                <failure type="TestFail" message="This test is supposed to fail"><![CDATA[Traceback (most recent call last):
  File "/home/medic/Work/Projekty/avocado/avocado/avocado/core/test.py", line 490, in _run_avocado
    raise test_exception
TestFail: This test is supposed to fail
]]></failure>
                <system-out><![CDATA[14:46:53 ERROR|
14:46:53 ERROR| Reproduced traceback from: /home/medic/Work/Projekty/avocado/avocado/avocado/core/test.py:435
14:46:53 ERROR| Traceback (most recent call last):
14:46:53 ERROR|   File "/home/medic/Work/Projekty/avocado/avocado/examples/tests/failtest.py", line 17, in test
14:46:53 ERROR|     self.fail('This test is supposed to fail')
14:46:53 ERROR|   File "/home/medic/Work/Projekty/avocado/avocado/avocado/core/test.py", line 585, in fail
14:46:53 ERROR|     raise exceptions.TestFail(message)
14:46:53 ERROR| TestFail: This test is supposed to fail
14:46:53 ERROR|
14:46:53 ERROR| FAIL 2-failtest.py:FailTest.test -> TestFail: This test is supposed to fail
14:46:53 INFO |
]]></system-out>
        </testcase>
        <testcase classname="SyncTest" name="3-synctest.py:SyncTest.test" time="2.57366299629"/>
</testsuite>
```
最后的`-`是xunit的选项,表示xunit应该转到标准输出

如果你的测试产生了很长的输出,你可以用 –xunit-max-test-log-chars 来限制嵌入字符的数量。如果日志文件中的输出较长,则只从最大值开始附加到最大测试日志字符,另一半从内容的结尾开始。

#### JSON

JSON是一种广泛使用的数据交换格式,JSON avocado插件使用类似于xunit使用方式

```
$ avocado run sleeptest.py failtest.py synctest.py --json -
{
    "cancel": 0,
    "debuglog": "/home/cleber/avocado/job-results/job-2016-08-09T13.53-10715c4/job.log",
    "errors": 0,
    "failures": 1,
    "job_id": "10715c4645d2d2b57889d7a4317fcd01451b600e",
    "pass": 2,
    "skip": 0,
    "tests": [
        {
            "end": 1470761623.176954,
            "fail_reason": "None",
            "logdir": "/home/cleber/avocado/job-results/job-2016-08-09T13.53-10715c4/test-results/1-sleeptest.py:SleepTest.test",
            "logfile": "/home/cleber/avocado/job-results/job-2016-08-09T13.53-10715c4/test-results/1-sleeptest.py:SleepTest.test/debug.log",
            "start": 1470761622.174918,
            "status": "PASS",
            "id": "1-sleeptest.py:SleepTest.test",
            "time": 1.0020360946655273,
            "whiteboard": ""
        },
        {
            "end": 1470761623.193472,
            "fail_reason": "This test is supposed to fail",
            "logdir": "/home/cleber/avocado/job-results/job-2016-08-09T13.53-10715c4/test-results/2-failtest.py:FailTest.test",
            "logfile": "/home/cleber/avocado/job-results/job-2016-08-09T13.53-10715c4/test-results/2-failtest.py:FailTest.test/debug.log",
            "start": 1470761623.192334,
            "status": "FAIL",
            "id": "2-failtest.py:FailTest.test",
            "time": 0.0011379718780517578,
            "whiteboard": ""
        },
        {
            "end": 1470761625.656061,
            "fail_reason": "None",
            "logdir": "/home/cleber/avocado/job-results/job-2016-08-09T13.53-10715c4/test-results/3-synctest.py:SyncTest.test",
            "logfile": "/home/cleber/avocado/job-results/job-2016-08-09T13.53-10715c4/test-results/3-synctest.py:SyncTest.test/debug.log",
            "start": 1470761623.208165,
            "status": "PASS",
            "id": "3-synctest.py:SyncTest.test",
            "time": 2.4478960037231445,
            "whiteboard": ""
        }
    ],
    "time": 3.4510700702667236,
    "total": 3
}
```

请记住,没有AvocadoJSON结果格式的文档标准。这意味着它可能会逐渐增加,以适应更新的Avocado特性。适当的工作解析JSON构成的结果将不会破坏与应用程序的向后兼容性。

#### TAP
提供当前在V12版本的基本TAP(测试任何协议)结果。不像大多数现有Avocado机器可读的输出,这一个是流线型(每个测试结果)：

```
$ avocado run sleeptest.py --tap -
1..1
# debug.log of sleeptest.py:SleepTest.test:
#   12:04:38 DEBUG| PARAMS (key=sleep_length, path=*, default=1) => 1
#   12:04:38 DEBUG| Sleeping for 1.00 seconds
#   12:04:39 INFO | PASS 1-sleeptest.py:SleepTest.test
#   12:04:39 INFO |
ok 1 sleeptest.py:SleepTest.test
```

> 译者 debug.log不会显示在控制台,需要到debug.log中去查看
> cat ~/avocado/job-results/latest/test-results/1-sleeptest.py_SleepTest.test/debug.log

#### Silent result
此结果禁用所有stdout日志记录(同时将错误消息打印到stderr)。然后,可以使用返回代码来了解结果：

```
$ avocado --silent run failtest.py
$ echo $?
1
```
在实践中,这通常会被脚本用来运行avocado,并检查其结果：

```
#!/bin/bash
...
$ avocado --silent run /path/to/my/test.py
if [ $? == 0 ]; then
   echo "great success!"
elif
   ...
```
关于退出代码中的退出代码的更多细节部分。

### 一次获得多个结果

只要只有一个使用标准输出,就可以同时拥有多个结果格式。例如,使用xunit结果输出到stdout并将json结果输出到文件：

```
$ avocado run sleeptest.py synctest.py --xunit - --json /tmp/result.json
<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="avocado" tests="2" errors="0" failures="0" skipped="0" time="3.64848303795" timestamp="2016-05-04 17:26:05.645665">
        <testcase classname="SleepTest" name="1-sleeptest.py:SleepTest.test" time="1.00270605087"/>
        <testcase classname="SyncTest" name="2-synctest.py:SyncTest.test" time="2.64577698708"/>
</testsuite>

$ cat /tmp/result.json
{
     "debuglog": "/home/cleber/avocado/job-results/job-2016-08-09T13.55-1a94ad6/job.log",
     "errors": 0,
     ...
}
```

但是如果没有传递给程序的 -json 项,您将无法做到这一点：

```
$ avocado run sleeptest.py synctest.py --xunit - --json -
Options --json --xunit are trying to use stdout simultaneously
Please set at least one of them to a file to avoid conflicts
```

这基本上是你需要遵循唯一,理智的的规则。

### 退出码

Avocado退出代码试图代表在执行过程中可能发生的不同事情。这意味着退出代码作为一个单独的退出代码可以是和代码组合在一起。最后的退出代码可以取消绑定,这样用户就可以对工作发生的事情有一个很好的了解。

示例如下:

* `AVOCADO_ALL_OK (0)`
* `AVOCADO_TESTS_FAIL (1)`
* `AVOCADO_JOB_FAIL (2)`
* `AVOCADO_FAIL (4)`
* `AVOCADO_JOB_INTERRUPTED (8)`

举个例子,如果一个job以退出代码9结束,它意味着我们至少有一个测试失败了,而且我们在某个时候有一个job中断,这可能是由于job超时或CTRL+C造成的。

### 实现其他结果格式

如果你想实现一种新的机器或人类可读的输出格式,你可以参考`avocado.plugins.xunit`并使用它作为起点。

f你的结果是一次生成的,基于完整的工作结果,你应该创建一个继承`avocado.core.plugin_interfaces.Result`接口的新类。并实现`avocado.core.plugin_interfaces.Result.render() `方法。

但是,如果您的结果实现是在测试之前/期间/测试之后输出信息,就要看一看`avocado.core.plugin_interfaces.ResultEvents`. 它将要求您实现对job和测试执行中的每个定义的事件执行操作(写入文件/流)的方法。

你可以看看插件系统,了解更多关于如何编写插件的信息,这些插件将激活和执行新的结果格式。

## [配置](https://avocado-framework.readthedocs.io/en/63.0/Configuration.html)

关于如何使用户喜欢使用他们的系统,Avocado有一些基于训练,合理的(我们希望)猜测的默认行为。

当然,不同的人会有不同的需求和/或不喜欢我们的默认值,这就是为什么可以用配置系统来帮助这些案例的原因。

Avocado配置文件格式是基于(非正式)INI文件的“规范”,它由Python的配置分析器实现。分段组成,格式简单明了,包含多个键和值。以一个基本的Avocado配置文件为例：

```
[datadir.paths]
base_dir = /var/lib/avocado
test_dir = /usr/share/doc/avocado/tests
data_dir = /var/lib/avocado/data
logs_dir = ~/avocado/job-results
```

datadir.paths部分包含多个键,它们都与测试工具使用的目录相关。`base_dir`是其他重要Avocado目录的基础目录,如日志、数据和测试目录。您还可以通过变量`test_dir`、`data_dir`和`logs_dir`选择设置其他重要目录。您可以通过简单编辑可用的配置文件来实现这一点。

### 配置文件解析顺序

Avocado开始解析它所称的系统范围配置文件`/etc/avocado/avocado.conf`,该文件被传输到全系统目录中的所有Avocado用户.然后,它将验证是否存在一个本地用户配置文件,该文件通常位于`~/.config/avocado/avocado.conf`.解析的顺序很重要,所以首先系统范围的文件被解析,然后用户配置文件最后被解析,这样用户可以随意重写值。还有另一个目录将被额外配置文件扫描,`/etc/avocado/conf.d`.该目录可能包含插件配置文件,以及系统管理员/Avocado开发人员可能判断需要放置的额外附加配置文件。

请注意,对于基本目录,如果您选择了不能被Avocado正确使用的目录(一些目录需要读访问、其他读取和写入访问),Avocado将回落到一些默认值。因此,如果您的普通权限用户想将日志写入到` /root/avocado/logs`,Avocado将不能使用该目录,因为它无法将文件写入该位置。默认情况下,将选择一个新的位置`~/avocado/job-results`。

本节中描述的文件顺序仅在Avocado安装在系统中才有效。对于使用Git仓库(通常是Avocado开发人员)的Avocado来说,并没有安装在系统中,请记住Avocado将读取Git仓库中存在的配置文件,并且将忽略系统范围配置文件。执行`avocado config`会让你之道哪些config文件正在实际使用。

### 插件配置文件

插件也可以通过配置文件来配置。为了不干扰主Avocado配置文件,如果希望的话,这些插件可以安装附加配置文件`/etc/avocado/conf.d/[pluginname].conf`这将在系统范围配置文件之后进行解析。用户也可以在本地配置文件级别上重写这些值。思考假想插件`salad`的配置：

```
[salad.core]
base = ceasar
dressing = ceasar
```
如果需要,可以通过在本地配置文件中简单地添加[salad.core]新部分来更改配置文件中的`dressing`,并在其中设置不同的值。

### 解析顺序重述

因此,文件解析顺序为：

* `/etc/avocado/avocado.conf`
* `/etc/avocado/conf.d/*.conf`
* `~/.config/avocado/avocado.conf`

按此顺序,意味着您在本地配置文件上设置的内容可以覆盖系统范围文件中定义的内容。

> 请注意,如果Avocado从Git 仓库中运行,这些文件将被忽略,并被配置树文件取代。这通常只会影响开发Avocado的人,如果你有疑问,`avocado config`会告诉你确切的文件在任何特定的情况下都被使用。

### 测试中使用的值的优先顺序

由于可以使用配置系统来改变测试中使用的行为和值(例如,对测试程序的思考路径),所以我们建立了以下变量优先级顺序(从最小优先级到大多数)：

* 缺省值(来自库或测试代码)
* 全局配置文件
* 本地(用户)配置文件
* 命令行开关
* 试验参数

因此,最不重要的值来自库或测试代码默认值,一直到测试参数系统。

### 配置插件

一个配置插件被提供给希望快速查看在Avocado配置的所有部分中定义的用户,在所有文件以正确的解析顺序解析之后。例子：

```
$ avocado config
Config files read (in order):
    /etc/avocado/avocado.conf
    $HOME/.config/avocado/avocado.conf

    Section.Key     Value
    runner.base_dir /var/lib/avocado
    runner.test_dir /usr/share/doc/avocado/tests
    runner.data_dir /var/lib/avocado/data
    runner.logs_dir ~/avocado/job-results
```

该命令还显示了解析配置文件的顺序,让您更好地了解正在发生的事情。关键术语在`git config --list output`得到启发。
### Avocado数据目录

当运行测试时,我们往往希望：

* 定位测试
* 将日志写入给定位置
* 抓取对测试有用的文件,例如ISO文件或VM磁盘映像

Avocado拥有一个专门用于寻找这些路径的模块,以避免人们在以前的测试框架中不得不做的繁琐的路径操作。

如果要列出所有有关测试的目录,可以使用Avocado`avocado config --datadir`命令列出这些目录。执行它会给你一个类似于下面看到的输出：

```
$ avocado config --datadir
Config files read (in order):
    /etc/avocado/avocado.conf
    $HOME/.config/avocado/avocado.conf

Avocado replaces config dirs that can't be accessed
with sensible defaults. Please edit your local config
file to customize values

Avocado Data Directories:
    base  $HOME/avocado
    tests $HOME/Code/avocado/examples/tests
    data  $HOME/avocado/data
    logs  $HOME/avocado/job-results
```

注意,虽然Avocado将尽最大努力使用配置文件中提供的配置值,如果它不能将值写入所提供的位置,它将回落到(我们希望)合理的默认值,并且我们在命令的输出中通知用户。相关的API文档和每个数据目录的含义都是在`avocado.core.data_dir`中,所以强烈建议您查看一下。

您可以通过将它们设置在Avocado配置文件中来设置首选数据文件夹。这里的重要数据文件夹的唯一例外是AvocadoTMP DIR,用来放置测试所使用的临时文件。该目录将在正常情况下`/var/tmp/avocado_XXXXX`,(XXXXX实际上是一个随机字符串)安全地创建在`/var/tmp/`上,除非用户有$TMPDIR环境变量集,因为这是UNIX程序中惯用的。

文档的下一部分说明了如何查看和设置修改Avocado实用工具和插件的行为的配置值。

## [测试发现](https://avocado-framework.readthedocs.io/en/63.0/Loaders.html)

在本节中,您可以了解测试是如何被发现的以及如何影响这个过程。

### 测试loader的顺序

Avocado支持不同类型的测试.从简单的测试开始,它是简单的可执行文件,然后是unitest-like测试,称为INSTRUMENTED,如avocado-vt的,它使用复杂的矩阵测试配置文件不直接映射到现有的文件。给定装载器的数量,从命令行上的测试名称到执行的测试的映射可能并不总是唯一的。另外,有些人可能总是(或给定的运行)希望只执行单个类型的测试。

为了调整这种行为,你可以在avocado设置(`/etc/avocado/`)中调整`plugins.loaders`,或暂时使用`--loaders`(Avocado运行选项)选项。

此选项允许您指定可用的测试加载器的顺序和一些参数。您可以指定`loader_name(file)`、 `loader_name + TEST_TYPE (file.SIMPLE)`,并且对于某些loaders,甚至附加的参数也会通过`: (external:/bin/echo -e`,您也可以提供`@DEFAULT`,它将所有剩余的未使用的loaders注入到该位置。

`--loaders` 如何影响生成的测试(手动收集,因为其中一些会导致错误)：

```
$ avocado run passtest.py boot this_does_not_exist /bin/echo
    > INSTRUMENTED passtest.py:PassTest.test
    > VT           io-github-autotest-qemu.boot
    > MISSING      this_does_not_exist
    > SIMPLE       /bin/echo
$ avocado run passtest.py boot this_does_not_exist /bin/echo --loaders @DEFAULT "external:/bin/echo -e"
    > INSTRUMENTED passtest.py:PassTest.test
    > VT           io-github-autotest-qemu.boot
    > EXTERNAL     this_does_not_exist
    > SIMPLE       /bin/echo
$ avocado run passtest.py boot this_does_not_exist /bin/echo --loaders file.SIMPLE file.INSTRUMENTED @DEFAULT external.EXTERNAL:/bin/echo
    > INSTRUMENTED passtest.py:PassTest.test
    > VT           io-github-autotest-qemu.boot
    > EXTERNAL     this_does_not_exist
    > SIMPLE       /bin/echo
    ```
### 使用参数运行简单测试

这个过去通过运行`avocado run "test arg1 arg2"`提供了现有的支持,但是它的确是很混乱并且已经被删除。但它仍然可以通过使用shell来实现,甚至可以将正常测试和参数化的测试结合起来：

```
avocado run --loaders file external:/bin/sh -- existing_file.py "'/bin/echo something'" nonexisting-file
```

这将运行3个测试,第一个测试是由existing_file.py定义的正常测试(很可能是一个仪器化测试)。然后我们将通过`/bin/sh -c '/bin/echo something'`执行`/bin/echo someting`。最后一个将是`nonexisting-file`,它将执行`/bin/sh -c nonexisting-file`,这很可能会失败的。

请注意,您负责引用测试ID(请参阅"'/bin/echo something'"示例)。

### 通过标签过滤测试

Avocado允许测试提供标签,可以用来创建测试类别。使用标签集,用户可以选择由测试解析器(也称为测试加载器)找到的测试的子集。有关测试标记的更多信息,请访问 [WritingTests.html#categorizing-tests](https://avocado-framework.readthedocs.io/en/63.0/WritingTests.html#categorizing-tests)。

### 测试引用 Test References

测试引用是一个字符串,可以通过Avocado测试解析器解析为(解释为)一个或多个测试。

每个解析器(a.k.a加载器)可以不同地处理测试引用。例如,外部加载器将使用测试引用作为外部命令的参数,而文件加载器将期望文件路径。

如果不指定要使用的加载器,则所有可用的加载器将用于解析所提供的测试引用。一个接一个地,测试引用将由第一个加载程序解决,该第一个加载程序能够从该引用中创建测试列表。

下面你可以找到一些具体的内置Avocado装载机的细节。对于通过插件(VT, Robot…)引入Avocado的装载机,请参阅相应的加载 loader/plugin 文档。

#### 文件加载器

对于文件加载器,加载器负责发现 INSTRUMENTED, PyUNITTEST(经典Python UNITTEST)和SIMPLE测试。

如果文件对应于 INSTRUMENTED 或 PyUNITTEST,可以通过在测试引用后面添加`：`,来筛选测试ID,`：`后面是正则表达式。

例如,如果您想列出所有在gdbtest.py文件中存在的测试,可以使用下面的列表命令：

```
$ avocado list /usr/share/doc/avocado/tests/gdbtest.py
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_start_exit
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_existing_commands_raw
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_existing_commands
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_load_set_breakpoint_run_exit_raw
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_load_set_breakpoint_run_exit
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_generate_core
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_set_multiple_break
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_disconnect_raw
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_disconnect
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_remote_exec
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_stream_messages
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_connect_multiple_clients
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_server_exit
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_multiple_servers
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_interactive
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_interactive_args
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_exit_status
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_server_stderr
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_server_stdout
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_interactive_stdout
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_remote
```
若要筛选结果,只列出在测试方法名称中具有test_interactive的测试,则可以执行：

```
$ avocado list /usr/share/doc/avocado/tests/gdbtest.py:test_interactive
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_interactive
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_interactive_args
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_interactive_stdout
```

`：`之后的字符串是正则表达式,三个测试被过滤进去。您可以操作正则表达式,使其具有确切名称的测试：

```
$ avocado list /usr/share/doc/avocado/tests/gdbtest.py:test_interactive$
INSTRUMENTED /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_interactive
```

一旦测试引用提供了预期的结果,您就可以用Run子命令替换列表子命令来执行测试：

```
$ avocado run /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_[le].*raw
JOB ID     : 333912fb02698ed5339a400b832795a80757b8af
JOB LOG    : $HOME/avocado/job-results/job-2017-06-14T14.54-333912f/job.log
 (1/2) /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_existing_commands_raw: PASS (0.59 s)
 (2/2) /usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_load_set_breakpoint_run_exit_raw: PASS (0.42 s)
RESULTS    : PASS 2 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 0
JOB TIME   : 1.15 s
JOB HTML   : $HOME/avocado/job-results/job-2017-06-14T14.54-333912f/html/results.html
```

> 特别是在使用正则表达式时,建议单独用引号包裹测试引用,以避免损坏它们。在这种情况下,上述示例的命令将是：

```
avocado run "/usr/share/doc/avocado/tests/gdbtest.py:GdbTest.test_[le].*raw"
```

#### 外部加载器

使用External Loader, Avocado 会考虑它,External
Runner 将会就位,所以Avocado不会真的去解析这个引用. 相反,Avocaddo将把引用作为参数传递给这个External Runner. 示例:

```
$ avocado run 20
Unable to resolve reference(s) '20' with plugins(s) 'file', 'robot',
'vt', 'external', try running 'avocado list -V 20' to see the details.
```

在上面的命令中,没有加载程序可以将`20`解析为一个测试.但是在上面的命令中台添加一个 External Runner `/bin/sleep` 将会使 Avocado 执行 `/bin/sleep 20` 并且检查它返回的代码:

```
$ avocado run 20 --loaders external:/bin/sleep
JOB ID     : 42215ece2894134fb9379ee564aa00f1d1d6cb91
JOB LOG    : $HOME/avocado/job-results/job-2017-06-19T11.17-42215ec/job.log
 (1/1) 20: PASS (20.03 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 0
JOB TIME   : 20.13 s
JOB HTML   : $HOME/avocado/job-results/job-2017-06-19T11.17-42215ec/html/results.html
```

将测试引用放在命令行的末尾, 在一个 – 之后更安全. 这将避免争论与测试引用冲突。在这种情况下,之后的所有内容都将被视为位置参数。考虑以上语法, 上个例子的命令是:

```
avocado run --loaders external:/bin/sleep -- 20
```

## [日志系统](https://avocado-framework.readthedocs.io/en/63.0/LoggingSystem.html)

本节介绍日志系统在Avocado和Avocado试验中的应用。

### 调整UI

Avocado使用Python的日志系统来生成UI并存储测试输出。该系统非常灵活,允许您通过内置流集或直接使用流名称来调整输出到您的需求。要调整它们,可以使用 ` avocado -–show STREAM[:LEVEL][,STREAM[:LEVEL],…] run ...`。具有描述的内置流(随后是相关联的Python流列表)：

app:    基于文本的UI (avocado.app)
test:   执行测试的输出 (avocado.test, "")
debug:  用于调试avocado的附加消息 (avocado.app.debug)
remote: Fabric/paramiko 调试消息,用于分析远程执行 (avocado.fabric, paramiko)
early:  在日志记录系统设置之前进行早期日志记录。它包括测试输出和由使用的库产生的大量输出 ("", avocado.test)

另外,您可以指定“全部”或“否”来启用/禁用所有预定义流,还可以提供自定义Python日志流,并将它们传递到标准输出。

### 存储自定义日志

当您运行测试时,您还可以通过`avocado run –store-logging-stream [STREAM[:LEVEL] [STREAM[:LEVEL] …]]`将自定义日志流存储到结果目录中,它将在测试结果目录中生成每一个(唯一的)条目的`$STREAM.$LEVEL`文件。

> 必须指定分离的日志流。在这个函数中不能使用内置流。

> 目前,自定义流仅存储在每个job中,而不是针对每个单独的测试。

### 分页器

一些子命令(列表,插件,…)支持"paginator",在兼容的终端上,基本上将有色输出管道设置为较少,以简化生成的输出的浏览。可以通过–paginator {on|off}.禁用它。

## [sysinfo收集](https://avocado-framework.readthedocs.io/en/63.0/Sysinfo.html)

Avocado附带一个sysinfo插件,它自动收集每个系统的系统信息,甚至在测试之间。当我们想知道是什么导致测试失败是这是非常有用的。这个系统是可配置的,但是我们为您提供了一组明智的默认值。

在 Avocado 默认配置 `/etc/avocado/avocado.conf`有一节`sysinfo.collect`您可以在其中启用/禁用sysinfo集合以及配置基本环境。在`sysinfo.collectibles`节中,您可以定义在何处寻找sysinfo 集合之前/期间执行哪些命令/任务的基本路径。Avocado支持三种类型的任务：

* command: 用新行分隔的命令列表,在job/test之前和之后执行命令(单执行命令)。可以通过在[sysinfo.collect]中设置commands_timeout为正数来为每个执行命令所执行的超时。
* file: 使用新行分隔的文件列表,表示要复制的文件
* profilers: 文件具有新的行分隔的命令列表,在job/test之前执行并在job/test结束时被杀死(类似命令)

此外,这个插件试图通过`journalctl`跟踪系统日志,如果可用的话。

默认情况下,每个job都会收集这些数据,但也可以通过在`sysinfo.collect`节中设置`per_test = True`在每个test中运行它们。

如果需要的话,也可以在命令行上通过`--sysinfo on|off`来启用/禁用sysinfo。

job执行后,您可以在`$RESULTS/test-results/$TEST/sysinfo`的`$RESULTS/sysinfo`找到所收集的信息,它被分类为前、后和概要文件夹,文件名是安全地执行命令或文件名。当您启用HTML结果插件时,还可以在HTML结果中看到sysinfo。

> 如果使用源代码的Avocado,则需要手动放置`commands/files/profilers`到`/etc/avocado/sysinfo`或者调整`$AVOCADO_SRC/etc/avocado/avocado.conf`的路径

> 译者: 使用pip 安装的配置文件在诸如`/usr/lib/python3.6/site-packages/avocado/etc/avocado/avocado.conf`路径中,真实路径可以使用`avocado config`命令进行查询

## [测试参数](https://avocado-framework.readthedocs.io/en/63.0/TestParameters.html)

本节详细介绍了哪些测试参数以及整个变体机制在Avocado中的工作原理。 如果您对基础知识感兴趣,请参阅Yaml_to_mux插件中的示例访问测试参数或实际视图。

Avocado允许将参数传递给测试,这有效地导致每个测试的几种不同变体。 这些参数在(test)的`self.params`中可用,并且是`avocado.core.varianter.AvocadoParams`类型。

`self.params`的数据由`avocado.core.varianter.Varianter`提供,它会询问所有已注册的插件的变体,或者在没有定义变体时使用默认值。

params处理如何工作的总体情况是：

```
    +-----------+
    |           |  // Test使用variant来生成AvocadoParams
    |   Test    |
    |           |
    +-----^-----+
          |  // 将单个变量传递给测试
          |
    +-----------+
    |  Runner   |  // 迭代测试和变量来运行所有
    +-----^-----+  // 由“--execution-order”指定的所需组合
          |
          |
+-------------------+     提供变量      +-----------------------+
|                   |<-----------------|                       |
| Varianter API     |                  | Varianter plugins API |
|                   |----------------->|                       |
+-------------------+    更新默认值     +-----------------------+
          ^                                ^
          |                                |
          |  // 默认参数注入                |  // 调用所有插件
+--------------------------------------+   |  // 轮流
| +--------------+ +-----------------+ |   |
| | avocado-virt | | other providers | |   |
| +--------------+ +-----------------+ |   |
+--------------------------------------+   |
                                           |
              +----------------------------+-----+
              |                                  |
              |                                  |
              v                                  v
    +--------------------+           +-------------------------+
    | yaml_to_mux plugin |           | Other variant plugin(s) |
    +-----^--------------+           +-------------------------+
          |
          |  // yaml 被解析为 MuxTree,
          |  // multiplexed and yields variants
    +---------------------------------+
    | +------------+ +--------------+ |
    | | --mux-yaml | | --mux-inject | |
    | +------------+ +--------------+ |
    +---------------------------------+
```

我们来介绍一下基本的关键词。

### TreeNode

`avocado.core.tree.TreeNode`

节点对象是否允许使用parent-> multiple_children关系创建树状结构并存储参数。 它还可以报告它的环境,这是从根到此节点收集的一组参数。 这用于测试,而不是传递完整树,只传递叶节点,它们的环境代表树的所有值

### AvocadoParams

`avocado.core.varianter.AvocadoParams`

在每个(instrumented)Avocado测试中存在params的“数据库”。 它是在avocado.core.test.Test的__init__期间,从变量中生成的。 它接受TreeNode对象列表; 测试名称`avocado.core.test.TestID`(用于记录目的)和默认路径列表(参数路径)。

在测试中,它允许使用以下方法查询数据：

```
self.params.get($name, $path=None, $default=None)
```

* name - 参数名称(键)
* path - 查找此参数的位置(未指定时使用mux-path)
* default - 找不到param时返回的内容(默认值)

每个变量都定义了一个层次结构,该层次结构会被保留,因此AvocadoParams跟随它以返回最合适的值或在出错时引发异常。

### 参数路径 Parameter Paths

由于测试参数在树中组织,因此可以在多个位置具有相同的变量。 当它们从同一个TreeNode生成时,它不是问题,但是当它们是不同的值时,无法区分应报告的内容。 一种方法是在询问参数时使用特定路径,但有时候,通常在组合上游和下游变体时,我们希望首先得到我们的值,然后在找不到它们时回退到上游值。

例如,假设我们在`/upstream/sleeptest`中有上游值,并且在`/downstream/sleeptest`中也有值。 如果我们使用路径"*"询问值,则会引发异常,因为程序无法区分是否需要来自"/downstream"或"/upstream"的值。 我们可以将参数路径设置为["/downstream/*","/upstream/*"]以使所有相对调用(以*开头的路径)首先查看/downstream中的节点,如果未找到则查看/ upstream。

### Variant

Variant是由Varianter_s生成的一组参数,并由测试运行员作为“params”参数传递给测试。 最简单的变体是`None`,它仍然会生成一个空的`AvocadoParams`。 此外,变量也可以是元组(列表,路径)或只是带有参数的`avocado.core.tree.TreeNode`列表。

### Dumping/Loading Variants

根据参数的数量,生成变量可能非常耗费计算量。 由于变量是作为作业执行的一部分生成的,因此计算密集型任务将由被测系统执行,从而导致这些系统上可能不需要的CPU负载。

为了避免这种情况,您可以获取由变量计算生成的生成的JSON序列化变体文件,并将该文件加载到将执行作业的系统上。

有两种方法可以获取JSON序列化变体文件：

* 使用avocado variants命令的--json-variants-dump选项：

```
$ avocado variants --mux-yaml examples/yaml_to_mux/hw/hw.yaml --json-variants-dump variants.json
...

$ file variants.json
variants.json: ASCII text, with very long lines, with no line terminators
```
* 执行Avocado作业后获取自动生成的JSON序列化变体文件：

```
 avocado run passtest.py --mux-yaml examples/yaml_to_mux/hw/hw.yaml
...

$ file $HOME/avocado/job-results/latest/jobdata/variants.json
$HOME/avocado/job-results/latest/jobdata/variants.json: ASCII text, with very long lines, with no line terminators
```

获得variants.json文件后,可以将其加载到将要执行作业的系统上：

```
$ avocado run passtest.py --json-variants-load variants.json
JOB ID     : f2022736b5b89d7f4cf62353d3fb4d7e3a06f075
JOB LOG    : $HOME/avocado/job-results/job-2018-02-09T14.39-f202273/job.log
 (1/6) passtest.py:PassTest.test;intel-scsi-56d0: PASS (0.04 s)
 (2/6) passtest.py:PassTest.test;intel-virtio-3d4e: PASS (0.02 s)
 (3/6) passtest.py:PassTest.test;amd-scsi-fa43: PASS (0.02 s)
 (4/6) passtest.py:PassTest.test;amd-virtio-a59a: PASS (0.02 s)
 (5/6) passtest.py:PassTest.test;arm-scsi-1c14: PASS (0.03 s)
 (6/6) passtest.py:PassTest.test;arm-virtio-5ce1: PASS (0.04 s)
RESULTS    : PASS 6 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 0
JOB TIME   : 0.51 s
JOB HTML   : $HOME/avocado/job-results/job-2018-02-09T14.39-f202273/results.html
```


### Varianter

`avocado.core.varianter.Varianter`是一个内部对象,用于与Avocado中的变体机制进行交互。 它的生命周期是两个阶段的复合。 首先,它允许核心/插件注入默认值,然后对其进行解析,只允许查询值,变体数量等。

avocado run passtest.py -m example.yaml的示例工作流程是：

```
avocado run passtest.py -m example.yaml
  |
  + parser.finish -> Varianter.__init__  // dispatcher initializes all plugins
  |
  + $PLUGIN -> args.default_avocado_params.add_default_param  // could be used to insert default values
  |
  + job.run_tests -> Varianter.is_parsed
  |
  + job.run_tests -> Varianter.parse
  |                     // processes default params
  |                     // initializes the plugins
  |                     // updates the default values
  |
  + job._log_variants -> Varianter.to_str  // prints the human readable representation to log
  |
  + runner.run_suite -> Varianter.get_number_of_tests
  |
  + runner._iter_variants -> Varianter.itertests  // Yields variants
```
为了允许强制更新Varianter,它支持ignore_new_data,可用于忽略新数据。 Job Replay使用它将当前运行的Varianter替换为从重放作业加载的Varianter。 ignore_new_data的工作流程可能如下所示：

```
avocado run --replay latest -m example.yaml
  |
  + $PLUGIN -> args.default_avocado_params.add_default_param  // could be used to insert default values
  |
  + replay.run -> Varianter.is_parsed
  |
  + replay.run  // Varianter object is replaced with the replay job's one
  |             // Varianter.ignore_new_data is set
  |
  + $PLUGIN -> args.default_avocado_params.add_default_param  // is ignored as new data are not accepted
  |
  + job.run_tests -> Varianter.is_parsed
  |
  + job._log_variants -> Varianter.to_str
  |
  + runner.run_suite -> Varianter.get_number_of_tests
  |
  + runner._iter_variants -> Varianter.itertests
```
Varianter本身只能使用Default params生成一个空变量,但是它会调用所有Varianter插件,如果它们中的任何一个报告变量,它会生成它们而不是默认变量。

### Default params

Default params是一种在Varianter或Varianter插件中指定默认值的机制。 它们的目的通常是定义依赖于系统的值,这些值不应影响测试的结果。 一个例子是qemu二进制位置,它可能因主机而异,但最终它们应该导致qemu在测试中可执行。 因此,Default params不会影响测试的variant-id(至少不会影响官方的Varianter插件)。

可以通过从args获取default_avocado_params并使用以下命令从plugin/core设置这些参数：

```
default_avocado_params.add_default_parma(self, name, key, value, path=None)
```

name - 注入数据的插件的名称(尚未用于任何内容,但我们计划允许白/黑列表)
key - 参数的名称
value - 参数的值
path - 此参数的位置。 当路径尚不存在时,它是由TreeNode创建的。

### Varianter plugins

`avocado.core.plugin_interfaces.Varianter` 一个插件接口,可用于构建自定义插件,Varianter使用它来获取测试变体。 有关灵感,请参阅avocado_varianter_yaml_to_mux.YamlToMux这是一个可选的varianter插件。 有关此插件的详细信息,请访问Yaml_to_mux插件。

### Multiplexer

avocado.core.mux

Multiplexer或简称Mux是一个抽象概念,它是树状参数结构背后的基本思想,支持产生所有可能的变体。 在创建自定义插件时可以使用基本构建块的核心实现。 在avocado_varianter_yaml_to_mux中有一个使用此概念的插件的演示版本,它添加了一个解析器,然后使用此多路复用器概念来定义一个avocado插件,以便从yaml(或json)文件生成变体。

#### Multiplexer concept

如前所述,这是构建块的内核实现,旨在基于定义了Multiplex域的树来编写Varianter插件。 可用的块是：

* MuxTree - 表示树的一部分并处理多路复用的对象,这意味着从树状对象生成所有可能的变体。
* MuxPlugin - 构建Varianter插件的基类
* MuxTreeNode - 从TreeNode继承并添加对控制标志(MuxTreeNode.ctrl)和Multiplex域(MuxTreeNode.multiplex)的支持。

### Multiplex domains

带变量的默认AvocadoParams树可能如下所示：

```
Multiplex tree representation:
 ┣━━ paths
 ┃     → tmp: /var/tmp
 ┃     → qemu: /usr/libexec/qemu-kvm
 ┗━━ environ
     → debug: False
```

多路复用器想要产生类似的结构,但也能够定义不仅一个变体,而是定义所有可能的组合,然后将切片报告为变体。 我们使用术语Multiplex域来定义此节点的子节点不仅仅是不同的路径,但它们是不同的值,我们一次只需要一个。 在表示中,我们使用双线来可视地区分正常关系和多路关系。 让我们稍微修改一下我们的例子：

```
Multiplex tree representation:
 ┣━━ paths
 ┃     → tmp: /var/tmp
 ┃     → qemu: /usr/libexec/qemu-kvm
 ┗━━ environ
      ╠══ production
      ║     → debug: False
      ╚══ debug
            → debug: True
```

不同之处在于environ现在是一个多重节点,它的子节点将一次产生一个,产生两个变体：

```
Variant 1:
 ┣━━ paths
 ┃     → tmp: /var/tmp
 ┃     → qemu: /usr/libexec/qemu-kvm
 ┗━━ environ
      ┗━━ production
            → debug: False
Variant 2:
 ┣━━ paths
 ┃     → tmp: /var/tmp
 ┃     → qemu: /usr/libexec/qemu-kvm
 ┗━━ environ
      ┗━━ debug
            → debug: False
```
请注意,Multiplex仅与直接子项有关,因此变体中的叶数可能不同：

```
Multiplex tree representation:
 ┣━━ paths
 ┃     → tmp: /var/tmp
 ┃     → qemu: /usr/libexec/qemu-kvm
 ┗━━ environ
      ╠══ production
      ║     → debug: False
      ╚══ debug
           ┣━━ system
           ┃     → debug: False
           ┗━━ program
                 → debug: True
```
使用/ paths和/ paths,/ environ / debug / system和/ environ / debug / program生成一个带/ paths和/ environ / production的变体和其他变体。

如前所述,权力不是产生一种变体,而是定义具有所有可能变体的巨大情景。 通过使用具有多重域的树结构,您可以避免从Jenkin的稀疏矩阵作业中可能知道的大多数丑陋过滤器。 为了比较,我们来看看Avocado中的相同例子：

```
Multiplex tree representation:
 ┗━━ os
      ┣━━ distro
      ┃    ┗━━ redhat
      ┃         ╠══ fedora
      ┃         ║    ┣━━ version
      ┃         ║    ┃    ╠══ 20
      ┃         ║    ┃    ╚══ 21
      ┃         ║    ┗━━ flavor
      ┃         ║         ╠══ workstation
      ┃         ║         ╚══ cloud
      ┃         ╚══ rhel
      ┃              ╠══ 5
      ┃              ╚══ 6
      ┗━━ arch
           ╠══ i386
           ╚══ x86_64
```

```
Variant 1:    /os/distro/redhat/fedora/version/20, /os/distro/redhat/fedora/flavor/workstation, /os/arch/i386
Variant 2:    /os/distro/redhat/fedora/version/20, /os/distro/redhat/fedora/flavor/workstation, /os/arch/x86_64
Variant 3:    /os/distro/redhat/fedora/version/20, /os/distro/redhat/fedora/flavor/cloud, /os/arch/i386
Variant 4:    /os/distro/redhat/fedora/version/20, /os/distro/redhat/fedora/flavor/cloud, /os/arch/x86_64
Variant 5:    /os/distro/redhat/fedora/version/21, /os/distro/redhat/fedora/flavor/workstation, /os/arch/i386
Variant 6:    /os/distro/redhat/fedora/version/21, /os/distro/redhat/fedora/flavor/workstation, /os/arch/x86_64
Variant 7:    /os/distro/redhat/fedora/version/21, /os/distro/redhat/fedora/flavor/cloud, /os/arch/i386
Variant 8:    /os/distro/redhat/fedora/version/21, /os/distro/redhat/fedora/flavor/cloud, /os/arch/x86_64
Variant 9:    /os/distro/redhat/rhel/5, /os/arch/i386
Variant 10:    /os/distro/redhat/rhel/5, /os/arch/x86_64
Variant 11:    /os/distro/redhat/rhel/6, /os/arch/i386
Variant 12:    /os/distro/redhat/rhel/6, /os/arch/x86_64
```
与Jenkin的稀疏矩阵对比：

```
os_version = fedora20 fedora21 rhel5 rhel6
os_flavor = none workstation cloud
arch = i386 x86_64

filter = ((os_version == "rhel5").implies(os_flavor == "none") &&
          (os_version == "rhel6").implies(os_flavor == "none")) &&
         !(os_version == "fedora20" && os_flavor == "none") &&
         !(os_version == "fedora21" && os_flavor == "none")
```

这仍然是一个相对简单的例子,但它随着内部依赖性而急剧增长。

### MuxPlugin

定义avocado.core.plugin_interfaces.Varianter所需的完整接口。 插件编写者应该从这个MuxPlugin继承,然后从Varianter继承并调用：

`self.initialize_mux(root, paths, debug)`

* root - 是params树的根(类似TreeNode节点的复合体)
* paths - 是测试中使用的所有变体的参数路径
* debug - 是否使用调试模式(要求传递的树是TreeNodeDebug类节点的复合,它存储变量/值/环境的来源作为列表用途的值,并且__NOT__用于测试执行。

### MuxTree

这是努力工作的核心功能。 当在搜索叶节点时到达另一个multiplex时,它遍历树并记住所有叶节点或使用MuxTree列表。

当它被要求报告变体时,它组合了每个记忆项目的一个变体(叶子节点始终保持不变,但MuxTree圈出它的值),递归地产生不同多重域的所有可能变体。

## [工作重演](https://avocado-framework.readthedocs.io/en/63.0/Replay.html)

为了使用相同的数据再现给定的job,我们可以使用`--replay`选项执行`run`命令,从原始job中得知hash id以实现重演.hash id可以只是一部分,只要所提供的部分对应于原始job id,并且它也足够独特。或者,代替jo
b id,您可以使用最新的字符串,Avocado将重演最新执行的job。

让我们来看一个例子。首先,用两个测试引用运行一个简单的job：

```
$ avocado run /bin/true /bin/false
JOB ID     : 825b860b0c2f6ec48953c638432e3e323f8d7cad
JOB LOG    : $HOME/avocado/job-results/job-2016-01-11T16.14-825b860/job.log
 (1/2) /bin/true: PASS (0.01 s)
 (2/2) /bin/false: FAIL (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 1 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.12 s
JOB HTML   : $HOME/avocado/job-results/job-2016-01-11T16.14-825b860/html/results.html
```
现在我们可以重新运行这个job：

```
$ avocado run --replay 825b86
JOB ID     : 55a0d10132c02b8cc87deb2b480bfd8abbd956c3
SRC JOB ID : 825b860b0c2f6ec48953c638432e3e323f8d7cad
JOB LOG    : $HOME/avocado/job-results/job-2016-01-11T16.18-55a0d10/job.log
 (1/2) /bin/true: PASS (0.01 s)
 (2/2) /bin/false: FAIL (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 1 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.11 s
JOB HTML   : $HOME/avocado/job-results/job-2016-01-11T16.18-55a0d10/html/results.html
```

回放功能将检索原始测试引用、变量和配置。让我们看看另一个例子,现在使用mux YAML文件：

```
$ avocado run /bin/true /bin/false --mux-yaml mux-environment.yaml
JOB ID     : bd6aa3b852d4290637b5e771b371537541043d1d
JOB LOG    : $HOME/avocado/job-results/job-2016-01-11T21.56-bd6aa3b/job.log
 (1/4) /bin/true;first-c49a: PASS (0.01 s)
 (2/4) /bin/true;second-f05f: PASS (0.01 s)
 (3/4) /bin/false;first-c49a: FAIL (0.04 s)
 (4/4) /bin/false;second-f05f: FAIL (0.04 s)
RESULTS    : PASS 2 | ERROR 0 | FAIL 2 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.19 s
JOB HTML   : $HOME/avocado/job-results/job-2016-01-11T21.56-bd6aa3b/html/results.html
```

我们可以使用`$ avocado run --replay latest`重新运行job,或者忽略变量运行job

```
$ avocado run --replay bd6aa3b --replay-ignore variants
Ignoring variants from source job with --replay-ignore.
JOB ID     : d5a46186ee0fb4645e3f7758814003d76c980bf9
SRC JOB ID : bd6aa3b852d4290637b5e771b371537541043d1d
JOB LOG    : $HOME/avocado/job-results/job-2016-01-11T22.01-d5a4618/job.log
 (1/2) /bin/true: PASS (0.01 s)
 (2/2) /bin/false: FAIL (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 1 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.12 s
JOB HTML   : $HOME/avocado/job-results/job-2016-01-11T22.01-d5a4618/html/results.html
```
此外,可以只重演给定结果的变体,使用`--replay-test-status`选项,查看以下示例:

```
$ avocado run --replay bd6aa3b --replay-test-status FAIL
JOB ID     : 2e1dc41af6ed64895f3bb45e3820c5cc62a9b6eb
SRC JOB ID : bd6aa3b852d4290637b5e771b371537541043d1d
JOB LOG    : $HOME/avocado/job-results/job-2016-01-12T00.38-2e1dc41/job.log
 (1/4) /bin/true;first-c49a: SKIP
 (2/4) /bin/true;second-f05f: SKIP
 (3/4) /bin/false;first-c49a: FAIL (0.03 s)
 (4/4) /bin/false;second-f05f: FAIL (0.04 s)
RESULTS    : PASS 0 | ERROR 0 | FAIL 24 | SKIP 24 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.29 s
JOB HTML   : $HOME/avocado/job-results/job-2016-01-12T00.38-2e1dc41/html/results.html
```
其中一个特殊的例子是`--replay-test-status INTERRUPTED`或`--replay-resume`,它跳过所执行的测试,只执行取消测试后取消或未执行的测试。这个特性即使在系统崩溃等严重中断时也可以工作。

在重演用`--failfast on`选项执行的job时,可以使用`--failfast off`禁用`failfast` 选项重演job。

为了能够重演job,Avocado将job数据记录在同一个job结果目录中,在一个名为`replay`的子目录内。如果给定的job有一个非默认路径来记录日志,当重播时间到来时,我们需要通知日志在何处。见下面的例子：

```
$ avocado run /bin/true --job-results-dir /tmp/avocado_results/
JOB ID     : f1b1c870ad892eac6064a5332f1bbe38cda0aaf3
JOB LOG    : /tmp/avocado_results/job-2016-01-11T22.10-f1b1c87/job.log
 (1/1) /bin/true: PASS (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.11 s
JOB HTML   : /tmp/avocado_results/job-2016-01-11T22.10-f1b1c87/html/results.html
```
试图重演这项job,但失败了:

```
$ avocado run --replay f1b1
can't find job results directory in '$HOME/avocado/job-results'
```

在这种情况下,我们必须通知工作结果目录位于何处：

```
$ avocado run --replay f1b1 --replay-data-dir /tmp/avocado_results
JOB ID     : 19c76abb29f29fe410a9a3f4f4b66387570edffa
SRC JOB ID : f1b1c870ad892eac6064a5332f1bbe38cda0aaf3
JOB LOG    : $HOME/avocado/job-results/job-2016-01-11T22.15-19c76ab/job.log
 (1/1) /bin/true: PASS (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0
JOB TIME   : 0.11 s
JOB HTML   : $HOME/avocado/job-results/job-2016-01-11T22.15-19c76ab/html/results.html
```
## [工作差异](https://avocado-framework.readthedocs.io/en/63.0/Diff.html)

Avocadodiff插件允许用户轻松地比较两个给定的job的几个方面。基本用法是：

```
$ avocado diff 7025aaba 384b949c
--- 7025aaba9c2ab8b4bba2e33b64db3824810bb5df
+++ 384b949c991b8ab324ce67c9d9ba761fd07672ff
@@ -1,15 +1,15 @@

 COMMAND LINE
-/usr/bin/avocado run sleeptest.py
+/usr/bin/avocado run passtest.py

 TOTAL TIME
-1.00 s
+0.00 s

 TEST RESULTS
-1-sleeptest.py:SleepTest.test: PASS
+1-passtest.py:PassTest.test: PASS

 ...
 ```
Avocado Diff可以比较和创建一个统一的差异：

* 命令行
* 工作时间
* 变量和参数
* 测试结果
* 配置
* sysinfo前后

结果中只包含不同内容的部分。还可以使用`--diff-filter`启用/禁用这些部分。请参阅`avocado diff --help`更多信息。

可以通过jobs ID、结果目录或`latest`来标识job。示例：

```
$ avocado diff ~/avocado/job-results/job-2016-08-03T15.56-4b3cb5b/ latest
--- 4b3cb5bbbb2435c91c7b557eebc09997d4a0f544
+++ 57e5bbb3991718b216d787848171b446f60b3262
@@ -1,9 +1,9 @@

 COMMAND LINE
-/usr/bin/avocado run perfmon.py
+/usr/bin/avocado run passtest.py

 TOTAL TIME
-11.91 s
+0.00 s

 TEST RESULTS
-1-test.py:Perfmon.test: FAIL
+1-examples/tests/passtest.py:PassTest.test: PASS
```
与统一的差异,你也可以生成HTML(选项 `--html`)差异文件,并可选地,打开它在您的首选浏览器(选项 `--open browser`)：

```
$ avocado diff 7025aaba 384b949c --html /tmp/myjobdiff.html
/tmp/myjobdiff.html
```

如果在没有`--html`的情况下使用 `--open browser`,我们将创建一个临时HTML文件。

对于那些希望使用自定义DIFF工具而不是Avocado DIFF工具的人,我们提供了`--create-reports`选项,因此我们创建了两个具有相关内容的临时文件。打印文件名,用户可以复制/粘贴到自定义DIFF工具命令行：

```
$ avocado diff 7025aaba 384b949c --create-reports
/var/tmp/avocado_diff_7025aab_zQJjJh.txt /var/tmp/avocado_diff_384b949_AcWq02.txt

$ diff -u /var/tmp/avocado_diff_7025aab_zQJjJh.txt /var/tmp/avocado_diff_384b949_AcWq02.txt
--- /var/tmp/avocado_diff_7025aab_zQJjJh.txt    2016-08-10 21:48:43.547776715 +0200
+++ /var/tmp/avocado_diff_384b949_AcWq02.txt    2016-08-10 21:48:43.547776715 +0200
@@ -1,250 +1,19 @@

 COMMAND LINE
 ============
-/usr/bin/avocado run sleeptest.py
+/usr/bin/avocado run passtest.py

 TOTAL TIME
 ==========
-1.00 s
+0.00 s

...
```

## [远程运行测试](https://avocado-framework.readthedocs.io/en/63.0/RunningTestsRemotely.html)
## [Avocado子类](https://avocado-framework.readthedocs.io/en/63.0/SubclassingAvocado.html)

使用子类来扩展Avocado测试类的特性是非常直接的,它可能构成了一个非常有用的办法,在项目存储库中托管一些共享/递归代码。

在本文档中,我们提出了一个项目组织,允许您创建和安装所谓的子框架。

让我们举个例子,一个叫做Apricot Framework的项目。这里是提议的文件系统结构：

```
~/git/apricot (master)$ tree
.
├── apricot
│   ├── __init__.py
│   └── test.py
├── README.rst
├── setup.py
├── tests
│   └── test_example.py
└── VERSION
```
在SETUP.PY中,将Avocado框架包指定为依赖项是很重要的：

```
from setuptools import setup, find_packages

setup(name='apricot',
      description='Apricot - Avocado SubFramwork',
      version=open("VERSION", "r").read().strip(),
      author='Apricot Developers',
      author_email='apricot-devel@example.com',
      packages=['apricot'],
      include_package_data=True,
      install_requires=['avocado-framework']
      )
```

VERSION: 你希望的文件版本

```
1.0
```
`apricot/__init__.py`:使您的新测试类在您的模块根目录中可用：

```
__all__ = ['ApricotTest']

from apricot.test import ApricotTest
```

`apricot/test.py`,在这里,您将基本上扩展Avocado测试类与您自己的方法和程序：

```python
from avocado import Test

class ApricotTest(Test):
    def setUp(self):
        self.log.info("setUp() executed from Apricot")

    def some_useful_method(self):
        return True
```

`tests/test_example.py`:这就是测试的样子。这里最重要的一项是使用`:avocado: recursive`递归,所以Avocado测试加载器将能够识别您的测试类作为Avocado测试类：

```python
from apricot import ApricotTest

class MyTest(ApricotTest):
    """
    :avocado: recursive
    """
    def test(self):
        self.assertTrue(self.some_useful_method())
```

非侵入的安装你的模块:

```
~/git/apricot (master)$ python setup.py develop --user
running develop
running egg_info
writing requirements to apricot.egg-info/requires.txt
writing apricot.egg-info/PKG-INFO
writing top-level names to apricot.egg-info/top_level.txt
writing dependency_links to apricot.egg-info/dependency_links.txt
reading manifest file 'apricot.egg-info/SOURCES.txt'
writing manifest file 'apricot.egg-info/SOURCES.txt'
running build_ext
Creating /home/apahim/.local/lib/python2.7/site-packages/apricot.egg-link (link to .)
apricot 1.0 is already the active version in easy-install.pth

Installed /home/apahim/git/apricot
Processing dependencies for apricot==1.0
Searching for avocado-framework==55.0
Best match: avocado-framework 55.0
avocado-framework 55.0 is already the active version in easy-install.pth

Using /home/apahim/git/avocado
Searching for stevedore==1.25.0
Best match: stevedore 1.25.0
Adding stevedore 1.25.0 to easy-install.pth file

Using /usr/lib/python2.7/site-packages
Searching for six==1.10.0
Best match: six 1.10.0
Adding six 1.10.0 to easy-install.pth file

Using /usr/lib/python2.7/site-packages
Searching for pbr==3.1.1
Best match: pbr 3.1.1
Adding pbr 3.1.1 to easy-install.pth file
Installing pbr script to /home/apahim/.local/bin

Using /usr/lib/python2.7/site-packages
Finished processing dependencies for apricot==1.0
```

然后运行你的测试

```
~/git/apricot$ avocado run tests/test_example.py
JOB ID     : 02c663eb77e0ae6ce67462a398da6972791793bf
JOB LOG    : $HOME/avocado/job-results/job-2017-11-16T12.44-02c663e/job.log
 (1/1) tests/test_example.py:MyTest.test: PASS (0.03 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 0
JOB TIME   : 0.95 s
JOB HTML   : $HOME/avocado/job-results/job-2017-11-16T12.44-02c663e/results.html
```


## [使用GDB Debugging](https://avocado-framework.readthedocs.io/en/63.0/DebuggingWithGDB.html)

## [通过测试运行可执行包](https://avocado-framework.readthedocs.io/en/63.0/WrapProcess.html)

Avocado允许可执行文件的测试以易懂的方式运行。用户指定一个脚本("包装器"),用于运行由测试调用的实际程序。

如果测试脚本被正确实现,它不应该干扰测试行为。也就是说,包装器应该避免改变原始可执行文件的返回状态、标准输出和标准错误消息。

用户可以指定要封装哪个程序(具有类似shell的Glob),或者如果省略了,将应用于测试调用的所有程序的全局包装器。

这个特性是作为插件实现的,它将--wraper添加到Avocado运行命令中。

作为包装器以易懂的方式运行strace的示例：

```
#!/bin/sh
exec strace -ff -o $AVOCADO_TEST_LOGDIR/strace.log -- $@
```

让所有程序由test.py开始,用`~/bin/my-wrapper.sh`包装：

```
$ scripts/avocado run --wrapper ~/bin/my-wrapper.sh tests/test.py
```

只有我的`my-binary`文件用`~/bin/my-wrapper.sh`包装

```
$ scripts/avocado run --wrapper ~/bin/my-wrapper.sh:*my-binary tests/test.py
```

### 警示

* 不可能用GDB(–gdb-run-bin)进行调试,同时使用包装器(-包装器)。这两个选项是互斥的。
* 只能设置一个(全局)包装器。如果需要两个包装器中存在的功能,则必须将这些组合成单个包装器脚本。
* 只有使用`avocado.utils.process`(以及使用它的其他API模块:avocado.utils.build)运行的可执行文件)才会受到此特性的影响。

## [插件系统](https://avocado-framework.readthedocs.io/en/63.0/Plugins.html)
## [Utilities](https://avocado-framework.readthedocs.io/en/63.0/utils/index.html)
## [可选插件](https://avocado-framework.readthedocs.io/en/63.0/optional_plugins/index.html)
## [参考指南](https://avocado-framework.readthedocs.io/en/63.0/ReferenceGuide.html)
## [贡献与社区指南](https://avocado-framework.readthedocs.io/en/63.0/ContributionGuide.html)
## [Avocado发展要点](https://avocado-framework.readthedocs.io/en/63.0/DevelopmentTips.html)
## [释放avocado](https://avocado-framework.readthedocs.io/en/63.0/MaintenanceGuide.html)
## [其它资源](https://avocado-framework.readthedocs.io/en/63.0/OtherResources.html)
## [测试API文档](https://avocado-framework.readthedocs.io/en/63.0/api/test/avocado.html)

这是用户在编写测试时应该使用并且可以依赖的最小API集。

### `avocado.main`

`avocado.core.job.TestProgram`的别名

### `class avocado.Test(methodName='test', name=None, params=None, base_logdir=None, job=None, runner_queue=None)`

测试类的基本实现。

你将继承自己编写自己的测试。 通常,您需要在自己的测试中实现`setUp()`,`test*()`和`tearDown()`方法。

初始化测试。

参数：
* `methodName` - 要运行的主方法的名称。 为了与原始unittest类兼容,您不应该设置它。
* `name(avocado.core.test.TestID)` - 测试名称的漂亮名称。 对于使用AvocadoAPI编写的常规测试,不应设置此项。 这保留给内部Avocado使用,例如将随机可执行文件作为测试运行时。
* `base_logdir` - 测试日志应该到达的目录。 如果提供None,则使用`avocado.data_dir.create_job_logs_dir()`。
* `job` - 此测试所属的工作。

#### `basedir`
此测试(由文件支持)所在的目录

#### `cache_dirs`
返回配置文件中设置的缓存目录列表。

#### `cancel(message=None)`

取消测试。

期望从测试方法调用此方法,而不是其他任何地方,因为根据定义,我们只能取消当前正在执行的测试。 如果在测试方法之外调用此方法,avocado会将测试状态标记为ERROR,并指示您在错误消息中修复测试。

参数：message(str) - 将记录在日志中的可选消息

#### `error(message=None)`

使当前正在运行的测试状态为错误。

调用此方法后,将终止测试并将其状态设置为ERROR。

参数：message(str) - 将记录在日志中的可选消息

#### fail(message=None)

#### fail_class
#### fail_reason
#### fetch_asset(name,asset_hash = None,algorithm = None,locations = None,expire = None)

方法o调用utils.asset以获取和支持散列检查,缓存和多个位置的资产文件。

参数：
    name - 资产文件名或URL
    asset_hash - 资产哈希(可选)
    algorithm - 哈希算法(可选,默认为avocado.utils.asset.DEFAULT_HASH_ALGORITHM)
    locations - 可从中获取资产的URL列表(可选)
    expire  - 资产到期的时间
raise： EnvironmentError - 无法获取资产时
EnvironmentError - 无法获取资产时
返回：资产文件本地路径

#### filename
返回包含当前测试的文件(路径)的名称

#### get_state()
序列化表示测试状态的选定属性

返回：包含相关测试状态数据的字典
返回类型：字典

#### job
这项测试与之相关的工作

#### log
增强的测试日志

#### logdir
此测试的日志目录的路径

#### logfile
此测试的主要debug.log文件的路径

#### name
返回测试ID,其中包含测试名称

返回类型：TestID
#### outputdir
可用于测试编写者将文件附加到结果的目录

#### params
此测试的参数(AvocadoParam实例)

#### report_state()
将当前测试状态发送到测试运行程序进程

#### run_avocado()
包装run方法,用于在Avocado跑步者内执行。

结果：未使用的参数,与unittest.TestCase的兼容性。
#### runner_queue
测试和测试运行器之间的通信通道

#### running
此测试目前是否正在执行

#### set_runner_queue(runner_queue)
覆盖runner_queue

#### status
此测试的结果状态

#### teststmpdir
返回临时目录的路径,该路径对于给定作业中的所有测试保持不变。

#### time_elapsed = -1
测试执行的持续时间(总是从time_end - time_start重新计算

#### time_end = -1
(unix)测试完成的时间(可能会被迫测试)

#### time_start = -1
(unix)测试开始的时间(可以强制进行测试)

#### `timeout = None`
测试超时(params的超时优先)

#### `traceback`

#### `whiteboard=`

测试结束时将存储在`$logdir/whiteboard`位置的任意字符串。

#### `workdir`

此属性返回在整个测试执行期间存在的可写目录,但在测试完成后将清除该目录。

它可以用于解压缩源代码压缩包,构建软件等任务。

### avocado.fail_on(exceptions=None)

当装饰函数产生指定类型的异常时,测试失败。

(例如,我们的方法可能会在测试软件失败时引发IndexError。我们可以尝试/捕获它或使用此装饰器代替)

参数：exceptions - 假定为测试失败的元组或单个异常[Exception]
注意：self.error和self.cancel行为保持不变
注意：为了允许简单使用,参数“exception”不能是可调用的


### avocado.skip(message=None)

跳过测试装饰器

### avocado.skipIf(condition, message=None)

如果条件为True,装饰器将跳过测试。

### `avocado.skipUnless(condition, message=None)`

如果条件为False,装饰器将跳过测试。

### `exception avocado.TestError`

基础：avocado.core.exceptions.TestBaseException

表示测试未完全执行且发生错误。

如果测试部分执行并且由于设置,配置或其他致命情况而无法完成,则会出现这种异常。

`status ='ERROR'`

### exception avocado.TestFail
基础：avocado.core.exceptions.TestBaseException,exceptions.AssertionError

表示测试失败。

TestFail继承自AssertionError,以保持与vanilla python单元测试的兼容性(它们只考虑从AssertionError派生的失败)。

`status ='FAIL'`

### `exception avocado.TestCancel`

基础：avocado.core.exceptions.TestBaseException

表示测试已取消。

使用cancel()测试方法时应该抛出。

`status = 'CANCEL'`

## [Utilities APIs](https://avocado-framework.readthedocs.io/en/63.0/api/utils/avocado.utils.html)

这是一组实用程序API,Avocado为测试编写者提供了附加值。

它假设是通用的,没有任何Avocado知识,可以在不同的项目中重复使用。

> 在当前版本中,存在Avocado日志记录流的隐藏知识。 有关此问题的更多信息,请访问https://trello.com/c/4QyUgWsW/720-get-rid-of-avocado-test-loggers-from-avocado-utils

> 译者：此章节为翻译,详情请查看原文档

### Subpackages
### Submodules
### avocado.utils.archive module
### avocado.utils.asset module
### avocado.utils.astring module
### avocado.utils.aurl module
### avocado.utils.build module
### avocado.utils.cpu module
### avocado.utils.crypto module
### avocado.utils.data_factory module
### avocado.utils.data_structures module
### avocado.utils.debug module
### avocado.utils.disk module
### avocado.utils.download module
### avocado.utils.filelock module
### avocado.utils.gdb module
### avocado.utils.genio module
### avocado.utils.git module
### avocado.utils.disk module
### avocado.utils.distro module
### avocado.utils.download module
### avocado.utils.filelock module
### avocado.utils.gdb module
### avocado.utils.genio module
### avocado.utils.git module
### avocado.utils.iso9660 module
### avocado.utils.kernel module
### avocado.utils.linux_modules module
### avocado.utils.lv_utils module
### avocado.utils.memory module
### avocado.utils.multipath module
### avocado.utils.network module
### avocado.utils.output module
### avocado.utils.partition module
### avocado.utils.path module
### avocado.utils.pci module
### avocado.utils.process module
### avocado.utils.runtime module
### avocado.utils.script module
### avocado.utils.service module
### avocado.utils.software_manager module
### avocado.utils.stacktrace module
### avocado.utils.vmimage module
### avocado.utils.wait module
### Module contents

## [内部(核心)API](https://avocado-framework.readthedocs.io/en/63.0/api/core/avocado.core.html)

可能是Avocado 骇客感兴趣的内部API.

> 译者:此节未翻译,更多内容请查看原文档

## [扩展(插件)API](https://avocado-framework.readthedocs.io/en/63.0/api/plugins/avocado.plugins.html)

扩展API可能是插件编写者兴趣所在.

> 译者:此节未翻译,更多内容请查看原文档

## [可选插件API](https://avocado-framework.readthedocs.io/en/63.0/api/optional-plugins/index.html)

下面的页面记录了可选的Avocado插件的私有API。

* [avocado_glib package](avocado_glib/avocado_glib.html)
* [avocado_runner_docker package](avocado_runner_docker/avocado_runner_docker.html)
* [avocado_resultsdb package](avocado_resultsdb/avocado_resultsdb.html)
* [avocado_varianter_yaml_to_mux package](avocado_varianter_yaml_to_mux/avocado_varianter_yaml_to_mux.html)
* [avocado_result_upload package](avocado_result_upload/avocado_result_upload.html)
* [avocado_runner_remote package](avocado_runner_remote/avocado_runner_remote.html)
* [avocado_robot package](avocado_robot/avocado_robot.html)
* [avocado_loader_yaml package](avocado_loader_yaml/avocado_loader_yaml.html)
* [avocado_varianter_pict package](avocado_varianter_pict/avocado_varianter_pict.html)
* [avocado_golang package](avocado_golang/avocado_golang.html)

## [发行说明](https://avocado-framework.readthedocs.io/en/63.0/release_notes/index.html)

> 译者:此节未翻译,更多内容请查看原文档

## [征求意见稿(RFCS)](https://avocado-framework.readthedocs.io/en/63.0/rfcs/index.html)

> 译者:此节未翻译,更多内容请查看原文档

## 原文档

[原文档](https://avocado-framework.readthedocs.io/en/63.0/Introduction.html)