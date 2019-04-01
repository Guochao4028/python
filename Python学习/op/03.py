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
#构造函数的概念
class Anime():
    pass
class PaXingAni(Anime):
    pass

class Dog(PaXingAni):
    # __init__就是构造函数
    #每次实例化的时候第一个被调用
    #因为主要工作是进行初始化，所有得名构造函数
    def __init__(self):
        print("__init__")
#实例化的时候，括号内的参数需要跟构造函数参数匹配
d = Dog()