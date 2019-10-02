#-*- coding:utf-8 -*-
from collections import deque
'''
@file: 2.7.dataStructure-deque.py
@description:
deque双向队列：线程安全，可以快速的从两端添加或删除元素。
【队列的实现】
其他对队列的实现：
1.queue：提供了同步（线程安全）类 Queue、 LifoQueue 和 PriorityQueue，
不同的线程可以利用这些数据类型来交换信息。
2.multiprocessing：实现了自己的 Queue，跟 queue.Queue 类似，是设计给进程间通信用的。
3.asyncio：Python 3.4 新提供的包，里面有 Queue、 LifoQueue、 PriorityQueue 和 JoinableQueue，
为异步编程里的任务管理提供了专门的便利。
4.heapq：heapq 没有队列类，而是提供了 heappush 和 heappop 方法，
让用户可以把可变序列当作堆队列或者优先队列来使用。
'''

dp = deque(range(10),maxlen=10)
print(dp)
#添加
dp.append(10)  #dp.appendleft()
print("尾部追加：",dp)
dp.extend(['a','b','c']) #dp.extendleft()
print("尾部追加多个：",dp)
dp.extendleft([10,20,30])
print("左侧依次添加：",dp)
#旋转
dp.rotate(3)
print("旋转右侧N个元素到左侧：",dp)
dp.rotate(-4)
print("旋转左侧N个元素到右侧：",dp)
#删除:从队列中间删除元素的操作会慢一些，因为它只对在头尾的操作进行了优化。
dp.remove(10)
print("删除第一次出现的某个元素",dp)
del dp[2]
print("删除指定位置上的元素",dp)
print(dp.pop())
print("移除最后一个元素并返回",dp)
#更新
dp[2]=100
#查询
print("查询指定位置的元素：",dp[2])
print("查询指定元素的位置：",dp.index(100))
alist = [e for e in dp]
print("遍历队列：",alist)

