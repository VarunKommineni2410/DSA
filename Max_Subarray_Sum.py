def sub_arrays (a):
    b=[]
    c=[] 
    for i in range(len(a)):
        
        for j in range(len(a)-i):
            b.append(a[j+i])
            print(b)
            s=sum(b)
            c.append(s)

        b=[]   
     
    print()
    print("Sums are: ",c)
    c.sort()
    print("Sorted: ",c)
    print("Max sum: ",c[-1])

a = [1,2,-3]
sub_arrays(a)