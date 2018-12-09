# -*- coding:utf-8 -*-

from enum import Enum,unique

# 枚举类，每个常量都是枚举类的一个唯一实例
print("=============枚举类：写法1============")
Month1 = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

'''
for x in Month._member_map_: 打印枚举类中的常量
for x in Month._member_map_.items(): 打印枚举类中实例信息tuple（实例名，实例）
for x in Month._member_names_: 打印枚举类中的常量
for x in Month._value2member_map_: 打印枚举类中的常量的计数，从1开始。
'''
items = Month1._member_map_.items()
amap = Month1._member_map_    #Jan <class 'str'>
names = Month1._member_names_ #Jan <class 'str'>
for k,v in items:
    # Jan(<class 'str'>) , Month.Jan(<enum 'Month'>) , 1
    if v.value <4:
        print("%s(%s) , %s(%s) , %s"%(k,type(k),v,type(v),v.value))
# Month.Feb打印:        Month.Feb    2       Feb
print("Month.Feb打印: ",Month1.Feb, Month1.Feb.value, Month1.Feb.name)
# 按value取枚举类实例：   Month.Mar
print("按value取枚举类实例：",Month1(3))

print("=============枚举类：写法2============")

# unique 检查没有重复值。
# 有重复值就报错：ValueError: duplicate values found in <enum 'Days'>:
@unique
class Days(Enum):
    Mon=10
    Tue=20
    Wed=3
    Thu=4
    Fri=5
items = Days.__members__.items()
for name,ins in items:
    print(name,ins.value)

#按value取枚举类实例： Days.Tue
print("按value取枚举类实例：",Days(20))