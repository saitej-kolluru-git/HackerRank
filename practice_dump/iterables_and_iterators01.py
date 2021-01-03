from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
F = list(filter(lambda C: 'a' in C, C))
print(F)
