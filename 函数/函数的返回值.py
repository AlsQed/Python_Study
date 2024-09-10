def add1(a,b):
    res = a + b
    print(res)
    return "aaa"
x = add1(2,4)
print(x)
def add2(a,b):
    res = a+b
    print(res)
    return "aaa",2131,'sad '
y = add2(3,6)
print(y)
# return后面也可以是多个参数，如果是多个参数则底层会将多个参数先放在一个元组中,将元组作为整体返回
x,y,z=add2(4,5)
print(x,y,z)
# 接收的时候也可以是多个,但返回值数目与变量数需要对应
