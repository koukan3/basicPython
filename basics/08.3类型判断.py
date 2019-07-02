# coding=utf-8

import types

def func():
    pass
class Animal(object):
    pass
class Dog(Animal):
    pass

print("===========type()类型判断=========")
print(type(123)==int)
print(type('abc')==str)
print(type([1,2])==list)
print(type((1,))==tuple)
print(type({"a",1})==set)
print(type({"a":1,2:2})==dict)
print(type(func)==types.FunctionType)
print("============isinstance()类型判断=========")
a = Animal()
d = Dog()
print(isinstance(d,Animal))  # True
print(isinstance(d,Dog))  # True
print(isinstance(a,Dog))  # False
print(isinstance(d,(Animal,object)))  # True
print(isinstance(abs,types.BuiltinFunctionType))  # True