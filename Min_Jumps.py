def MJ(a):
    l=len(a)
    j=a[0]
    c=1
    if a[0]==0:
        return print("Not possible")
    
    for i in range(l):
        c=c+1
        print(a[j],len(a[j:]))
        if a[j]>=len(a[j:]):
            break
        j=j+a[j]
        
        
        
    print("Min Jumps: ",c)

a=[3, 4, 3, 2, 6, 7]
MJ(a)