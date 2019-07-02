#coding:utf-8
import  numpy as np
arr1=np.arange(1,10).reshape((3,3))
arr2=np.ones((9,)).reshape((3,3))

# print(arr1)
# print("-"*30)
# print(arr2)
# print("-"*30)
# print(np.hstack((arr1,arr2)))
# print(np.vstack((arr1,arr2))) #vstack 不支持一个空矩阵和另外一个矩阵合并
# print(np.concatenate((arr1,arr2))) #在一维的情况 concatenate == hstack,在多维情况下concatenate ==vstack

#切割
arr3 =np.concatenate((arr1,arr2))
print(np.hsplit(arr3,3)) # ssplit 均等切割

