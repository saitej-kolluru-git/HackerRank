# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
x=deque()
for i in range(int(input())):
    temp=input().split()+[""]
    eval("x.{0}({1})".format(temp[0],temp[1]))
print(*x,sep=" ")
