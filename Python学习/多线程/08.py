import threading, queue
from time import sleep

class Producer(threading.Thread):
    def run(self):
        global  queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count +=1
                    msg = "gc"+str(count)
                    queue.put(msg)
                    print(msg)
            sleep(0.5)
class Consumer(threading.Thread):
    def run(self):
        global  queue
        while True:
            if queue.qsize()> 100:
                for i in  range(3):
                    msg = self.name +"gd"+queue.get()
                    print(msg)
            sleep(1)


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(500):
        queue.put("初始产品"+str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()