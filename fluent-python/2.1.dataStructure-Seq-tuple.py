#-*- coding:utf-8 -*-
from collections import namedtuple
'''
@file: 2.1.dataStructure-Seq-tuple.py
@description:序列-元组。元组是对数据的记录（包括数据的位置信息）。
【拆包，具名元组,序列拼接】
'''

provinces = [('上海','沪'),('重庆','渝'),('湖北','鄂')]
for pro in provinces:
    print(pro)
    print("%s/%s"%pro)
print("========元组的拆包 unpacking============")
# 拆包中某个元素没什么用处时，可以用_代替。
for pro,_ in provinces:
    print(pro)
    #print(_)
city,population,year = ('beijing',2300,2019) #拆包后，平行赋值
print(city,population,year)

class City:
    def __init__(self,name,code):
        self.name=name
        self.code=code
t = ("北京",1001)
#拆包，作为参数
c = City(*t)
print(c.name,c.code)
a,b,*rest,d=range(6)
print("a=%r,b=%r,rest=%r,d=%r"%(a,b,rest,d))
print("=========具名元组 namedtuple=========")
#country = namedtuple("Country","name square capital location") #空格隔开的字符串
#country = namedtuple("Country",["name","square","capital","location"]) #可迭代对象list
country = namedtuple("Country",("name","square","capital","location")) #可迭代对象tuple
c = country("China",960,"Beijing",(120.101,34.501))
print("name=%s,square=%r,capital=%s"%(c.name,c.square,c[2]))
print("longitude=%r,latitude=%r"%(c.location[0],c.location[1]))
Japan=("Japan",120,"Tokyo",(124.33,44.33))
jp = country._make(Japan) #等同于country(*Japan)
print(jp)
print(jp._fields)
print(jp._asdict())
for k,v in jp._asdict().items():
    print("k=%s,v=%s"%(k,v))
print("========序列的拼接：+ 和 * ========")
#序列的拼接：不改变操作对象，而是重新构建了一个新的序列。
t=(3,4)
concated = t+t
print("concated: ",concated)
concated = t*2
print("concated: ",concated)

