import textwrap
x="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
y=int(input())
k=0
for i in range(1,len(x)+1):
    if(i%y==0):
        x=x[0:i+k]+"\n"+x[i+k:]
        k+=1
        
print(x)
yy="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
for line in (textwrap.wrap(yy,width=y)):
    print(line)
tt=textwrap.fill(yy,width=y)
print(tt)
