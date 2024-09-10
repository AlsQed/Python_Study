# 元组定义
# 不可变有序数据集
data_1 = {1, 'sd', 1.34}
print(type(data_1))

# 在申明一个元组时，如果元组中的值只有一个，则必须在之后添加一个逗号
data_2 = (1)
print(type(data_2))
data_2 = (1,)
print(type(data_2))

# 统计元组中元素出现的次数 count函数
data = (1, 1, 1, 2, 3, 4, 1,)
print(data.count(1))

# index指当前元素的下标
print(data.index(4))

# 循环遍历
for i in data:
    print(i)

# 元组与列表之间互相转换
print(type(data))
print(type(list(data)))
print(type(tuple(data)))
