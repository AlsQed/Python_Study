# 简化函数定义部分
# 格式:lambda

# def add(a, b):
#     s = a + b
#     return s

s = lambda a, b: a + b
print(s)
# s本身为函数
print(s(1, 2))


# 匿名函数可作为参数
def add(a, b, func):
    print(func)
    print(a, b)
    res = func(a, b)
    print(res)

 # 调用add
add(1, 2,    lambda a, b: a + b)
