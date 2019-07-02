#coding:utf-8
import numpy as np
from collections import Iterable

print("==============迭代索引和元素===========")
for i,e in enumerate([10,20,30,"tom"]):
    print("i=%s e=%s"%(i,e))
list1 = [(1,2,3),(4,5,6)]
print("isinstance of Interable: ",isinstance(list1,Iterable))
for a,b,c in list1:
    print("a=",a,"b=",b,"c=",c)
arr=np.random.randint(1,10,20).reshape((4,5))

#根据索引遍历
for i in range(0,arr.shape[0]):
    for j in range(0,arr.shape[1]):
        print(arr[i][j],end=' ')
    print()
print("-"*30)
print(np.where(arr>5,arr,0))
# print(arr[2:,:]) # 后两行
# print(arr[[0,3]]) # 第1,4行
# print(arr[[0,3],-2:]) #第1,4行 的后两列
# print(arr[:2,:2]) # 前两行的前两列 ,在一个大中括号中如果存在，,左边是行的切片，右边是列的切片

#条件推导式
base_list1=[True,True,False,False] # [1,1,0,0]
base_list2=[True,False,True,False]

# list1=[ (1 if base_list1[i]&base_list2[i] else 0) for i in range(len(base_list1)) ]
# print(list1)

arr1 =np.array(base_list1)
arr2 =np.array(base_list2)

result=np.where(arr1&arr2,1,np.where(arr1,-1,np.where(arr2,-2,0)))
print(result)