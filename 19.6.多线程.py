#coding=utf-8

import threading

print("=============多线程：不共享变量（使用threadlocal）=============")
# 全局变量；threadlocal
tlocal = threading.local()

def doThread(name):
    '''
    tlocal.stu 是每个线程的局部变量，
    可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
    :param name:
    :return:
    '''
    tlocal.stu = name
    getStuInfo()

def getStuInfo():
    name = tlocal.stu
    print("thread: %s , name: %s"%(threading.current_thread().name,name))

th1 = threading.Thread(target=doThread,args=("jack",))
th2 = threading.Thread(target=doThread,args=("tom",))
th1.start()
th2.start()
th1.join()
th2.join()