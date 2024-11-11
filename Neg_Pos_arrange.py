a=[-3,2,-8,4,-66,99]


l=0
h=len(a)-1
m=0
while m<=h:
    if a[m]<0:
        a[l],a[m]=a[m],a[l]
        m=m+1
        l=l+1
    elif a[m]>0:
        a[m],a[h]=a[h],a[m]
        h=h-1

print(a)