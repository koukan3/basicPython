#-*- coding:utf-8 -*-

from multiprocessing.managers import  BaseManager
import random,queue

print("===========分布式进程：master服务进程=================")
'''
Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。
比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，
而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
'''
class QueueManager(BaseManager):
    pass
# 创建队列 并注册到网络上
sendQ = queue.Queue()
receiveQ = queue.Queue()
QueueManager.register("getSendQueue",callable=lambda :sendQ)
QueueManager.register("getReceiveQueue",callable=lambda :receiveQ)

#绑定端口和验证码
manager = QueueManager(address=('',5555),authkey=b'key')
#启动queue队列
manager.start()
#通过网络获取发送和接收队列
sendQueue = manager.getSendQueue()
receiveQueue = manager.getReceiveQueue()

for i in range(10):
    data = random.randint(1000)
    print("put data[%d] in queue..."%data)
    sendQueue.put(data)
for i in range(10):
    r = receiveQueue.get()
    print("receive data[%d] from queue..."%r)
#关闭
manager.shutdown()
print("queue manager shut down.")
