#coding:utf-8
# import mymodule # 自动执行模块中代码

# dog3=mymodule.Dog() # 模块名.函数(类)
from os import path as os_path
from mymodule import Dog # from 模块 import 函数(类)
from mymodule import * # 出现名字冲突

dog4 =Dog()
a =Animal()

