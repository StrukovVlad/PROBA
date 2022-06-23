import threading
import time

time1=time.time()
def count(num: int):
    return print(num*2)

for n in range(100):
    thread=threading.Thread(target=count,args=(n,))
    thread.start()
    #count(n)

print(time.time()-time1)