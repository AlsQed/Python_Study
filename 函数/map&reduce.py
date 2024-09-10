# map(function,iterable,...)
# 第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。
# 把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list。
from 函数.函数定义 import y


def square(x):
    return x ** 2


map(square, [1, 2, 3, 4, 5])
# # 结果如下:
# [1,4,9,16,25]

# 通过使用lambda匿名函数的方法使用map()函数
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

# # 结果如下：
# [3,7,11,15,19]

# 通过lambda函数使返回值是一个元组
map(lambda x, y: (x ** y, x + y), [2, 4, 6], [3, 2, 1])

# # 结果如下
# [(8,5),(16,6),(6,7)]

# 当不传入function时，map()就等同于zip()，将多个列表相同位置的元素归并到一个元组
map(None, [2, 4, 6], [3, 2, 1])

# 结果如下
# [(2,3),(4,2),(6,1)]

# 将元组转换为list

map(int, (1, 2, 3))

# 结果如下：
# [1,2,3]

# 将字符串转换为list

map(int, '1234')

# 结果如下：
# [1,2,3,4]

# 提取字典中的key，并将结果放在一个list中：

map(int, {1: 2, 2: 3, 3: 4})

# 结果如下
# [1,2,3]


from functools import reduce


# reduce()函数的定义：
# 格式：
# reduce(function,sequence,initial_value)
# function:接收一个函数，该函数必须接受两个参数。
# sequence:接收可迭代的类型
# initial_value:默认值，如果提供该值，在第一次运行的时候会以sequence中的第一个元素和initial_value作为参数调用 function，
# 否则会以sequence中的前两个元素作为参数。
# 需要注意的是：reduce()中传入的函数f必须接受两个参数，reduce()对列表中的每个元素反复调用函数f，并返回最终的结果值。
def f(x, y):
    return x + y


a = reduce(f, [1, 2, 3, 4, 5, 6])
print(a)
# >>>21
a = reduce(f, [1, 2, 3, 4, 5, 6], 100)
print(a)
# >>>121

# 统计某字符串出现的次数
from functools import reduce
sentences = ['我今年刚到北京，我去过北京天安门，北京真的是很棒，我想留在北京。 ']
word_count =reduce(lambda a,x:a+x.count("北京"),sentences,0)
print(word_count)

sentences = ['我今年刚到北京，我去过北京天安门，北京真的是很棒，我想留在北京。 ']
print(sentences[0].count("北京"))
