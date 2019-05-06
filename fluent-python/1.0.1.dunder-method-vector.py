from math import  hypot

'''
使用双下方法/特殊方法实现向量运算：
1.定义向量：v1=Vector(3,4)  v2=Vector(2,1)
2.向量相加：v1+v2=Vector(5,5)
3.向量的模：abs(v1)=5
4.向量与标量的乘法：v1 * 2 = Vector(6,8)
'''

class Vector:
    #定义向量
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    # 把一个对象用字符串的形式表达出来,相当于Java中的toString
    def __repr__(self):
        # % 和 str.format都表示格式化
        # %r 来获取对象各个属性的标准字符串表示形式
        return 'Vector(%r, %r)' % (self.x, self.y)

    #__repr__方便开发人员调试和记录日志，__str__是给终端用户看的
    # def __str__(self):
    #     return 'Vector(%r, %r)' % (self.x, self.y)

    #求向量的模
    def __abs__(self):
        #返回欧几里得距离
        return hypot(self.x, self.y)

    #向量的模是0时，返回False；否则返回True。
    #对于bool()，python会调用__bool__，如果不存在__bool__，会调用__len__. 0对应False，其他对应True.
    def __bool__(self):
        return bool(self.x or self.y)

    #向量相加，不改变被操作的向量，而是返回一个新的向量
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    #向量与标量相乘，也是返回一个新的向量。
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(3,4)
v2 = Vector(3,1)
print(v1)
print(abs(v1))
print(v1+v2)
print(v1*3)