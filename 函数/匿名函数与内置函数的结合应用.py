list1 =[2,3,4,5,6]

m=max(list1)

list2=[{'a':2,'b':3},{'a':4,'b':5},{'a':6,'b':7},{'a':8,'b':9}]

# n=max(list2)
# 如果使用max函数比较会因为字典本身无法使用比较符号而报错

m=max(list2,key=lambda x:x['a'])

# 使用lambda函数取key=a的值,max函数比较得出字典中该键对应最大值
# 其中,max函数中key必须等于一个函数
# max(iterable, *[, default = obj, key = func]) -> value
# max(arg1, arg2, *args, *[, key = func]) -> value

print(m)