if __name__ == '__main__':
    N = int(input())
    list_ops=[]
    for i in range(N):
        
        #it splits the input based on space and saves the data in formate of list
        temp=input().split()
        
        #tuple(map(int,temp[1:]))
        if (temp[0]!='print'):
            eval("list_ops.{a}{b}".format(a=temp[0], b=tuple(map(int,temp[1:]))))
        else:
            print(list_ops)
            
