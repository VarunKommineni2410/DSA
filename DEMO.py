N=6
arr = [6,0,1,8,0,2] 
nl=[0]*N
j=0
for i in range(len(arr)):
    if arr[i]!=0:
        nl[j]=arr[i]
        j=j+1

print(nl)