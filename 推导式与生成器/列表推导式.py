# 1.列表推导式：格式：表达式 for 变量 in 旧列表 或者【表达式for 变量in 旧列表if条件】
names = ['aaa','bbb','ccc','dd','ee']
result = [name for name in names if len(name)>=3]
print(result)

# 将1-100之间能被3整除，组成一个新的列表
newlist = [i for i in range(1,100) if i % 3 == 0]
print(newlist)

list1 = [[1,2,3],[4,5,6],[7,8,9]]
newlist1 = [i[-1] for i in list1]
print(newlist1)

# if薪资大于5000加200，低于等于5000加500
dict1 = {'name':'tom','salary':5000}
dict2 = {'name':'tommy','salary':6000}
dict3 = {'name':'sam','salary':4000}
list2 = [dict1,dict2,dict3]

newlist2 = [name['salary']+200 if name['salary']>5000 else name['salary']+500 for name in list2]
print(newlist2)