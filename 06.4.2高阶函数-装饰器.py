# -*- coding:utf-8 -*-
import time

#Decorator:在代码运行过程中动态增加功能的方式，本质是一个高阶函数（返回值为函数）
#装饰器不改变被装饰对象本身的功能，只是锦上添花。
print("==============1.高阶函数：装饰器 decorator===============")
def log(func):
    def wrapper(*param1,**param2):
      print("call function %s()" % (func.__name__))
      return func(*param1,**param2)
    return wrapper
print("Decorator1 >>>>")
@log
def getDate():
    print("-- %s --"%(time.strftime("%Y.%m.%d %H:%M:%S",time.localtime(time.time()))))
print("函数名：",getDate.__name__)
getDate()
print("等价于 Decorator2 >>>>")
def getDate2():
    print("-- %s --"%(time.strftime("%Y.%m.%d %H:%M:%S",time.localtime(time.time()))))
print("函数名：",getDate2.__name__)
getDate2 = log(getDate2)
getDate2()

print("==============2.高阶函数：有参数的装饰器 decorator===============")
def log2(text):
    def decorator(func):
        def wrapper(*param1,**param2):
            print("%s, call Function: %s()"%(text,func.__name__))
            return func(*param1,**param2)
        return wrapper
    return decorator

print("Decorator3 >>>>")
@log2("this is a decorator with parameters")
def getDate3():
    print("-- %s --"%(time.strftime("%Y.%m.%d %H:%M:%S",time.localtime(time.time()))))
getDate3()

print("等价于 Decorator4 >>>>")
def getDate4():
    print("-- %s --"%(time.strftime("%Y.%m.%d %H:%M:%S",time.localtime(time.time()))))
getDate4 = log2("this is a decorator with parameters")(getDate4)
getDate4()