'''
利用time函数 生成两个函数
顺序调用
计算总运行时间
'''
import time

def loop1():
    #ctime 得到当前时间
    print('start loop 1 at :', time.ctime())
    #睡眠时间 单位秒
    time.sleep(4)
    print("end loop 1 at:",time.ctime())

def loop2():
    #ctime 得到当前时间
    print('start loop 2 at :', time.ctime())
    #睡眠时间 单位秒
    time.sleep(2)
    print("end loop 2 at:",time.ctime())
def main():
    print("start at :",time.ctime())
    loop1()
    loop2()
    print("all done at:",time.ctime())

if __name__ == '__main__':
    main()