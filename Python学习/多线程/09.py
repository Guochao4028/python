import  threading
import time
lock_1 = threading.Lock()
lock_2 = threading.Lock()
res = lock_1.acquire(timeout=4)
if res:
    pass