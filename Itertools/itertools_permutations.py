# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a,b=input().split()
print(*(''.join(list(i))  for i in sorted(list(permutations(a,int(b))))),sep="\n")
