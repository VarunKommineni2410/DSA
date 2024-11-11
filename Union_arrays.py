def union(a1,a2):
    l=[]
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i]!=a2[j]:
                l.append(a1[i])
                l.append(a2[j])

    l=list(set(l))        
    print("Union of arrays is: ",l)



a2 = [1, 2, 4, 5, 6]
a1 = [2, 3, 5, 7]

union(a1,a2)
