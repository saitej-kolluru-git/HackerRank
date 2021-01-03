from itertools import product
a=[1,2]
b=[3,4]
c=[5,6]
print(list(product(a,repeat=2)))
print(list(product(a,b)))
print((str(list(product(a,b,c)))[1:-1]).strip(","))
print(*product(a,b))
