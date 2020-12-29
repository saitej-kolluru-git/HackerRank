# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
DoorMat = [('.|.'*(2*i+1)).center(m,'-') for i in range(n//2)]
print('\n'.join(DoorMat+['WELCOME'.center(m,'-')]+DoorMat[::-1]))
