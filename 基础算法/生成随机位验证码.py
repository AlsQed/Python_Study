import random
# n为位数
def generate_code(n):
    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(n):
        ran = random.randint(0,len(s))
        code += s[ran]
    return code
print(generate_code(4))