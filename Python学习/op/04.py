'''
Mixin案例
'''
class Perons():
    name = "liu"
    age = 18
    def eat(self):
        print("eat")
    def sleep(self):
        print("sleep")

class Teacher(Perons):
    def work(self):
        print("work")
        return None
class Student(Perons):
    def Study(self):
        print("study")
class Tutor1(Teacher, Student):
    pass
t = Tutor1()
#print(Tutor.__mro__)
#print(t.__dict__)
#print(Tutor.__dict__)

#转成mixin实现

class TeacherMixin():
    def work(self):
        print("wprk")
class StudentMixin():
    def stduy(self):
        print("study")
class Tutor(Perons, TeacherMixin, StudentMixin):
    pass
tt = Tutor()