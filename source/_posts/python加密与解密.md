title: python字符串加密与解密
author: 李云鹏
tags: []
categories: []
date: 2018-09-13 06:22:00
---
对于字符串加密与解密来说，PyCrypto这个库应该是python密码学方面最出名第三库了，但是它几经很久没有维护了，python3.6以上版本会安装失败，现在的解决方案是使用[cryptography](https://github.com/pyca/cryptography)

<!--more-->

## 官方示例

```python
>>> from cryptography.fernet import Fernet
>>> # Put this somewhere safe!
>>> key = Fernet.generate_key()
>>> key
>>> b'YDDzLAdujn-QYxq5tjnTrU9MOPiHCJ6tU9MgkQ0BS1E='
>>> f = Fernet(key)
>>> token = f.encrypt(b"A really secret message. Not for prying eyes.")
>>> token
'...'
>>> f.decrypt(token)
'A really secret message. Not for prying eyes.'
```

1. 导入包Fernet
2. 实例化Fernet需要唯一的参数key,这个参数要求有点高，不是随便一个字节序列就行，要求32位 + url-safe + base64-encoded 的bytes类型。为了方便，Fernet类内置了生成key的类方法: generate_key()，作为加密解密的钥匙，生成的key你要保存好，以供解密的时候使用
3. 实例化一个Fernet对象。
4. 接下来就是加密方法: fernet.encrypt(data) 接受一个bytes类型的数据，返回一个加密后的bytes类型数据(人类看不懂)，俗称 token-Fernet。
5. 解密fernet.decrypt(token)

## 使用实例

```python
from cryptography.fernet import Fernet

class Crypto(object):
    """docstring for ClassName"""
    def __init__(self, key):
        self.factory = Fernet(key)
    def generate_key(self):
        key = Fernet.generate_key()
        print(key)
    # 加密
    def encrypt(self,string):
        token = self.factory.encrypt(string.encode('utf-8'))
        return token
    # 解密
    def decrypt(self,token):
        string = self.factory.decrypt(token).decode('utf-8')
        return string

# 密钥，需要保存好
key = b'GqycX8dOsZThS25NRI7hwCJw3JcKebj8NnXfVvqRHSc='
crypto = Crypto(key)

if __name__ == '__main__':
    # 加密字符串
    token = crypto.encrypt('A really secret message. Not for prying eyes.')
    print(token)
    # 解密字符串
    string = crypto.decrypt(token)
    print(string)

```
