#coding:utf-8
import numpy as np

# 创建一个矩阵
# list1=[1,2,3,4,5,6]
list1=[[11,11,11],[22,22,22],[3,3,3]]
list1=[[[11,11],[22,22]],[[33,33],[44,44]]]
# arr = np.array(list1)
# print(arr.shape) # (6,) ,元组来描述维度：1、轴的个数，2、每个轴的长度
# print(arr.ndim) # 秩
# print(arr.dtype)
# print(arr.size)


#第二种
arr=np.arange(0,20).reshape((4,5)) # reshape函数的形参传一个维度,改变维度，size是不能变
arr=np.random.randint(1,10,25).reshape((5,5))
arr=np.random.randn(10) # 生成一个以0为原点 正态分布数列
#

#第三种
arr=np.zeros((3,3,3))
arr=np.ones((3,3,3))
arr=np.empty((3,3,3))
print(arr)