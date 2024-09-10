name = 'a'
list = [1 , 2 , 3 , 4 , 5 , 6]


# 全局变量

def func1() :
    print(name)
    print(list)


# 函数可调用全局变量

def func2() :
    s = 'b'
    s += 'cc'
    list.append(7)
    print(s)
    print(list)


# 此处s为局部变量，可在函数内部修改
# 但不可直接修改全局变量

def func3() :
    global name
    name += 'AA'
    print(name)
    print(list)


# 使用global可以在函数中改变全局变量
# global使用一般用于不可变变量
# 当变量为可变形式时（如list）则无需global

func1()
func2()
func3()
