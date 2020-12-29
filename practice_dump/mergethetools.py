x="AABCAAADA"
start=0
"""
for i in range(len(x)//2):
    temp=x[0+start:3+start]
    print(''.join(sorted(set(temp),key=temp.index)))
    start+=3
"""
for j in x[0+start:3+start]:
    print(j)
    start+=3
    
