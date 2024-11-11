a=[9, 8, 7, 6, 4, 2, 1, 3]
a1=[]

for i in range(len(a)):
    if i==0:
        a1.append(a[len(a)-1])
    if i<len(a)-1:
        a1.append(a[i])

print("cylinder: ",a1)