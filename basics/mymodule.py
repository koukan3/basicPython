#coding:utf-8
class Animal(object):

    name="动物"

    def say(self):
        print("父类的函数")


class Parent(object):

    def __init__(self):
        self.age=20
    def work(self):
        print("父类Parent的函数")

    def say(self):
        print("父类Parent的函数")

class Dog(Animal,Parent):

    __instance=None
    def __init__(self,xsex):
        self.sex=xsex
    def work(self):
        print("子类重写的函数")

    def __new__(cls, *args, **kwargs):
        if cls.__instance==None:
            cls.__instance=object.__new__(cls)
        return cls.__instance

if __name__=="__main__":
    dog1=Dog("雌性")
    dog2=Dog("雄性")
    print(dog1.sex)
    print(dog1==dog2)
    print(Dog.__mro__)