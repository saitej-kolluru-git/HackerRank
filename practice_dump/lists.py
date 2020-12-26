n=1
test=[]
for i in range(n):
    temp=input().split()
    if(temp[0]!='print'):
        print(temp[0],int(temp[1:]))
    else:
        print(test)
    
