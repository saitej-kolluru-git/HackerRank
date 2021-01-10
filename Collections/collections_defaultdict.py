# Enter your code here. Read input from STDIN. Print output to STDOUT
k=list(map(int,input().split()))
temp={}
for i in range(k[0]):
    key=input()
    temp.setdefault(key,[])
    temp[key].append(i+1)

for j in range(k[1]):
    temp1=input()
    if(temp1 in temp.keys()):
        print(*temp[temp1],sep=" ")
    else:
        print("-1")
