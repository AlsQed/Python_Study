def add(a,b=10,c=7):
    print(a,b,c)
    r=a+b+c
    print(r)
add(1)
# 默认值可改变
add(1,4)
# 只给关键字赋值
add(1,c=4)