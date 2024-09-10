import time
def decorator(a):
    def wrapper(*args):
        print('checking')
        time.sleep(1)
        print('done')
        a(*args)
    return wrapper

@decorator
def f1(n):
    print('f1',n)

@decorator
def f2(name,age):
    print('f2',name,age)

f1(2)
f2('as',12)