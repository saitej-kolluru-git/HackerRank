# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    n,setA=int(input()),set(map(int,input().split()))
    m,setB=int(input()),set(map(int,input().split()))
    print(setA.issubset(setB))
