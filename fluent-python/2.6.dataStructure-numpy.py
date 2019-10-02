#-*- coding:utf-8 -*-
import numpy as np
from time import perf_counter as pc
'''
@file: 2.6.dataStructure-numpy.py
@description:
高阶数组、矩阵操作：numpy,scipy
【内存映射】
'''

a = np.arange(12)
print("ndarray: ",a)  #(12,0)
print(a.shape)
a.shape = 4,3
#读取任意行、列
print(a)
print(a[2,2])
print(a[:,1])
print(a[2,:])
#转置
a = a.transpose()
print(a)
nums = np.array(range(10**7),"float32")
#精度和性能较高的计时器
print("最后3个数：",nums[-3:])
#调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。
#当第二次调用时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。
#两个函数取差，即实现从时间点B1到B2的计时功能。
t0 = pc()
nums /= 3
t1=pc()
print("1000万运算耗时:",t1-t0)
print("运算后的最后3个数：",nums[-3:])
#保存数组
#np.save("ndarray_file",nums)
load_result  = np.load("ndarray_file.npy","r+")
#np.load使用了内存映射，只访问大文件的一小部分，而不是全部读取到内存中。
print("加载之后的最后3个数：",load_result[-3:])
