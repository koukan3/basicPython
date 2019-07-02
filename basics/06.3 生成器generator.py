#coding:utf-8
from collections import Iterator,Iterable
import types

print("======类型 判断===========")
print(type(abs)==types.BuiltinFunctionType)

print("============定义生成器：斐波那契数列==========")
def fibonacci(max):
    n,a,b,c = 0,0,1,1
    while n<=max:
        # print(c)
        yield c
        c = a + b
        a = b
        b = c
        n = n + 1

generator1 = fibonacci(7)
print(isinstance(generator1,Iterable))   # true
print(isinstance(generator1,Iterator))   # true
print(generator1)  # <generator object fibonacci at 0x0000016971B9A570>
print("======循环1========")
for g in generator1:
    if g:
        print(g)

generator2 = fibonacci(7)
print("======循环2========")
while True:
    try:
        i = next(generator2)
        # print(isinstance(i,Iterator))  # false
        print(i)
    except StopIteration as e:
        print("END of generator: ",e.value)
        break


