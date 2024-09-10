# 列表定义
# 可变有序数据集
name_list1 = ['sd','df','fg']
print(name_list1)


# 数据添加
# 在指定位置添加数据 .insert
name_list1.insert(0,'ad')
print(name_list1)
# 在末尾增加一个数据 .append
name_list1.append('sc')
print(name_list1)
# 将列表2的数据添加到表1 .extend
name_list2 = ['er','yh','jk']
name_list1.extend(name_list2)
print(name_list1)


# 数据修改
name_list1[1] = 'vb'
print(name_list1)


# 数据删除
del name_list1[0]
print(name_list1)
# 删除第一个出现的指定数据 .remove
name_list1.remove('sc')
print(name_list1)
# 删除末尾数据 .pop
name_list1.pop(3)
print(name_list1)
name_list1.pop()
print(name_list1)


# 清除整个列表
name_list3 = ['zx','cv','bn']
name_list3.clear()
print(name_list3)

# 统计
# 列表长度 len
# 数据在列表中出现的次数
print(len(name_list1))
name_list4 = ['sd','sd','xc','xc','xc']
print(name_list4.count('sd'))
print(name_list4.count('xc'))


# 排序
# 升序 .sort
name_list1.sort()
print(name_list1)
# 降序
name_list1.sort(reverse=True)
print(name_list1)
# 逆序
name_list1.reverse()
print(name_list1)
# 定义排序准则
def key1(x):
    return (x*x-4*x+4)
s = [1,2,3,4,5]
print(sorted(s,key=key1,reverse = True))

# 循环取值
for i in name_list1:
    print(i)
    print(type(i))

a = {1:[1,2,3]}
b = a
print(b)
c = {2:[1,2,3]}
b = c.copy()
b[2].append(8)
print(b)
import copy
b = copy.deepcopy(a)

