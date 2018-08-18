url_1 = '![x](https://cdn.sspai.com/minja/2018-07-24-%E5%BF%AB%E8%B4%B4.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)'
url_2 = '![x](https://cdn.sspai.com/minja/2018-07-24-%E5%BF%AB%E8%B4%B4.jpg)'

import re

matched = re.compile(r'!\[(.*?)\]\((http.*?)\)').match(url_2)
# 处理查询： ![x](https://cdn.sspai.com/minja/2018.jpg?imageView1)'
if re.search(r'\?',url_1):
    image_url = matched.group(2).split('?')[0]
else:
    image_url = matched.group(2)
self.image_type = image_url.split('.')[-1]

print(image_url,image_type)