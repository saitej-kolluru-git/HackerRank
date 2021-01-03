# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a,b=input().split()
for i in range(1,int(b)+1):
    print(*(''.join(list(i)) for i in sorted(list(combinations(sorted(a),i)))),sep="\n")
