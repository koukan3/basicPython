#-*- coding:utf-8 -*-
'''
@file: 2.0.dataStructure-Seq-list.py.py
@description: 序列（分为容器序列、扁平序列、可变序列、不可变序列）--列表
列表：list
【列表推导，表达式生成器，序列拼接】
'''

#列表推导：list comprehension.
#列表推导只用来创建新的列表。
symbols = "@#&%"
list1 = [ord(str) for str in symbols]
print(list1)
list2 = [ord(str) for str in symbols if ord(str)>35]  #listcomps实现过滤filter效果。
print(list2)

colors=["black","white"]
sizes=["S","M","L"]
#列表推导
clothes = [(c,s) for c in colors for s in sizes]
print(clothes)
#生成器表达式：generator expression  #generator object
#生成器表达式每次在for循环时才生成一个组合，逐个产生元素，不会像列表推导一样对内存造成压力。
generatorObj = ((c,s) for c in colors for s in sizes)
# for cloth in generatorObj:
#     print(cloth)
clothes = [cloth for cloth in generatorObj]
print(clothes)
print("========序列的拼接：+ 和 * ========")
#序列的拼接：不改变操作对象，而是重新构建了一个新的序列。
list1=[3,4]
concated=list1+list1
print("concated: ",concated)
concated=2*list1
print("concated: ",concated)
list2=[["x"]]*3  #里面的列表指向同一个引用
print(list2)
list2[0][0]="y"
print(list2)
list2=[["x"] for i in range(3)] #里面的列表指向不同的引用
print(list2)
list2[0][0]="y"
print(list2)



