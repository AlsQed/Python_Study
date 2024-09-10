# 定义类
# 方法的第一个函数一般是self，表示接受消息的对象本身


class student:
    # 类的属性定义（默认为__init__）
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self._address = address
        # 定义属性前加_为受保护属性（类似private）打印时一般不显示

    # 类的行为
    def study(self, course_name):
        print(f'学生{self.name}正在学习{course_name}')

    def play(self):
        print(f'学生正在玩')

    # 带有双下划线的方法为魔法方法
    # repr可让对象打印时不输出地址而是自己定义的信息
    def __repr__(self):
        return f'{self.name}, {self.age}'

    # 创建与使用对象
    # 此为未定义类属性时所用定义对象的方式
    # stu1 = student()
    # #stu1为student方法定义对象
    # stu1.study('sd')
# 定义类中的对象应不与类的定义的排头对齐
stu2 = student('asdv', 21, 'sh')
stu2.study('sdf')

# 此时打印对象会打印对象的地址
# print((stu2))

print((stu2))   
