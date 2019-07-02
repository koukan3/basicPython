# -*- coding:utf-8 -*-

from io import StringIO,BytesIO
import os

#StringIO: 读写发生在内存中
print("==========StringIO: 写入内存==========")
f = StringIO()
print(f.write("hello"))   # 返回写入的字符数
f.write(",")
f.write("world!")
print(f.write("中"))
print(f.getvalue())
f.close()
print("==========StringIO: 读内存==========")
f = StringIO("content\nfrom\nMemory")
#print(f.read())
while True:
    line = f.readline()
    if line:
        # 去掉首尾指定的字符（空格）
        print(line.strip())
    else:
        break
if f:
    f.close()

print("===========bytesio: 读写字节byte===========")
f = BytesIO()
print(f.write("中文".encode("utf-8")))
print(f.write(bytes("abc".encode("gbk"))))
print(f.getvalue())
f.close()

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87abc')
print(f.read())
f.close()