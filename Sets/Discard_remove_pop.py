n,setA=int(input()),set(map(int,input().split()))
for i in range(int(input())):
    eval("setA.{0}({1})".format(*input().split()+[""]))
print(sum(setA))
