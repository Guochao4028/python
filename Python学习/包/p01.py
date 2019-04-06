# 包含一个学生类
#一个sayHello函数
#一个打印语句

class Stutendt():
    def __init__(self, name = None, age = 18):
        self.name = name
        self.age = age
    def say(self):
        print("name"+self.name)
def sayHi():
    print("Hi")
# 此判断语句建议一直作为程序入口
if __name__ == "__main__":
    print("p01模块")
