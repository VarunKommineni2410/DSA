a=[1,80,2,3,498,58,6,7]
min=a[0]
max=a[0]

for i in range(1,7):
        if a[i]<min:
            min=a[i]
        if a[i]>max:
            max=a[i]
       


print("min: ",min)
print("max: ",max)
