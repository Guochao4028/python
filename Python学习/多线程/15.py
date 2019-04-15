import os
from  multiprocessing import  Process
def info(title):
    print(title)
    print("module_name",__name__)
    #得到父进程的id
    print("parent process", os.getppid())
    #得到本身进程的id
    print("process id : ", os.getpid())

def f(name):
    info("function f")
    print("hello",name)

if __name__ == '__main__':
    info("main line")
    p = Process(target= f, args= ("bbb",))
    p.start()
    p.join()