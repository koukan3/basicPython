#coding:utf-8
#list 就是数组 ,有序，可重复,可以的
list1=[1,2,5,3,4,5]
print(list1[2:])
print("list的元素个数：",len(list1))
l1,l2,l3,l4,l5,l6= list1
print("list中的元素：",l1,l2,l3,l4,l5,l6)
blist = []
print("empty list: ",blist[0])  # IndexError: list index out of range

print("=========列表元素的增删改查========")
list1.insert(0,100)
list1.append(200)
print("insert/append之后：",list1)
print("list.pop(2): ",list1.pop(2))
print("pop之后：",list1)
#删除第一次出现的元素5
list1.remove(5)
print("remove之后：",list1)
del(list1[0])
print("del(list[0])之后，list的元素个数：",len(list1)) # len获取字符串或者集合的长度
print("当前的list: ",list1)
list1[1]=111
print("list1[1]=111改变之后：",list1)
print("查询list[3]: ",list1[3])
print("查询%d的index: "%5,list1.index(5))

print("=========列表中的列表元素========")
l2 = ['tom',123]
l3 = ['jack',0.1,l2,'amy']
print(l3)
print("l3[2][0]:",l3[2][0])
for i in list1:
    print(i)

for i,item in enumerate(list1):
    print("下标是：%d,值:%d"%(i+1,item))

print("============列表生成式===========")
lc = [x*2 for x in range(10)]  # 0~9
print("list comprehensions: ",lc)
lc = [x*2 for x in range(10) if x%2==0]  # 0~9
print("list comprehensions: ",lc)
lc = [m+n for m in "ABC" for n in "XYZ"]
print("list comprehensions: ",lc)
list2 = ["apple",18,"Xiaomi","Huawei"]
lc = [d.upper() for d in list2 if isinstance(d,str)]
print("list comprehensions: ",lc)