'''
类的三大特性
'''
'''
封装
'''
class Person():
    name = "adf"
    __age = 18
p = Person()
print(p.name)
p._Person__age = 19
print(p._Person__age)

#name mangling技术
print(Person.__dict__)