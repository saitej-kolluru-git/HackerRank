import string
x=string.ascii_lowercase
l=[]
def print_rangoli(size):
    # your code goes here
    for i in range(size):
        k="-".join(x[i:size])
        l.append((k[::-1]+k[1:]).center(4*n-3, "-"))
    print("\n".join(l[:0:-1]+l))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
