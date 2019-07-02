#coding=utf-8
from collections import Iterable,Iterator
from functools import reduce
import sys
import time
'''
高阶函数：变量可以指向函数，函数名本质是执行函数的一个变量；
将函数作为参数传入另一个函数，这样的函数是高阶函数
'''

print("==================高阶函数：map(function,Iterable)===========")
r = map(str,[1,2,3,4,5])
print("map结果是否是Iterator：",isinstance(r,Iterator))  # true
print("应用str函数之后的结果：",list(r))
flag = isinstance(r,Iterable)
print("map()的结果是否可迭代:",flag)  # true
if flag:
    for s in r:
        print(s)

#输出首字母大写的名字
names = ['adam', 'LISA', 'barT']
def initUpper(word):
    sword = str(word)
    return sword[0].upper()+sword[1:].lower()
namesResult = map(initUpper,names)
for n in namesResult:
    print(n)
print("==================高阶函数：reduce(function,Iterable)===========")
def sum(x,y):
    return x+y
count = reduce(sum,(10,20,30,40))
print("reduce的结果是否是Iterator：",isinstance(count,Iterator))  # false
print("count: ",count)
print("=============高阶函数===============")
DIGITS = {"0":0,"1":1,"2":2,"3":3,"4":4}
def higherOrder(str):
    def fun1(x,y):
        return x*10+y
    def fun2(s):
        return DIGITS[s]
    return reduce(fun1,map(fun2,str))
#先将“012”遍历转成整数型的迭代器，再将迭代出的整数元素应用fun1进行计算求和。
print(higherOrder("234"))
print("=============高阶函数：filter===========")
#筛选出20000以内的回数，例如12321
nums = range(12300,13000)
def filter1(num):
    sNum = str(num)
    i,nNums = -1,""
    while i+sNum.__len__()>=0:
        nNums= nNums+sNum[i]
        i = i-1
    return nNums == sNum
filterResult = filter(filter1,nums)
for r in filterResult:
    print("回数：",r)
print("==============高阶函数：sorted============")
init = ["Jessy","abc","zoey","Amy"]
sr = sorted(init)
print(sr)
sr = sorted(init,key=str.lower)  # 映射为小写，即忽略原来数据中的大小写，再进行排序
print(sr)
sr = sorted(init,key=str.lower,reverse=True)
print(sr)
print("============高阶函数: 函数作为函数参数或返回值========")
#求和：封装求和过程，而不是直接返回求和结果，需要时，才计算结果
def ttSum(*args):
    def sum():
        init = 0
        for i in args:
            i = int(i)
            init = init + i
        return init
    return sum
sumResult1 = ttSum(*(1,2,3,4,5))
sumResult2 = ttSum(*(1,2,3,4,5))
#每次返回的都是新的函数
print("两次返回值比较：",sumResult1==sumResult2)  # False
print("高阶函数-求和：",sumResult1())
print("============高阶函数：闭包（内层函数引用外层的局部变量）=============")
'''
闭包（Closure）是词法闭包（Lexical Closure）的简称，是引用了自由变量的函数。
这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外
'''
def outter():
    alist = []
    for i in range(1,4):
        def inner():
            return i*i
        alist.append(inner)
    return alist
f1,f2,f3 = outter()
#函数延迟执行，闭包引用循环变量，最后执行时，i=3，最终结果都为 9
print("高阶函数（闭包）执行结果1：", f1(),f2(),f3())  # 9,9,9
# 绑定循环变量，防止它后续发生变化
def outter2():
    alist = []
    def inner1(i):
        def inner2():
           return i*i
        return inner2
    for i in range(1,4):
        alist.append(inner1(i))  # 让函数立即执行，从而绑定循环变量
    return alist
f1,f2,f3 = outter2()
print("高阶函数（闭包）执行结果2：", f1(),f2(),f3()) # 1,4,9
print("高阶函数：实现计数器，每次调用返回递增整数>>>>>>")
def increases(i=[]):
    if i.__len__():
        i.append(i.pop()+1)
    else:
        i.append(1)
    return i[0]
print(increases(),increases(),increases(),increases(),increases())
#利用闭包，创造计数器
def createCounter():
    tmp= [0]
    def counter():
        tmp[0]=tmp[0]+1
        return tmp[0]
    return counter
count1 = createCounter()
print(count1(),count1(),count1(),count1(),count1())



