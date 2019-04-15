import  threading
from time import sleep

def func():
    print("run")
    sleep(4)
    print("i am done")


if __name__ == '__main__':
    t = threading.Timer(6, func)
    t.start()
    i = 0
    while True:
        print("{0}".format(i))
        sleep(3)
        i+=1
        if i >10:
            break