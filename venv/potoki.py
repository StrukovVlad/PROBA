import multiprocessing
import time

t1=time.time()

def worker(num):
    return print(num*2)

if __name__=='__main__':
    jobs=[]
    for i in range(100):
        p=multiprocessing.Process(target=worker,args=(i,))
        jobs.append(p)
        p.start()

    print(t1-time.time())
