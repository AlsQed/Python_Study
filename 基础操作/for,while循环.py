for i in range(5):
	print(i)


range(5)
[0, 1, 2, 3, 4]
range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(1,11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
range(1,11,2)        ##取出奇数
[1, 3, 5, 7, 9]
range(0,11,2)        ##取出偶数
[0, 2, 4, 6, 8, 10]


# 求1～100内偶数之和
sum = 0
for i in range(2,101,2):
    sum += i
print(sum)


# 求1～100之间所有奇数之和
sum1 = 0
for i in range(1,101,2):
    sum1 += i
print(sum1)


# 求阶乘
num = int(input('请输入一个数字：'))
res = 1
for i in range(1, num + 1):
	res*=i
print('%d的阶乘为：%d' %(num,res))


# 有1，2，3，4四个数字,求这四个数字能生成多少个互不相同且无重复数字的三位数
sum = 0
for i in (1,2,3,4):
    for j in (1,2,3,4):
            for k in (1,2,3,4):
                        if i != j and j!= k and i != k:
                                       sum += 1
print('共有%d种组合' %sum)


# 9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
            print('%d * %d = %d\t' %(i,j,i*j),end='')
    print()


# 输入两个数字
num1=int(input('Num1：'))
num2=int(input('Num2：'))
# 找出两个数中的较小者
min_num = min(num1,num2)
# 确定最大公约数
for i in range(1,min_num+1):
    if num1 % i ==0 and num2 % i ==0:
        max_commer = i
# 求最小公倍数
min_commer =int(num1 * num2)/max_commer
print('%s 和 %s 的最大公约数为%s' %(num1,num2,max_commer))
print('%s 和 %s 的最小公倍数为%s' %(num1,num2,min_commer))

