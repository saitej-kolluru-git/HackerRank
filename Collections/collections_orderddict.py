
temp={}
d=OrderedDict
for i in range(int(input())):
    *name,price=input().split()
    key=' '.join(name)
    temp.setdefault(key,[])
    temp[key].append(int(price))

for i in temp.keys():
    print(i,sum(temp[i]),sep=" ")
    
