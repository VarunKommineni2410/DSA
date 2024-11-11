def sort(a):
    l = 0
    h = len(a) - 1
    m = 0
    
    while m <= h:

        if a[m] == 0: 
            a[l], a[m] = a[m], a[l]
            l= l + 1
            m= m+ 1
      
        elif a[m] == 1:
            m = m + 1
      
        else:
            a[m], a[h] = a[h], a[m]
            h = h - 1
    return a
 

a = [0, 1, 1, 0, 2, 2, 1, 2, 0, 0, 0, 1]
a = sort(a)
print(a)