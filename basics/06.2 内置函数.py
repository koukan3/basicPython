#-*- coding:utf-8 -*-
print("======ord: 打印字符对应的ASCII或Unicode值====")
print("ord:",ord('a'))
print("chr:",chr(97))
print("中文",ord("焱"))

print("=======字符串长度/字节数：len()======")
print("len(str): ",len("abcd"))
print("len(bytes): ",len(b"abcd"))
print("len(str): ",len("字符串"))
#print("len(bytes): ",len(b"字符串"))  #SyntaxError: bytes can only contain ASCII literal characters
print("len(bytes):",len("字符串".encode("utf-8")))

print("==========数据类型转换============")
print("bool(%s)="%0,bool(0))
print("bool(%s)="%1,bool(1))
print("bool(%s)="%"",bool(""))
print("bool(%s)="%None,bool(None))
print("bool(%s)="%[],bool([]))
print("==========数据类型转换2============")
print("按10进制进行转换：",int("11"))
print("按2进制进行转换：",int("11",2))
print("按16进制进行转换：",int("11",base=16))
print("===========hex十六进制字符串==============")
h = hex
print("hex(): ",hex(123))
print("hex(): ",h(123))