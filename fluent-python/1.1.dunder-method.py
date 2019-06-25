from math import hypot

#构造向量间的计算逻辑

class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    #求向量的长度（模）
    def __abs__(self):
        return hypot(self.x, self.y)
    #向量之间的加减
    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y)
    #向量之间的乘除
    def __mul__(self,other):
        if(type(other)==Vector):
            return Vector(self.x*other.x,self.y*other.y)
        return Vector(self.x*other,self.y*other)
    '''
    如果一个对象没有 __str__ 函数，而 Python 又需要调用它的时候，
    解释器会用 __repr__ 作为替代。所以，建议实现__repr__方法。
    '''
    def __str__(self):
        #return "Vector(%s,%s)"%(str(self.x),str(self.y))
        # %r打印时能够重现它所代表的对象
        return "Vector(%r,%r)"%(self.x,self.y)
    #如果不存在 __bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()。0为false.
    def __bool__(self):
        return bool(self.x or self.y)
    # def __len__(self):
    #     return int(abs(self))  #要返回int，而不是float。

v1 = Vector(3,4)
print("v1的长度：",abs(v1))
v2 = Vector(1,2)
v3 = v1+v2
print("v3=",v3)
#print(v1*v2)
print("v2*v1=",v1*v2)
print("3*v1=",v1*3)
print("v1的布尔值:",bool(Vector(0,1)))



