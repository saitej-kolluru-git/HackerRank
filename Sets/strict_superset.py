# Enter your code here. Read input from STDIN. Print output to STDOUT
setA=set(map(int,input().split()))
k=[]
for i in range(int(input())):
    k.append(setA.issuperset(set(map(int,input().split()))))
print(all(k))
