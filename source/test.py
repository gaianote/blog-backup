str_ = """简直完美,a = "1,2 ",b,hah,"c,2",c=5,e = 'a =c  ',15,简直完美,dlll"""
import re
from collections import namedtuple

def res_param(str_):
    KEY = r'(?P<KEY>[a-zA-Z_][a-zA-Z_0-9]*(?:\s.*?=|=))'
    STR = r"""(?P<STR>".*?"|'.*?')"""
    WS = r'(?P<WS>\s+)'
    NUM = r'(?P<NUM>\d+)'
    SPLIT = r'(?P<SPLIT>,)'
    VALUE = r'(?P<VALUE>\S+?(?=,|$))'
    master_pat = re.compile('|'.join([KEY,STR,SPLIT,NUM,WS,VALUE]))

    def generate_tokens(pat, text):
        Token = namedtuple('Token', ['type', 'value'])
        scanner = pat.scanner(text)
        for m in iter(scanner.match, None):
            yield Token(m.lastgroup, m.group())
    result = ''
    for tok in generate_tokens(master_pat, str_):
        print(tok)
        if tok.type == 'VALUE':
            result += '"'+ tok.value + '"'
        else:
            result += tok.value
    return result

res_param(str_)
# for s in scanner:
#     print(s)

# re.compile('|'.join())
# def res_param(str_):
#     list_ = str_.split(",")
#     new_list = []
#     for i in range(len(list_)):
#         if list_[i].startswith('"') or list_[i].startswith("'"):
#             pass
#         elif list_[i].endswith('"') or list_[i].endswith("'"):
#             new_list.append(list_[i-1] + ',' + list_[i])
#         else:
#             new_list.append(list_[i])

#     return list_,new_list

# print(res_param(str_))