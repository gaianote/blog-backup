## 使用flask

1. 创建应用，类型选择python-web
2. 添加依赖，项目里新增requirements.txt文件

```requirements
flask
```

3. 修改app.conf 修改 url：/ 为 url：/.*
4. 创建flask代码,直接从bae的文档上找到示例，更新index.py

```python
from flask import Flask, g, request

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
    return "Hello, world! - Flask\n"

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
```
