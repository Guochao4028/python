import time
import  threading as thread
def loop1(nl):
    print("start loop 1 at", time.ctime())
    print("参数",nl)
    time.sleep(4)
    print("end loop 1 at", time.ctime())
def loop2(n1, n2):
    print("start loop 2 at", time.ctime())
    print("参数", n1, "*"*10, n2)
    time.sleep(4)
    print("end loop 2 at", time.ctime())
def mian():
    print("Start at:", time.ctime())
    t1 = thread.Thread(target=loop1, args=("gc",))
    t1.start()
    t2 = thread.Thread(target=loop2, args=("cg", "cg1", ))
    t2.start()
    t1.join()
    t2.join()
    print("All done at",time.ctime())
    
if __name__ == '__main__':
    mian()