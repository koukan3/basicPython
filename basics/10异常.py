#coding:utf-8

import logging

def test1():
    try:
        #f=open("D:/abc.txt","r")
        a=100/0
        print("====try====")
    except (FileNotFoundError ,TypeError,ZeroDivisionError) as ex:
        print(ex)
        #logging模块记录错误信息（错误原因、出错位置）
        logging.exception(ex)
        raise TypeError("我自己抛出的异常")
    finally:
        print("最后都会执行")
test1()
