import json as js

# emp = {"Eid":101, 'name':'John', "salary":12000}
# print(emp)
# print(type(emp))

# jsdata = js.dumps(emp)
# print(jsdata)
# print(type(jsdata))
#
# # jsd = str(emp)
# # print(jsd)
# # print(type(jsd))

# dictdata = js.loads(jsdata)                 # str to dict
# print(dictdata)
# print(type(dictdata))

"""================================--------------------================================"""

import requests as rq
# check github (session17a)

"""================================--------------------================================"""

import re

# qe = "hello hi hey hi "
# result = re.match("hello",qe)
# res = re.findall("hey",qe)
# resu = re.search("hi",qe)
# resul = re.split("e", qe)
# r = re.sub("hey", "hello", qe)
# print(r)
# print(resu)
# print(resul)
# print(res)
# print(result)
# print(type(result))

quote = "Work Hard And Get Luckier"
data = re.findall(".",quote)
print(data)

data = re.findall("\w",quote)
print(data)

data = re.findall("\w*",quote)
print(data)

data = re.findall("\w+",quote)
print(data)

# assignment using regex
# validate vehicle number

"""<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>"""

