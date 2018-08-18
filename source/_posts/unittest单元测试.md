---
title: unittest单元测试
date: 2018-05-29 17:44:14
tags: python
---

## 一个简单的测试

```python
import unittest

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

if __name__ == '__main__':
    unittest.main()
```

这就是一个简单的测试，有几点需要说明的：

1. 在第一行给出了每一个用例执行的结果的标识，成功是 .，失败是 F，出错是 E，跳过是S。从上面也可以看出，测试的执行跟方法的顺序没有关系，test_divide写在了第4个，但是却是第2个执行的。

2. 每个测试方法均以 test 开头，否则是不被unittest识别的。

3. 在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果

## 用例顺序

### 人为指定用例顺序

```python
import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
```
https://blog.csdn.net/huilan_same/article/details/52944782

### 默认顺序

使用addTest的方法比较繁琐，而sunittest的默认顺序是按照文件名进行排序的，因此在实际使用过程中，可以数字作为序号的方式进行命名，从而达到排序的目的

```python
import unittest

class TestMathFunc(unittest.TestCase):

    def test_1_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_2_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_3_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_4_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))
```
## setup与teardown

### 执行每条测试用例前调用一次

当类里面定义了 `setUp()` 方法的时候，测试程序会在执行每条测试项前先调
用此方法；同样地，在全部测试项执行完毕后，`tearDown()` 方法也会被调用。

```python
import unittest

class simple_test(unittest.TestCase):
    def setUp(self):
        self.foo = list(range(10))

    def test_1st(self): # 这里调用一次setUp
        self.assertEqual(self.foo.pop(),9)

    def test_2nd(self): # 这里又调用一次setUp
        self.assertEqual(self.foo.pop(),9)

if __name__ == '__main__':
    unittest.main()
```

### 一个类全程只调用一次 setUp/tearDown

那如果我们想全程只调用一次 setUp/tearDown 该怎么办呢？就是用 `setUpClass()` 和 `tearDownClass()` 类方法。注意使用这两个方法的时候一定要用 @classmethod 装饰器装饰起来：

```python
import unittest

class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.foo = list(range(10))

    def test_1st(self):
        self.assertEqual(self.foo.pop(),9)

    def test_2nd(self):
        self.assertEqual(self.foo.pop(),8)

if __name__ == '__main__':
    unittest.main()
```

### 整个文件级别上只调用一次 setUp/tearDown

整个文件级别上只调用一次 setUp/tearDown，这时候就要用 `setUpModule()` 和 `tearDownModule()` 这两个函数了，注意是函数，与 TestCase 类同级：

```python
import unittest

def setUpModule():
    pass

class simple_test(unittest.TestCase):
    ...
```

## unittest断言

### 断言使用示例

```python
class demoTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4 + 5,9)
```

### 常用断言

|断言语法                | 解释                |
|-----------------------|---------------------|
|assertEqual(a, b)      | 判断a==b            |
|assertNotEqual(a, b)   |  判断a！=b          |
|assertTrue(x)          | bool(x) is True     |
|assertFalse(x)         |bool(x) is False     |
|assertIs(a, b)         | a is b              |
|assertIsNot(a, b)      |  a is not b         |
|assertIsNone(x)        | x is None           |
|assertIsNotNone(x)     |  x is not None      |