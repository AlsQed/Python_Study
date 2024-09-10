# 创建一个空集合
set1 = set()

# 通过add，update添加元素
set1.add(1)
set1.update({12,34,65,6,45})
print(set1)

# 通过diacard方法删除元素
set1.discard(45)
print(set1)

# 通过remove方法删除元素
# 建议先检查元素是否存在，否则会引发异常
if 12 in set1:
    set1.remove(12)
print(set1)

# pop方法可以随机删除一个元素并返回
print(set1.pop())

# clear方法清空整个集合
set1.clear()
print(set1)

# isdisjoint方法用于判断两个集合是否有相同元素
set2 = {'sd','df','fg'}
set3 = {'sd','cv','fg'}
set4 = {'we','er','rt'}
print(set2.isdisjoint(set3))
print(set2.isdisjoint(set4))