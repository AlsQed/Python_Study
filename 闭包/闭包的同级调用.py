def func():
    a = 100
    def innerfunc1():
        b=10
        s=a+b
        print(s)
    def innerfunc2():
        innerfunc1()
        print('--->innerfunc2')
        return 'hello'
    return innerfunc2
# 函数调用
f = func()
print(f)
# 指向地址
f()
# 调用函数
ff = f()
print(ff)
# 只有变量接住return值才能打印