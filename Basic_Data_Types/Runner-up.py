if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr);arr.sort();max_index=arr.index(max(arr))
    if(max_index<0):
        print(arr[0])
    else:
        print(arr[max_index -1])