#coding:utf-8
# age=input("请输入年龄:")

# age=int(age) #类型转换
# # ：和缩进控制代码格式
# if age<18:
#     print("未成年")
# elif age>=18 and age<35:
#     print("青年")
# else:
#     print("中老年")


# 打印九九乘法表
line=1
while line<10:
    column=1
    while column<=line:
        print("%d*%d=%d"%(line,column,column*line),end="\t")
        column+=1
    print()
    line+=1


#计算1加100的和
sum=0
for i in range(1,101):
    sum+=i
print(sum)

print("============循环中的continue,break==============")
#range(11):0 0~10
for i in range(11):
    if i%2==0:
        continue
    print("i={0}".format(i))
    if i>5:
        break

dict1 = {"1st":100,2:20}
for i in dict1:
    print("K=%s,V=%s"%(i,dict1[i]))
