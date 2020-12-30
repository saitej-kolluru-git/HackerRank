for i in range(1,5+1):
    #print(*(j for j in range(1,i+1)),"",*[j for j in range(1,i)][::-1],sep="")
    print(((10**i - 1)//9)**2)
    
