# -*- coding:utf-8 -*-


# 写一个简单类
# 表示该类继承自object,object是所有类都会最终继承的类
class Stu(object):

    '''
    __init__方法的第一个参数永远是self，表示创建的实例本身;
    在__init__方法内部，就可以把各种属性绑定到self
    有了__init__方法，在创建实例的时候，必须传入与__init__方法匹配的参数，
    但self不需要传，Python解释器自己会把实例变量传进去
    '''
    def __init__(self,name,score,gender):
        self.name = name
        self.score = score
        self.__gender = gender
    '''
    和普通的函数相比，在类中定义的函数的第一个参数永远是实例变量self，
    除此之外，类的方法和普通函数没有什么区别。
    调用时，不用传递该参数。
    '''
    def print_info(self):
        print("Name: %s , Score: %s"%(self.name,self.score))
    def set_score(self,score):
        # 对赋值进行条件限定
        if not isinstance(score,int):
            raise ValueError('score must be an int type')
        if score<0 or score>100:
            raise ValueError('score must between 0 ~ 100')
        self.score = score
    # 对于private变量，只能在内部访问
    def getGender(self):
        return self.__gender
    def setGender(self,gender):
        self.__gender = gender
    def getInfo(self):
        print("this is a student...")

class Andy(Stu):
    def getInfo(self):
        print("this is a student named Andy...")

class Tom(Stu):
    def getInfo(self):
        print("this is a student named Tom...")

class Teacher(object):
    def getInfo(self):
        print("this is a teacher...")


class Dict(dict):
    def __init__(self,**kv):
        super().__init__(**kv)
    def __getattr__(self, item):
        try:
            return self[item]
        except BaseException:
            raise AttributeError("no attr like %s exist"%item)
    def __setattr__(self, key, value):
        self[key] = value

d = Dict(a=1,b=2)
print("Dict====>",d["a"])
print("Dict====>",d.a)
