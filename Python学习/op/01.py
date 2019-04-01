# coding=utf-8
'''
定义一个学生类，用来形容学生
'''

# 定义一个空类
class Student():
    # 一个空类，pass代表直接跳过
    #此处pass必须有
    pass
# 定义一个对象
mingyue = Student()

'''
#再定义一个类用于描述听Python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "python"
    #需要注意
    #1，def doHomework的缩进层级
    #2，系统默认有一个self参数
    def doHomework(self):
        print("做作业")
        return None
#实例化一个叫yueyue的学生，是一个具体的人
#yueyue = PythonStudent()
#print(yueyue.name)
#print(yueyue.__dict__)
#print(PythonStudent.__dict__)
# 注意成员函数的调用没有传递进入参数
#yueyue.doHomework()

class A():
    name = "dana"
    age = 18
    def say(self):
        self.name = "aaa"
        self.age = 200
#此时 a 称为类的实例
print(A.name)
print(A.age)
print("*"*20)
print(id(A.name))
print(id(A.age))
print("*"*20)
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

#此例说明类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下。指向同一变量
'''
'''
class A():
    name = "dana"
    age = 18
    def say(self):
        self.name = "aaa"
        self.age = 200
#此时 a 称为类的实例
print(A.name)
print(A.age)
print("*"*20)
print(id(A.name))
print(id(A.age))
print("*"*20)
a = A()
a.name = "asd"
a.age = 10
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
'''
'''
class Student():
    name = "da"
    age = 18
    def say(self):
        self.name = "aaa"
        self.age = 200
        print("my name is {0},age{1}".format(self.name,self.age))
        return  None
    def sayAgain(s):
        print("my name {0}".format(s.name))
        return None
yy = Student()
yy.say()
yy.sayAgain()
'''

class Teacher():
    name = "d"
    age = 19
    def say(self):
        self.name = "aaa"
        self.age = 200
        print("my name is {0},age{1}".format(self.name, __class__.age))
        return None
    def sayA():
        print("asdf")
        print(__class__.name)
        print(__class__.age)
        return None
t = Teacher()
t.say()
Teacher.sayA()
