from itertools import combinations
n=int(input())
#k=input().split()
m=int(input())
#print([i  for i in range(1,n+1)])
k=list(combinations([i  for i in range(1,n+1)],m))
t=0
for i in range(len(k)):
    if(k[i][0] in range(1,m+1)):
        t+=1
print("{0:.4f}".format(t/len(k)))

    
