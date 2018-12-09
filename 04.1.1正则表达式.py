#-*- coding:utf-8 -*-

import re
'''
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
(如果一个正则表达式要重复使用几千次，可以先预编译，再重复使用。)
用编译后的正则表达式去匹配字符串。
'''
print("=======正则表达式：匹配字符串========")
'''
匹配邮箱地址的格式：
1.必须是字母、数字、下划线的组合
2.长度最少3位，最长10位
3.后缀是@+小写字母+.com/.cn/.net的格式
'''
exp=r'^[0-9+a-zA-Z+_+]{3,10}@[a-z]+(.com|.cn|.net)$'
myEmail = "t1_@live.cn"
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
result = re.match(exp,myEmail)
#预编译
#compileResult = re.compile(exp)
#result = compileResult.match(myEmail)
print("match result: ",result)
if result:
    print("Match!")
else:
    print("unMatch!")

print("=========利用正则表达式 切分字符串=============")
# 不清楚b，c之间有多少空格
str="ab    c"
r = re.split(r"\s+",str)
print(r)
# 切分的标准比较复杂
str="a,b, ;c  d"
r = re.split(r"[\s,;]+",str)
print(r)

print("============利用正则表达式，分组并提取子串===========")
r = re.match(r"^([0-9]{3})-([0-9]{8})","010-53296156")
print("整个字符串：",r.group(0))
print("字符串所有分组：",r.groups())
print("第一部分：",r.group(1))
print("第二部分：",r.group(2))