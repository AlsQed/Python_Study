# 温度转换
# from decimal import Decimal
# t = input("输入温度:")
# T = float(t)
# C = (T - 32) / 1.8
# F = T * 1.8 + 32
# print("若输入华氏度,则当前为摄氏度C"+str('%.2f'%C))
# print("若输入摄氏度,则当前为华氏度F"+str('%.2f'%F))
# ----------------------------------------------------------------------------------------------------------------------
# n,a=input().split(",")
# r = 1
# for i in range(1,int(n)+1):
# 	r*=i
# for k in range(1,int(n)):
#     ak = int(a)**k
#     aj = int(a)**(k+1)
#     if r%ak == 0 and r%aj != 0:
#         print(k)
#         break
# ----------------------------------------------------------------------------------------------------------------------
# 正方形
# import turtle as t
# t.fd(200)
# t.seth(90)
# t.fd(200)
# t.seth(180)
# t.fd(200)
# t.seth(270)
# t.fd(200)
# t.mainloop()
# ----------------------------------------------------------------------------------------------------------------------
# # 渐变的圆
# import turtle as t
# t.screensize(1800,800)
# t.color('blue')
# t.begin_fill()
# t.fillcolor('yellow')
# n = int(input())
# for i in range(3,n):
#     t.circle(50,steps = i)
#     t.fd(100)
# t.circle(50)
# t.end_fill()
# t.mainloop()
# ----------------------------------------------------------------------------------------------------------------------
# 身份证号基本信息
# n = input()
# l = []
# for i in range(0,len(n)):
#     l.append(n[i])
# print("出生年月日为:"+l[6]+l[7]+l[8]+l[9]+"年"+l[10]+l[11]+"月"+l[12]+l[13]+"日")
# s = int(l[16])
# if s%2 == 1:
#     print('性别：男')
# else:
#     print('性别：女')
# ----------------------------------------------------------------------------------------------------------------------
# 三次方格式化
# a = eval(input())
# print("{:-^20}".format(pow(a,3)))
# ----------------------------------------------------------------------------------------------------------------------
# 数值运算
# T = input()
# print('{:.2f}'.format(eval(T)))
# ----------------------------------------------------------------------------------------------------------------------
# 鸡兔同笼
# def app(a, b):
#     x = (4 * a - b) / 2
#     if a != 0 and (4 * a - b) % (x * 2) == 0:
#         y = a - x
#         if x < 0 or y < 0:
#             print("{}只动物{}条腿的情况无解".format(a, b))
#         else:
#             print("鸡有{}只，兔有{}只".format(int(x), int(y)))
#     else:
#         print('Data Error')
#
# a,b = input().split(" ")
# a = int(a)
# b = int(b)
# app(a, b)
# ----------------------------------------------------------------------------------------------------------------------
# 汇率兑换
# from decimal import Decimal
# def exchange1():
#     while True:
#         print("请输入金额:")
#         t = input()
#         T = float(t)
#         Y = T*6
#         D = T/6
#         print("若输入人民币,则当前为美元"+str('%.2f'%D))
#         print("若输入美元,则当前为人民币"+str('%.2f'%Y))
#         c = input("退出请按q")
#         if c == "q":
#             break
# ----------------------------------------------------------------------------------------------------------------------
# import time
# a = 8
# for i in range(20):
#     a=a*8
# time.sleep(2)
# print(a)
# ----------------------------------------------------------------------------------------------------------------------
# 复杂度不合格
# def findSmallestSetOfVertices(n, edges):
#     start = []
#     finsh = []
#     for i in range(0,len(edges)):
#         start.append(edges[i][0])
#         finsh.append(edges[i][1])
#     start = list(set(start))
#     finsh = list(set(finsh))
#     index_list = []
#     for i in range(len(start)):
#         for j in range(len(finsh)):
#             if start[i] == finsh[j]:
#                 index_list.append(i)
#     start = [n for i,n in enumerate(start) if i not in index_list]
#     return start
# ----------------------------------------------------------------------------------------------------------------------
# def findSmallestSetOfVertices(n, edges):
#     endSet = set(y for x, y in edges)
#     ans = [i for i in range(n) if i not in endSet]
#     return ans
# print(findSmallestSetOfVertices(4,[[2,0],[3,1],[0,3]]))
# ----------------------------------------------------------------------------------------------------------------------
# 列表实现剪刀石头布
# import random
# ls = ["石头","剪刀","布"]
# player = random.choice(ls)
# computer = random.choice(ls)
# print("玩家出：",player)
# print("电脑出：",computer)
# if ((player == "石头" and computer == "剪刀")
#         or (player == "剪刀" and computer == "布")
#         or (player == "布" and computer == "石头")):
#     print("玩家胜利")
# elif player == computer:
#     print("平局")
# else:
#     print("电脑胜利")
# ----------------------------------------------------------------------------------------------------------------------
# 字典添加元素
# dict1 = {'赵广辉':'13299887777','特朗普':'814666888','普京':'522888666','吴京':'13999887777'}
# k=input('key:')
# v=input('value:')
# ls = []
# ls.append(dict1.keys())
# for i in ls:
#     if k == i:
#         print('已存在')
#     else:
#         dict1.setdefault(k,v)
# print(dict1.items())
# ----------------------------------------------------------------------------------------------------------------------
# 求平均成绩
# i = (input().split(' '))
# m = int(i[1])
# n = int(i[0])
# s = []
# for i in range(m):
#     print('第{}行:'.format(i+1))
#     for j in range(n):
#         s.append(input().split(' '))
#         print(sum(s)/len(s))
# ----------------------------------------------------------------------------------------------------------------------
# class B:
#     def handle(self):
#         print("i am b")
#
# class A(B):
#     def handle(self):
#         super().handle()
#         print("i am a")
#
# a = A()
# ----------------------------------------------------------------------------------------------------------------------
# def num(num):
#     count=0
#     while(num>0):
#         if num%2==1:
#             num=num-1
#         else:
#             num=num/2
#         count=count+1
#     return count
# print(num(14))
# ----------------------------------------------------------------------------------------------------------------------
