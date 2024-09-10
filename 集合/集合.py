set1 = {1,2,3,4,3,3,2,1}
print(set1)
print(len(set1))
# 集合的性质
# 无序，互异，确定
# 可变无序数据集

set2 = set('hello')
print(set2)
# 集合的创造器语法

set3 = [1,2,3,4,3,2,1]
set4 = set(set3)
print(set4)
# 将列表转为集合

set5 = {num for num in range(1,20) if num % 3 == 0 or num % 5 == 0}
print(set5)
# 集合的构造性语法

for elem in set5:
    print(elem)
# 循环遍历