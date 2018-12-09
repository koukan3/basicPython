# -*- coding:utf-8 -*-

import threading,time,multiprocessing

print("=================创建线程======================")
def loop():
    print("thread %s is running..."%threading.current_thread().name)
    n = 0
    while n<5:
        n = n + 1
        print("thread %s is running >>> %d"%(threading.current_thread().name,n))
        time.sleep(1)
    print("thread %s ends..."%threading.current_thread().name)

print("thread %s is runing ..."%threading.current_thread().name)
t = threading.Thread(target=loop,name="loopThread")
t.start()
t.join()
print("thread %s ends..."%threading.current_thread().name)
print("cpu count: ",multiprocessing.cpu_count())

