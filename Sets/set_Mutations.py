# Enter your code here. Read input from STDIN. Print output to STDOUT
n,setA=int(input()),set(map(int,input().split()))
for i in range(int(input())):
    temp=input().split()
    eval("setA.{}({})".format(temp[0],set(map(int,input().split()))))
print(sum(setA))
