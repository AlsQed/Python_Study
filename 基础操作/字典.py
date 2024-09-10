#字典定义
xiaoming = {"name" : "ALS",
            "age" : 9,
            "sex" : True,
            }
print(xiaoming)
print(type(xiaoming))
#前为键（key）后为值（value）
# 字典的方法

print(len(xiaoming))
# 获取长度

print(xiaoming.keys())
# 所有键列表

print(xiaoming.values())
# 所有值列表

print(xiaoming.items())
# 所有元组（key，value）列表

print(xiaoming["name"])
print(xiaoming.get("name"))
# 字典中取值

del xiaoming["sex"]
print(xiaoming)
xiaoming.pop("age")
print(xiaoming)
# 字典中删除指定键对

xiaoming.popitem()
# 随机删除一个键值对

xiaoming['height'] = 180
print(xiaoming)
# key存在修改数据，key不存在新建键值对
xiaoming.setdefault('height',181)
xiaoming.setdefault('address','sd')
print(xiaoming)

