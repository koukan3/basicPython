#-*- coding:utf-8 -*-

'这是该模块的文档注释'

__author__="Terry Gao"

import sys
#导入sys模块，就有sys变量指向该模块，利用这个变量可以访问sys模块的所有功能。

print("__name__:",__name__)
print("获取文档注释：",__doc__)
#private 变量，不应该被直接引用
__pr1 = "this is private parameter 1"
_pr2 = "this is private parameter 2"
#private 函数，不应该被直接引用
def __test():
    print("this is a private function")
# 普通函数
def test2():
    __test()
#普通函数
def test():
    #sys.argv存储了命令行中的所有参数。
    paramsList = sys.argv
    #sys.argv至少有一个元素，即该.py文件的名称
    if len(paramsList)==1:
        print("only one parameter：%s"%paramsList[0])
    elif len(paramsList)==2:
        print("parameters: %s , %s"%(paramsList[0],paramsList[1]))
    else:
        print("more than two parameters!")

'''
该.py文件在命令行下执行时，python解释器会把__name__置为__main__。
如果在其他地方导入该文件，则不会置为__main__， 如交互方式中，被置为该模块文件的名字。
'''
if __name__=="__main__":
    test()
