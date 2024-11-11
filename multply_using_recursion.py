
def mul(a,b):

    k=max(a,b)
    l=min(a,b)

    if (k | l)==0:
        return 0 

    if l==1:
        return k
    
    return (k)+(mul(k,l-1))

print(mul(3,99))