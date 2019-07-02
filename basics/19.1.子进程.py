# -*- coding:utf-8 -*-

from multiprocessing import Process,Pool
import os,time,random

#print1
print("===========创建子进程：fork(), 用在Unix/Linux/Mac系统环境中=======")
#print2
print("===========创建子进程：Process,跨平台版本的多进程支持==========")

def runProc(name):
    print("run child process name:%s , pid:%s ..."%(name,os.getpid()))
# command line:
if __name__=='__main__':
    print("parent process (%s) ..."%os.getpid())
    p = Process(target=runProc,args=('test',))
    print("--- child process start running ---")
    # 启动子进程，上面的print1,2会打印两次
    p.start()
    # 等待进程执行完后再往下执行，用于同步
    p.join()
    print("--- child process end ---")

#print3
print("===========创建子进程：Pool,进程池中批量创建子进程==========")
def batchProc(name):
    print("run sub-process name:%s , id:%s..."%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("sub-process (%s : %s) running last %s ..."%(name,os.getpid(),(end-start)))
if __name__=='__main__':
    print("Pool,parent progress (%s)"%os.getpid())
    # Pool默认大小（同时执行的进程数）是CPU核数。
    p = Pool(6)
    for i in range(6):
        # 每个子进程执行的时候，都会把print3打印一遍
        p.apply_async(batchProc,args=(i,))
    print("waiting for all sub-process done ...")
    # 调用close之前必须先调用close，close之后就不能添加新的process了。
    p.close()
    # 等待所有子进程执行完毕
    p.join()
    print("---- END ----")
