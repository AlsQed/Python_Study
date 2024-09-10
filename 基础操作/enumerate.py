# enumerate用法
# enumerate()是python的内置函数
# enumerate在字典上是枚举、列举的意思
# 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
# enumerate多用于在for循环中得到计数
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print (index, item)

# enumerate还可以接收第二个参数，用于指定索引起始值
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1, 1):
    print(index, item)

#  使用enumerate函数删除列表中指定下标元素
lis = ['香蕉','橘子','火龙果','梨','苹果','柚子','csdn']
index_list = [1,2,6]
lis = [n for i, n in enumerate(lis) if i not in index_list]
print('删除后lis的值：%s' %lis)


