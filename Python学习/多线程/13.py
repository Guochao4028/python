import  multiprocessing
from  time import ctime, sleep
def clocl(interval):
    while True:
        print(ctime())
        sleep(interval)
if __name__ == '__main__':
    p = multiprocessing.Process(target= clocl, args=(5,))
    p.start()
    while True:
        sleep(1)