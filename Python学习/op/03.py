'''
类的三大特性
'''
'''
封装
'''
#class Person():
#   name = "adf"
#    __age = 18
#p = Person()
#print(p.name)
#p._Person__age = 19
#print(p._Person__age)

#name mangling技术
#print(Person.__dict__)

'''
继承
'''
'''
#在Python中，任何类都有一个共同的父类叫做object
class Person():
    name = None
    age = 0
    def sleep(self):
        print("*"*20)
        return  None
class Teacher(Person):
    def make_test(self):
        print("teacher","*"*21)
        return None
    def sleep(self):
        print("asdf")
        self.make_test()
        super().sleep()


t = Teacher()
t.name = "adsf"
t.sleep()
t.make_test()
print(t.name)
'''
'''
#构造函数的概念
class Anime():
    pass
class PaXingAni(Anime):
    def __init__(self, name):
        print("paxingdongwu => {0}".format(name))

class Dog(PaXingAni):
    # __init__就是构造函数
    #每次实例化的时候第一个被调用
    #因为主要工作是进行初始化，所有得名构造函数
    def __init__(self):
        print("__init__")
#实例化的时候，括号内的参数需要跟构造函数参数匹配

class Cat(PaXingAni):
    pass
d = Dog()
c = Cat("gg")

#super

class Person():
    def __init__(self):
        print(1)
class A(Person):
    def __init__(self):
        print(2)
        super().__init__()
a = A()
print(A.__mro__)
'''
class Fish():
    def __init__(self, name):
        self.name = name
    def swim(self):
        print("mming")
class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("fly")
class Person():
    def __init__(self, name):
        self.name = name
    def work(self):
        print("work")
class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name
s = SuperMan("yy")
s.fly()
s.swim()
s.work()