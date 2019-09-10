import re
# 1.获得pattern对象，pattern = re.compile('正则表达式')
pattern = re.compile('^\d{0,2}')
# 2.使用re方法获得所需内容
pattern.split('one1two2three3four4')
input()
# 删除所有的符号
def trim(string):
  pattern = re.compile('《|》|,|.|?|“|”|‘|’(|)|（|）|，|。|\"|\'')
  return ''.join(pattern.split(string))
print(trim('adfd,d.d/dd.。。。'))
input()
