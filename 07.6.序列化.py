# coding=utf-8

import json

class person(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
# 序列化中的错误： TypeError: Object of type 'person' is not JSON serializable
def person2dict(p):
    return {"name":p.name,"age":p.age,"score":p.score}

print("======序列化对象，将对象转为JSON格式=====")
jack = person("jack",18,{"math":90,"science":80})
'''
``default(obj)`` is a function that should
 return a serializable version of obj
'''
json1 = json.dumps(jack,default=person2dict)
print("class对象序列化为json字符串1: ",json1)
json2 = json.dumps(jack,default=lambda obj:obj.__dict__)
print("class对象序列化为json字符串2: ",json2)

print("=========反序列化，将JSON字符串转为clazz对象=========")
json2 = '{"name": "jack", "age": 18,"score":"{\'math\':90,\'science\':80}"}'
def json2object(j):
    return person(j["name"],j["age"],j["score"])

obj1 = json.loads(json2, object_hook=json2object)
print("json字符串反序列化为class对象：",type(obj1.score))
