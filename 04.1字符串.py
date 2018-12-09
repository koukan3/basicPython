#! /usr/bin/python
#coding:utf-8
#转义  \  r''表示''中的内容不转义
print("==========转义=========")
print("转义1：",'\\\t\\')
print("转义2：",r"\\\t\\")
print("转义3：",r'\\\t\\')
print("==========换行=========")
print("换行1：","line1\nline2\nline3")
print("换行2：",'''line1
line2
line3''')
print("======None========")
print("None: ",None)
print("======编码======")
print("字符串对应若干字节：",'abc')
print("bytes类型：",b'abc')
print("abc".encode('ascii'))
print("abc".encode('utf-8'))
print("decode: ",b'abc'.decode("utf-8"))
print("中".encode('utf-8')) #中：\u4e2d
print("decode: ",b'\xe4\xb8\xad'.decode("utf-8"))
print("==========字符串中的格式化==========")
print("字符串%s的格式化..."%'abc')
print("整数%d和%d的格式化..."%(123,456))
print("整数%5d和%05d的格式化..."%(123,456))
print("浮点数%f和%.3f的格式化..."%(3.1415972,3.14159))
print("十六进制整数%x和%x的格式化..."%(11,17))
print("%%s会把任意类型转成字符串，例如：%s"%True)
print("{0}的成绩提高了{1:.2f}%".format("xiaoming",17.123))
#切片(subString)
print(str1[0:3])
print(str1[-3:])
print(str1[-1:-4:-1])
print(str1[:-4:-1])
# 字符串的反转
print(str1[::-1])

# print("-"*50)
# print("北京尚学堂".center(50))
# print("-"*50)


