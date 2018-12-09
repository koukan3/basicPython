#coding=utf-8

import functools
#偏函数 partial function，固定函数的某些参数，即赋予默认值，用以简化函数的调用
print("===== 按2进制进行整数转换 ====")
def int2(s):
    try:
        return int(s, base=2)
    except ValueError:
        print("invalid literal for int()...")
print(int2("0110"))
print("===== 偏函数：按2进制进行整数转换 ====")
int2_1 = functools.partial(int,base=2)
print(int2_1("0110"))

# 偏函数中的参数也可以是函数、不定长参数
param = {"base":2}
int2_2 = functools.partial(int,**param)
print(int2_2("0110"))

# 也可以改变 偏函数中的默认值
print(int2_1("0110",base=10))





