#coding=utf-8
import math
# 普通函数
def test1(a,b):
    print("test函数")
    return a+b
PI = 3.14
def area_of_circle(r):
    return PI*r*r
print("半径为%.2f的圆的面积是：%.3f"%(1.2,area_of_circle(1.2)))

print("==============不定长参数============")
def test2(a,*b,**c): #** 表示包含有k,v不定长参数
    print(b)
    print(c)
    sum=a
    for i in b:
        sum+=i
    return sum

print("不定长参数：",test2(100,1,2,10,f2=20,f3=30))

def test2_1(*a):
    print("不定长参数/可变参数：",a)
alist = [1,1,0]
test2_1(alist)  #将列表list当成可变参数tuple中的一个元素
test2_1(*alist) #将list展开对应成可变参数中的每一个元素

def test2_2(**a):
    print("不定长参数/关键字参数：",a)
test2_2(a=3,b=4)
dictParam = {"a":3,"b":4}
test2_2(**dictParam)

print("=========缺省参数函数 ,一定要写在后面==============")
def test3(a,b=100):
    return a+b
# print(test3(1,20))
def test3_1(*a,b=20,c=30):
    print("a=%s,b=%s,c=%s"%(a,b,c))
test3_1(4,b=5)
test3_1(4,5)
def test3_2(a,list1=['a','b']): # 陷阱
    list1.append(a)
    return list1
print(test3_2(10)) # a ,b ,10
# print(test3_2(20,['c','d'])) # c,d 20
print("default value: ",test3_2(30)) # a,b,10,30

def test3_3(a,b,*,city,name):
    print("命名关键字参数：",a,b,city,name)
test3_3(1,2,city=3,name=4) #当参数没有默认值时，参数关键字一定要指定为city，name
def test3_4(a,b,*c,city,name):
    print("命名关键字参数：",a,b,c,city,name)
test3_4(1,2,5,3,city="bj",name="shunyi") #当参数中有可变参数时，就不需要加分隔符 *

# 内嵌函数
def f1():
    def f2():
        print("内嵌函数")
    f2()

# f1()

# 匿名函数: 匿名函数中智能用python表达式
func1=lambda x,y:x+y
# func1(1,100)

# 递归函数 ：计算一个数字的阶乘
def test4(n):
    if n<=1: #设置递归的边界
        return 1
    else:
        return n*test4(n-1)
# print(test4(6))

# 高阶函数 ,1、把函数作为形参，2、把函数作为返回值
# 打印1到n(包括n)之间的所有数字的阶乘
def test5(n,f):
    for i in range(1,n+1):
        print(f(i))
# test5(10,test4)
def test6(x,y):
    def func3(z):
        return x+y+z
    return func3
# print(test6(100,200)(300))

# 局部变量和全局变量，函数中默认是不能修改全部变量引用
a=100
str1="hello"
list2=[10,20,30]
def test7():
    a=200 #定义一个局部变量而已
    global str1
    str1="laoxiao" #修改全局变量的引用,修改全局变量的引用需要加global
    #list2[0]=100
    list2 = [1,2,3]
    print("局部变量:%d"%a)
    # print("全局变量:%d"%b)
test7()
print("全局变量：",a)
print("全局变量：",str1)
print("全局变量：",list2)