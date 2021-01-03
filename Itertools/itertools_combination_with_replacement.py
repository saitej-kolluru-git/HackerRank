# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
a,b=input().split()
print(*(''.join(list(i)) for i in sorted(list(combinations_with_replacement(sorted(a),int(b))))),sep="\n")
