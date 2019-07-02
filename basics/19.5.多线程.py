#coding=utf-8

import threading

'''
多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，
因为所有线程共享进程的内存。
'''
print("===============多线程：共享一个变量===================")
lock = threading.RLock()
num = 0
'''
高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
balance = balance + n
也分两步：
计算balance + n，存入临时变量中；
将临时变量的值赋给balance。
【解决方法：加锁。当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁。】
'''
'''
python解释器执行代码时，有一个GIL锁：Global Interpreter Lock。
任何Python线程执行前，必须先获得GIL锁，【否则n个线程的死循环会把n核CPU占满。】
每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
多个Python进程有各自独立的GIL锁，互不影响。
'''
def changeNum(n):
    global num
    num = num + n
    num = num - n
def loopThread(n):
    # for i in range(100000):
    #     changeNum(n)
    for i in range(1000000):
        lock.acquire()
        try:
            changeNum(n)
        finally:
            lock.release()
t1 = threading.Thread(target=loopThread,args=(5,),name="loopThread1")
t2 = threading.Thread(target=loopThread,args=(8,),name="loopThread2")
t1.start()
t2.start()
t1.join()
t2.join()
print("num = ",num)

