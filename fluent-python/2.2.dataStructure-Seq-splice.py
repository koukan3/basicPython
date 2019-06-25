#-*- coding:utf-8 -*-
'''
@file: 2.2.dataStructure-Seq-splice.py
@description: 切片，python中切片的位置是左闭右开。
左闭右开的好处：
1.有一个位置信息时，可以直接看出切片区间中的元素个数。如：range(6)有6个元素。
2.有两个位置信息时，方便计算出切片区间的长度(stop-start)。如 list[1:6]长度为5.
3.方便把序列分成不重叠的两部分。如 list[:n]和 list[n:]
多维切片：
[] 运算符里还可以使用以逗号分开的多个索引或者是切片，外部库 NumPy 里就用到了这个特性。
【切片对象，多维切片，切片赋值】
'''

str = "bicycle"
print(str[:3])
print(str[::3]) # 以3为间隔取。str[a:b:c]表示在a和b之间以c为间隔取值。
# a:b:c 这种用法只能作为索引或者下标用在 [] 中来返回一个切片对象。
print(str[::-1]) #倒着取值，相当于逆序输出。
print(str[::-5]) #间隔是负数时，第一个输出的都是原本的最后一个。
print(str[2:None]) # 截取到最后一个
print(str[None:]) #从第一个开始截取
print("========== 切片对象 slice ：有名字的切片=========")
invoice = "1909  abc $17.50 3 $52.50"
SKU = slice(0,6)
DESC = slice(6,9)
PRICE = slice(9,16)
print(invoice[SKU],invoice[DESC],invoice[PRICE])
print("========== 切片赋值:占据指定区间的位置。 ==========")
mylist = list(range(10))
print(mylist)
mylist[2:4]=[100,100,100]  #赋值等式的右侧必须是可迭代对象。
print("赋值之后：",mylist)
del mylist[2:5]
print("删除指定区间后：",mylist)

