set1 = {1,3,5}
set2 = {1,3,5,7,9}
set3 = set2
# <表示真子集，<=表示子集
print(set1<set2,set1<=set3)
print(set2<set3,set2<=set3)

# 相反的符号也成立
print(set2>set1,set2>=set1)