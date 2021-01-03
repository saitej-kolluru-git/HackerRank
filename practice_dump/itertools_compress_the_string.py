from itertools import groupby
n='1222311'
for i,j in groupby(n):
    print(i,list(j))
