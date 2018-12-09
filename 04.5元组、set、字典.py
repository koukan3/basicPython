#coding:utf-8
#tuple 元组,没有长度限制，但是只要创建就不可修改，有序，可以重复
t1 =() # 空元组
t2=('hello','python','spark')
i1,i2,i3 = t2
print(t2[1])
print("元组中的各项为：",i1,i2,i3)
# t2[0]="hadoop"   #TypeError: 'tuple' object does not support item assignment
# a,b=100,200

t3=(100,) #一元组的写法

#set集合，不可重复，没有顺序
# s1={100,500,200,1,100}
# print(len(s1))
# s1.add(300)
# print(len(s1))
# item1=s1.pop()
# print(item1)
# print(len(s1))
# for i in s1:
#     print(i)

#字典 ，java中Map
print("============字典dict的增删改查==============")
dict1={"s":100,"t":200,"s":300,10:400}
d = dict(s=100,t=200)
print("查询get({0}): {1}".format("s",dict1.get("s","no found")))
print(dict1)
dict1['t']=2000 #修改
dict1['x']=500 # 添加
print("修改和添加之后的dict：",dict1)
del(dict1['s']) # 删除一个元数
print("del删除之后的dict：",dict1)
print("删除 %s 之后的dict：%s"%(dict1.pop('x',123),dict1))


dict1.keys() # 返回所有的key
dict1.values() # 所有的值
dict1.items() # 所有元素
for k,v in dict1.items():
    print("键为：%s,值为:%s"%(k,v))

dict1.clear()
print("字典clear之后：",dict1)

'''
#注意：只有不可变类型才能作为key
dict2 = {[1,2]:"v1"}  # TypeError: unhashable type: 'list'
print("dict2: ",dict2)
'''
# 可变类型：list，set,dict
# 不可变类型:int,float,string,tuple

# str1="hello laoxiao"
#
#
# str2=str1.replace("laoxiao","laowang")
# print(str2)
# a=100
# b=100
# print(id(a))
# print(id(b))
print("=============set:不重复的key的无序集合================")
#alist = [1,2,3,"four",[5]]  #TypeError: unhashable type: 'list'
alist = [1,2,3,"four"]
aset = set(alist)
aset2 = set([5,6,"seven",3,"four"])
print("aset: ",aset)
print("aset & aset2: ",aset & aset2)
print("aset | aset2: ",aset | aset2)

