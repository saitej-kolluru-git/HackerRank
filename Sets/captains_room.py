# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=int(input()),input().split()
single,repeat=set(),set()
for i in m:
    if i in single:
        repeat.add(i)
    else:
        single.add(i)
print(list(single.difference(repeat))[0])
