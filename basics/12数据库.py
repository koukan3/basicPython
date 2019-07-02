#coding:utf-8
import pymysql

# pymysql.connect(host="",port=3306)
conn=pymysql.connect("localhost",'root','123123',"test")

cursor= conn.cursor()

cursor.execute("select count(*) from emp")

# all=cursor.fetchall()
# print(all)

print(cursor.fetchone())