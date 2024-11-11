def MHT(a,k):
    n=[]
    l=len(a)
    print(a)

    for j in range(k-1):
        n.append(a[j]+k)
    for m in range(k-1,l):
        n.append(a[m]-k)

    print(n)
    print("Maximum diff: ",(n[-1])-(n[0]))

k=3
a=[3,9,12,16,20]
MHT(a,k)