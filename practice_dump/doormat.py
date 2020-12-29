n,m=9,27
k=[]
ch='.|.'
for i in range(n//2):
    #print((ch*(2*i+1)).center(m,'-'))
    print(ch*(2*i+1))

dm=[(ch*(2*i+1)).center(m,'-') for i in range(n//2)]
print(dm)
print(dm[::-1])

print('\n'.join(dm+['welcome'.center(m,'-')]+dm[::-1]))

k,l=map(int,input().split())
