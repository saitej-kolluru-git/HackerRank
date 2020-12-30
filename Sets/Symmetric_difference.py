# Enter your code here. Read input from STDIN. Print output to STDOUT
n,setA=int(input()),set(map(int,input().split()))
m,setB=int(input()),set(map(int,input().split()))
print(*(i for i in sorted(list(setA.symmetric_difference(setB)))),sep="\n")
