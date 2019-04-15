from time import ctime,sleep
import threading
class ThreadFunc:
    def __init__(self, name):
        self.name = name
    def loop(self, nloop, ntime):
        '''

        :param nloop:  名字
        :param ntime: 停留时间
        :return
        '''
        print("nloop",nloop,"ntime",ntime)
if __name__ == '__main__':
    t = ThreadFunc("loop")
    t1  = threading.Thread(target= t.loop, args=("loop1",8,))
    t1.start()
    t2 = threading.Thread(target=ThreadFunc("loop").loop, args=("loop2", 9,))
    t2.start()
    t1.join()
    t2.join()
    print("all done",ctime())
