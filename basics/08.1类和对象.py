#coding:utf-8

class Employee:
    '员工类'

    emp_count=0 # 类属性

    @classmethod
    def say_hello(cls): # 类函数（方法）,第一个形参必须是当前的类 ，通过类名或者对象来调用
        print("类函数，当前类名是:%s"%cls.__name__)
        print("当前类的api文档:%s"%cls.__doc__)

    @staticmethod
    def static_method(): # 类里面静态函数,通过类名或者对象来调用
        print("静态函数")

    def __init__(self,xname,xsalary): # self代表当前类的实例 == java this  scala 中this
        self.name=xname # self.xxx 。xxx就是成员属性 ，默认属性都是public
        # self.salary=xsalary
        self.__salary=xsalary # __(两个下划线)开头的属性就是私有的
        self._sex='男' # _(一个下划线)开头的属性就是保护的
    def work(self,*arg): # 成员函数第一个形参，必要有，代表当前类的实例
        print("%s正在工作"%self.name)
        print(self.__salary)

    def __str__(self):
        return "java中toString"
    def __del__(self): #对象的内存地址引用数为0的时候开始回收
        print("对象被回收的时候")

    def __new__(cls, *args, **kwargs): #必须有返回值,返回当前类的实例,第一形参代表：当前类
        return object.__new__(cls)


print(Employee.emp_count)
Employee.say_hello()
Employee.static_method()
emp1 = Employee("zhangsan",3000) # 创建类的实例
print(emp1.name) #成员属性的访问
emp1.name="lisi" # 修改成员属性
emp1.work()
emp2=emp1
# emp2.static_method()
# __init__重写object父类的方法，代表：初始化的函数
# __str__
# __del__
#__new__ 构造函数



del(emp1)
print("程序结束")