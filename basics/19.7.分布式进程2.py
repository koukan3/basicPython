#-*- coding:utf-8 -*-

from multiprocessing.managers import  BaseManager
import random,queue

print("===========分布式进程：worker进程=================")
# 进程1 发送数据 >>>>> 进程2 接收数据 >>>>> 进程2对接收的数据进行处理并发送 >>>>> 进程1 接收处理过的数据
class QueueManager(BaseManager):
    pass
# 创建队列 并注册到网络上
QueueManager.register("getSendQueue")
QueueManager.register("getReceiveQueue")

#连接到服务进程所在的服务器
server_ip='127.0.0.1'
print("start connecting to server[%s]"%server_ip)
manager = QueueManager(address=(server_ip,5555),authkey=b'key')
manager.connect()

#通过网络获取发送和接收队列
sendQueue = manager.getSendQueue()
receiveQueue = manager.getReceiveQueue()

for i in range(10):
    try:
        data = sendQueue.get()
        print("get data[%d] and deal with it..."%data)
        dealJob = 'deal with data %d * %d = %d'%(data,data,data*data)
        #处理后发送出去
        receiveQueue.put(dealJob)
    except queue.Empty:
        print("==== queue is empty ====")

#结束
print("workers exist.")
