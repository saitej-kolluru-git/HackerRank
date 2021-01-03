# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n=int(input())
j=input().split()
m=int(input())
list1=list(combinations(j,m))
b=list(filter(lambda k: 'a' in k, list1))
print("{0}".format(len(b)/len(list1)))
