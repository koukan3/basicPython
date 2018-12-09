# -*- coding:utf-8 -*-

import pickle,json

#序列化：将内存中的数据存入磁盘或进行传输
print("=========将任意对象序列化成byte字节=========")
d = dict(a="第一",b=2)
pbytes = pickle.dumps(d)
print("序列化后的字节：",pbytes)

print("==========将对象序列化后写入一个file-like object=======")
#f = open(r"e:/dump.txt","wb")
#pickle.dump(d,f)
#f.close()
# 以上等价于：
'''
f = open(r"E:/dumpfile","wb")
f.write(pbytes)
f.close()
'''
print("==========反序列化，读取字节信息===========")
load1 = pickle.loads(pbytes)
print("反序列化1: ",load1)
'''
f = open(r"e:/dump.txt","rb")
load2 = pickle.load(f)
f.close()
print("反序列化2：",load2)
'''
print("===========序列化:JSON格式字符串==============")
d = {"a":"第一","b":2}
#json1类型为 str
json1 = json.dumps(d,ensure_ascii=False)
print("将python对象序列化成JSON字符串： ",json1,type(json1))
'''
# 将 json写入 file-like object
f = open(r"e:/jsondump.txt","w")
json.dump(d,f)
f.close()
'''
print("======反序列化：读取JSON格式的内容，转成python对象=========")
# obj1 的类型是 dict
obj1 = json.loads(json1)
print("json反序列化成python对象1：",obj1,type(obj1))
'''
f = open(r"e:/jsondump.txt","r")
# obj2 的类型是 dict
obj2 = json.load(f)
print("json反序列化成python对象2：",obj2,type(obj2))
f.close()
'''

