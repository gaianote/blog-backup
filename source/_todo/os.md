## 列出文件

列出当前目录所有的文件夹
[x for x in os.listdir('.')  if os.path.isdir(x)]
列出当前目录所有的文件
[x for x in os.listdir('.')  if os.path.isdfile(x)]
列出当前目录指定格式的文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']