
'''
@file: 2.3.dataStructure-Seq-sort.py
@description: 序列--排序
【sort就地排序，sorted新建对象排序】
'''

'''
list.sort是就地排序，返回值为None。
'''
list = ['jack','andy','lily','sam','bob']
print("before sort: ", id(list))  #2191212059784
print(list.sort())
print(list)
print("after sort: ",id(list)) #2191212059784
'''
sorted可以对任何可迭代对象排序，返回一个新建的列表。
'''
str='asdji'
print("before sorted: ", id(str))
result = sorted(str)
print("返回的是新建的列表：",result)
print("原本的序列不变： ",str)
print("after sorted: ", id(result))


