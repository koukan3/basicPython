# -*- coding:utf-8 -*-

from multiprocessing import Process,Queue
import os,time,random

print("==========进程间通信：父进程创建Queue，用于子进程间的通信==============")
#  子进程A >>>>>>>写数据>>>>> Queue <<<<<<读数据<<<<<< 子进程B
def write2queue(q):
    print("write to queue by process (%s)"%os.getpid())
    for i in ['a','b','c']:
        print("start to write %s ...."%i)
        q.put(i)
        time.sleep(random.random())
def readQueue(q):
    print("read from queue by process (%s)"%os.getpid())
    while True:
        value = q.get(True)
        print(" read data: %s ..."%value)

if __name__=='__main__':
    print("parent process (%s) start to create a Queue"%os.getpid())
    # Queue : FIFO
    q = Queue()
    # child process 1
    wp = Process(target=write2queue,args=(q,))
    # child process 2
    rp = Process(target=readQueue,args=(q,))
    #开始写和读的进程
    wp.start()
    rp.start()
    #等待进程完成
    wp.join()
    #强行终止读的进程
    rp.terminate()
