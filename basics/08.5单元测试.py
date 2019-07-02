# coding=utf-8

import unittest

class MyTest(unittest.TestCase):

    #在每调用一个测试方法之前执行
    def setUp(self):
        print("====setup====")
    # 在每调用一个测试方法之后执行
    def tearDown(self):
        print("====teardown====")

    #测试方法必须以test开头
    def testItem(self):
        l = [1,2,3]
        self.assertEqual(l[0],l[1])
    #运行单元测试
    if __name__=='__main__':
        unittest.main()