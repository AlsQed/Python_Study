#错误例子
n1=1.1
n2=2.2
print(n1+n2)

#正确示范
#导入Decimal模块
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

a = 10
b = 4
c = a // b
print(c)
# python中“//”是一个算术运算符，表示整数除法，它可以返回商的整数部分（向下取整）