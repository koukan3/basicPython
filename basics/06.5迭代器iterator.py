#coding:utf-8
from collections import Iterator,Iterable

# 可迭代的，不一定是迭代器； 是迭代器的，一定可迭代
# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列

print("list是否是迭代器：",isinstance([],Iterator))  # False
print("list是否可迭代：",isinstance([],Iterable))  # True

print("string是否是迭代器：",isinstance("abc",Iterator))  # False
print("string是否可迭代：",isinstance("abc",Iterable))  # True

print("tuple元组是否是迭代器:", isinstance((1,2,3),Iterator))  # False
print("tuple元组是否可迭代:", isinstance((1,2,3),Iterable))   #True

print("dict字典是否是迭代器：",isinstance({"a":1,"b":2},Iterator))  # False
print("dict字典是否可迭代：",isinstance({"a":1,"b":2},Iterable))   # True

print("set 是否是迭代器：",isinstance({"a","b"},Iterator))  # False
print("set 是否可迭代：",isinstance({"a","b"},Iterable))   #True

print("for循环结果是否是迭代器：",isinstance((x for x in range(1,3)),Iterator))  # True
print("for循环结果是否可迭代：",isinstance((x for x in range(1,3)),Iterable))  # True

print("=========创建 迭代器 iterator ============")
it = iter([10,20,30])
print("iter创建迭代器：",isinstance(it,Iterator))
while 1:
    try:
       print("iterator.next: ",next(it))
    except StopIteration:
        print("迭代器迭代为空了")
        break
it = (x for x in range(10,15))
while True:
    try:
        print("iterator.next: ",next(it))
    except StopIteration:
        print("迭代器迭代为空了")
        break




