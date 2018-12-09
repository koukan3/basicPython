# -*- coding:utf-8 -*-
# 匿名函数的关键字 lambda,:冒号前的变量表示参数
lam = lambda x:x*x
'''
lambda x:x*x 相当于：
def fun(x):
    return x*x
'''
print("调用lambda函数：",lam(6))
alist = map(lam,[1,2,3,4,5])
print("map映射之后的list：")
tmp=[]
for a in alist:
    tmp.append(a)
print(tmp)
def fun(x):
    return x+1
lam2 = lambda x:fun(x)
print("匿名函数中返回函数: ",lam2(100))

print("=======练习：改造非匿名函数/代码 为匿名函数============")
#改造前：
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print("列出1到20中的奇数：",L)
#改造后：
L = list(filter(lambda n:n%2==1,range(1,20)))
print("列出1到20中的奇数：",L)
