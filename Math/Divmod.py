# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=int(input()),int(input())
print(*(divmod(n,m)),sep="\n")
print(divmod(n,m))
