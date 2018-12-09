# coding=utf-8

print("==========读文件: 手动关闭文件流===========")
try:
    f = open(r"E:\0722python\testio",'r',encoding='utf-8')
    # f 有read方法，f是file-like Object
    print(f.read())   # 打印出文件的所有内容
    # while True:
    #     line = f.readline()
    #     if line:
    #        print(line)
    #     else:
    #         break
except BaseException as e:
    print("error: ",e)
finally:
    if f :
        f.close()
print("==========读文件: 自动关闭文件流===========")
with open(r"E:\0722python\testio",'r',encoding='utf-8') as f:
    ## readlines 读取所有内容，按行返回list
    #lineList = f.readlines()
    #print(lineList.__len__(),'\n',lineList[0])
    ## read(size) 限制读取size个字节byte;两次read，第二次接着第一次读取的位置接着读。
    print(f.read(6))
    print(f.read(20))
print("==============写文件：============")
try:
    # w 覆盖写入，文件不存在就创建  a 追加写入，文件不存在就创建
    f = open(r"E:\ww.txt",'a')
    f.write("\nthis is a new line")
finally:
    if f:
        #必须关闭，因为写数据并不是直接就写入磁盘，不关闭可能数据丢失
        f.close()