a=[1,80,2,3,498,58,6,7]
b=[]
print("Reverse: ",end=" ")

for i in range(len(a)):
   b.append(a[len(a)-i-1])

print(b)