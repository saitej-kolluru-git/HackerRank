# Enter your code here. Read input from STDIN. Print output to STDOUT
temp={}
for i in range(int(input())):
    key=input()
    temp.setdefault(key,[])
    temp[key].append(1)
print(len(temp.keys()))
print(*[sum(temp[i]) for i in temp],sep= " ")
