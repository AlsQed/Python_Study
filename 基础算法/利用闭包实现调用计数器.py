def generate_counter():
    count=[0]
    def add():
        count[0]=count[0]+1
        s=count[0]
        print('当前为第{}次调用'.format(count[0]))
        return s
    return add
counter = generate_counter()
counter()
counter()
counter()
C = counter()
print(C)