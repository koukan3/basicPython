#coding:utf-8
import numpy as np

arr1=np.random.randint(0,10,9).reshape((3,3))
# print(arr1)
# print(arr1.sum())
# print(arr1.sum(1)) #sum(数字) ,代表轴，
# print((arr1>5).sum()) # 几个大于5数字
arr2=np.arange(0,12).reshape((3,4))

# print(np.dot(arr1,arr2)) # 矩阵相乘

print(arr1)
print(arr1.T)#矩阵转置
# np.dot(arr2,arr2.T)
print(arr1+arr1.T) # 维度相同才能+ ,- ,* ,/

arr3=np.linalg.inv(arr1) # 逆矩阵 ,arr1 和 arr3 互为逆矩阵
# print(arr3)


