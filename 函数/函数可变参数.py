a = [1,2,3]
b = [*a,4,5,6]
# ----------------- 输出结果 -----------------
# [1, 2, 3, 4, 5, 6]
# ----------------- 总结 -----------------
# 将a的内容移入（解包）到新列表b中。
# *args 表示任何多个无名参数， 他本质上是一个 tuple
# ** kwargs 表示关键字参数， 它本质上是一个 dict
# 同时使用时必须要求 *args 参数列要在** kwargs 前面 [因为位置参数在关键字参数的前面。]
def test_var_args(f_arg, *args):
    print("first normal arg:",f_arg)
    for arg in args:
        print("another arg through *argv:",arg)
test_var_args('yasoob','python','eggs','test')


def print_func(*args):
    print(type(args))
    print(args)
print_func(1,2,'python希望社',[])

# 在打印函数的参数处，新增 x 和 y 变量
def print_func(x,y,*args):
    print(type(x))
    print(x)
    print(y)
    print(type(args))
    print(args)
print_func(1,2,'python希望社',[])

# 将 *args 放在参数最前面
# def print_func(*args,x,y):
#     print(type(x))
#     print(x)
#     print(y)
#     print(type(args))
#     print(args)

# 若 *args 不是在最后，则需要在参数传入时，明确定义 *args后面的变量参数名，如下：

# 改正的代码
def print_func(*args,x,y):
    print(type(x))
    print(x)
    print(y)
    print(type(args))
    print(args)
print_func(1,2,'python希望社',[],x='x',y='y')

# **kwargs允许你将不定长度的 【键值对 key-value 】，作为参数传递给一个函数
def print_func(**kwargs):
    print(type(kwargs))
    print(kwargs)

print_func(a=1, b=2, c='呵呵哒', d=[])

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))
greet_me(name="yasoob")

# arg,*args,**kwargs ,三者是可以组合使用的
# 需要按照：
# arg,*args,**kwargs 作为函数参数的顺序
def print_func(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)

print_func(1, 2, 3, 4, y=1, a=2, b=3, c=4)

# 使用*args 和 **kwargs 来调用一个函数
def test_args_kwargs(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)

# ------------------
args = ("two",3,5)
test_args_kwargs(*args)
# 此处元组内数量应对应

kwargs = {"arg3": 3,"arg2":"two","arg1":5}
test_args_kwargs(**kwargs)


