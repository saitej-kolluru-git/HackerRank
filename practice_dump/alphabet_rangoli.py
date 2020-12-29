import string
x=string.ascii_lowercase
l=[]
print(x)
n=5
for i in range(n):
    k='-'.join(x[i:n])
    print((k[::-1]+k[1:]).center(4*n-3, "-"))
    l.append((k[::-1]+k[1:]).center(4*n-3, "-"))

print(l)
print('\n'.join(l[::-1]+l))
