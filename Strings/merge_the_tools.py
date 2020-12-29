def merge_the_tools(string, k):
    # your code goes here
    start=0
    for i in range(len(string)//k):
        temp=string[0+start:k+start]
        print(''.join(sorted(set(temp),key=temp.index)))
        start+=k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
