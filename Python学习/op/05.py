#属性案例
#创建Student类，描述学生类
#学生具有Student.name属性
#但name格式并不统一
#可以用增加一个函数，然后自动调用的方式但很蠢
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.setName(name)
    def intro(self):
        '''
        介绍自己
        :return:
        '''
        print("hai, my name:{0}".format(self.name))
        return None
    def setName(self, name):
        self.name = name.upper()
s1 = Student("LIU Ying", 19)
s2 = Student("michi stangle", 24)
s1.intro()
s2.intro()

#peroperty案例
#定义一个person类，具有name, age 属性
#对于任何输入的姓名，大写保存
#年龄，统一整数
#X = property（fget，fset，fdel，doc）
class Person():
    def fget(self):
        return self._name
    def fset(self, name):
        self._name = name.upper()
    def fdel(self):
        self._name = None
    name = property(fget, fset, fdel, "对name进行以下操作")
    def getAge(self):
        return self._age
    def setAge(self, age):
        self._age = age+1
    age = property(getAge, setAge)
p1 = Person()
p1.name = "tuling"
p1.age = 7
print(p1.age)

class Proson1():
    def __set__(self, instance, value):
        pass
    def __get__(self, instance, owner):
        pass
    def __delete__(self, instance):
        pass
