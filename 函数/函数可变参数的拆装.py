# 接上回可变参数
# 函数参数前的*会拆装输入为元组
def func1(name,*course):
    for i in course:
        print("{} have learnt {}".format(name,i))
course=['c','r','b']
# 若不加*则会将输入作为整体放入元组
func1('A',course)
func1('M',*course)