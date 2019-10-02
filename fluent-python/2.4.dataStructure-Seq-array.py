#-*- coding:utf-8 -*-
from array import array
from random import random
'''
@file: 2.4.dataStructire-Seq-array.py
@description:
数组。
【创建数组】
1.创建数组：Python 数组跟 C 语言数组一样精简。
创建数组需要一个类型码type code，用来表示在底层的 C 语言应该存放怎样的数据类型。
'''

#创建1000万个随机浮点数的数组
arr1 = array('d',(random() for i in range(10**3)))
print(arr1[-1])
#将数组写入二进制文件
#1.浮点数写入二进制文件，速度更快，占用的字节空间也要比文本文件小。
bin_file = open('floatnum.bin','wb')
arr1.tofile(bin_file)
bin_file.close()
#从二进制文件中读出数据，放入数组.
#2.从二进制文件中读浮点数据要比从文本文件中快，
# 因为后者会使用内置的 float 方法把每一行文字转换成浮点数。
bin_file = open('floatnum.bin','rb')
arr2 = array('d')
arr2.fromfile(bin_file,10**3)
bin_file.close()
#验证读出的数据和原始数据是否一致
print(arr2[-1])
