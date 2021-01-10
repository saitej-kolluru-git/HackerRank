x,y=int(input()),int(input())
for i in range(1):
    s=input().split()
    l=round(len(s)/3)
    if(s[0:l]==s[-l:][::-1]):
        print(True)
    else:
        print(False)
