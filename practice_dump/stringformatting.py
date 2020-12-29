n=17
for i in range(1,n+1):
    #z="{0:b}".format(n)
    print("{0:{1}d} {0:{1}o} {0:{1}x} {0:{1}b}".format(i,len("{0:b}".format(n))))
    
