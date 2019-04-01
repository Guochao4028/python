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
yueyue = PythonStudent()
print(yueyue.name)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()