# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n,m=int(input()),map(int,input().split())
counter1=Counter(m)
total=0
for i in range(int(input())):
    temp=list(map(int,input().split()))
    if(temp[0] in counter1.keys() and counter1[temp[0]]>0 ):
        total+=temp[1]
        counter1[temp[0]]= counter1[temp[0]]-1
print(total)
