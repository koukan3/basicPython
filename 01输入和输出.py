#coding:utf-8

#print 是python标准库中内置函数，del，len，
print("abc")
print(100)

age=34
name="laoxiao"
str2 ="姓名是:%s,年龄是:%s,π的值是:%.2f"%(name,age,3.145)
print(str2)

# input 函数：python2中输入的内容都当成python代码（python表达式）,python2用raw_input替换
#username=raw_input("请输入姓名:")
#print(username)

#input 输入

inputName=input()
print(inputName)
#input 输入2  print 输出
num=input("请输入一个数：")
num = int(num)
i=1
while num:
    print("i=",i)
    i = i+1
    num = num -1

#print("刚才输入的姓名是：",inputName)
#print("刚才输入的姓名是：%s"%inputName)
#print("刚才输入的姓名是：%s"%(inputName))