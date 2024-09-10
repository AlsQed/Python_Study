def func2(b , c) :
    a = 100

    def inner_func2() :
        s = a + b + c
        print(s)

    return inner_func2


# 此时只调用函数是没有值输出的
func2(3,4)
# 将其返回值（即内部函数）赋值给变量后才会生效
ifunc = func2(3,4)
ifunc()

# 当内部函数被定义时会形成单独的内存空间
# 当函数被调用则其单独再开辟一块内存空间调用之前内存空间中的内部函数以及存储变量
# 这使得当以两个不同参数同时调用时参数不会互相干扰
# 当函数后有括号就是调用，当有变量指向其则是将函数运行完的值赋值给变量
ifunc1 = func2(7,8)
ifunc1()

print(ifunc)
print(ifunc1)
# 输出为内存地址