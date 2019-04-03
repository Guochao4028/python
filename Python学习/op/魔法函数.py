#__call_举例
class A():
    name = None
    def __init__(self):
        print("调用")
    def __call__(self, *args, **kwargs):
        print("对象当函数调用")
    def __str__(self):
        return "函数名"
    def __getattr__(self, item):
        print("no have")
        print(item)
# a = A()
# a()
# print(a)
# print(a.addr)

#__setarrt__
class Person():
    def __init__(self):
        pass
    def __setattr__(self, key, value):
        # self.name = value
        #避免死循环 统一对父类魔法函数
        super().__setattr__(key,value)
# p = Person()
# print(p.__dict__)
# p.age = 18

#__gt__
class Student():
    def __init__(self, name):
        self._name = name
    def __gt__(self, obj):
        print(obj._name)
        return self._name > obj._name
stu1 = Student("one")
stu2 = Student("two")
print(stu1 > stu2)

