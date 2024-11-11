s=int(input("Enter size: "))
      
a=[int(n) for n in input().split(" ",s-1)]

b=a.copy()
b.sort()

print("Unsorted: ",a)
print("Sorted: ",b)

l=[]
for i in range(len(a)):
    if a[i]==b[i]:
        l.append(i)

print()
print("Unchanged: ",l)
