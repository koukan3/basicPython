# coding=utf-8

import os

# os模块可以直接调用操作系统提供的接口函数

pathModule = os.path
currentPath = pathModule.abspath('.')
print("当前路径path：",currentPath)
print("环境变量（指定获取某个环境变量）：", os.environ.get('JAVA_HOME'))
print("拼接路径：",os.path.join("a/b","c.txt"))
print("拆分路径：",os.path.split(currentPath))
print("拆分路径，得到文件拓展名：",os.path.splitext(currentPath))
#print("创建目录：",os.mkdir("E:/gaohan/"))
#print("创建目录：",os.rename("E:/gaohan","E:/gh"))
#print("删除目录：",os.rmdir("e:/gh"))

print("=======列出当前目录下的所有目录==========")
list = [x for x in os.listdir(".") if os.path.isdir(x)]
print(list)
print("=======列出当前目录下的所有py文件==========")
list = [x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(list[-5:])
