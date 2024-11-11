a=[1,2,3,4,2,1]
visited = [False] * len(a)

for i in range(len(a)):
    if (visited[i] == True):
        continue
    c = 0
        
    for j in range(len(a)):
        if (a[i] == a[j]):
            visited[j] = True
            c += 1
            
    print(a[i]," = ",c)