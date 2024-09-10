# 函数A是作为参数出现的(函数B就接收函数A作为参数)
# 要有闭包的特点

def test() :
    print("----test----")

def func(a) :
    print(a)
    a()
    print('--func--')

t = test
func(t)

# 函数调用函数
print('------------------')


# 装饰器定义及使用
def decorate(a) :
    print('加载wrapper')
    def wrapper() :
        a()
        print('add door')
        print('add kitchen')
    print('使用wrapper')
    return wrapper

@decorate
def house() :
    print('house')
# 当被装饰函数还未被调用时执行装饰器decorate这个函数本身
print('----------------------')

# house被装饰函数
# 将被装饰函数作为参数传给装饰器decorate
# 执行decorate函数
# 将返回值又赋值给house

# 返回的地址中有wrapper的地址
print(house)
print('----------------------')
house()

