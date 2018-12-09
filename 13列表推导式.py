#coding:utf-8
list1 =[ i for i in range(1,11)]

list1=[ i for i in range(1,100) if i%3==0 ]

list1=[ [i,i,i] for i in range(1,10)]
list1=[ [i,j] for i in range(1,10) for j in range(1,4)]
list1=[ (1,2,3) for i in range(1,11) ]

#生成一个[[1,2,3],[4,5,6].[7,8,9]...]的列表最大值在100以内
list1=[ [3*i+1,3*i+2,3*i+3] for i in range(0,100) if i*3+3<100 ]

base=[1,2,3]
list1=[[base[0]+3*i,base[1]+3*i,base[2]+3*i] for i in range(0,100) if 3*i+base[2]<100 ]


base_list1=[True,True,False,False] # [1,1,0,0]
base_list2=[True,False,False,False]

print(list1)