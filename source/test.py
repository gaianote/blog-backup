def dic_to_str(dic,split = ','):
    list_ = []
    split = ' {} '.format(split)
    for key,value in dic.items():
        value = "'{}'".format(value.replace("'","''")) if isinstance(value,str) else str(value)
        list_.append(key + " = " + value)
    return split.join(list_)
def _select(self,tablename,*keys,where = '',**kw):
    headers = ','.join(keys)
    # kw存在的时候省略where：fetchone('table','id',name = 'lee')
    if kw:
        where = dic_to_str(kw,'AND')
        sql ="SELECT {0} FROM {1} WHERE {2}".format(headers,tablename,where)
    elif not where:
        sql = "SELECT {0} from {1}".format(headers,tablename)
    else:
        # 处理字符串内的单引号
        base_str = re.compile(r"'(.*?)'(?: AND|$)").findall(where)
        for str_ in base_str:
            where = where.replace(str_,str_.replace("'","''"))
        sql = "SELECT {0} from {1} WHERE {2}".format(headers,tablename,where)
        import os
        from lib.config import DATA_PATH
        with open(os.path.join(DATA_PATH,'text.text'),'w') as f:
            f.write(sql)

    print(sql)
_select('a','d','c',id= 100,page = 'x',nice = "'fdfdf{}kw'")
