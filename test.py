import re
line = '![img](http://wiki.jikexueyuan.com/project/learn-road-qt/images/31.png)'
matched = re.compile(r'!\[(.*?)\]\(http:.*?(\.png)\)').match(line)
if matched:
    print(line)
    print(matched.group(1),matched.group(2))