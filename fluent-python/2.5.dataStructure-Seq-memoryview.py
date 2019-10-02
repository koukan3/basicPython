#-*- coding:utf-8 -*-
from array import array
'''
@file: 2.5.dataStructure-Seq-memoryview.py
@description:
内存视图。
内存视图其实是泛化和去数学化的 NumPy 数组；
可以在不需要复制内容的前提下，在数据结构之间共享内存。
内存视图中的数据结构可以是任何形式。
【创建内存视图】
'''

nums = array('h',[-2,-1,0,1,2])
memv = memoryview(nums)
print(len(memv))
print(memv[0])
#改变视图
memv[0]=10
print(nums)
# memoryview.cast 会把同一块内存里的内容打包成一个全新的 memoryview 对象。
memv_cast = memv.cast('B')
print(len(memv_cast))
print("memv_cast:",memv_cast.tolist())
print("改变memv_cast前：",nums)
memv_cast[5]=4
print("改变memv_cast后：",nums)