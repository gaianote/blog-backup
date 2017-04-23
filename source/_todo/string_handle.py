import re
# 1.获得pattern对象，pattern = re.compile('正则表达式')
#pattern = re.compile('^\d{0,2}')
# 2.使用re方法获得所需内容
#pattern.split('one1two2three3four4')

# 删除所有的符号
def trim(string):
  pattern = re.compile('《|》|,|\.|\s*|\?|“|”|‘|’|\(|\)|（|）|，|。|\"|\'')
  return ''.join(pattern.split(string))
input()
