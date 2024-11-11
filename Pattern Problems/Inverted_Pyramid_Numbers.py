"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

"""

n=inp=5

i=1
while i<=inp:
    for num in range(n):
        print(i,end=" ")
    print()
    i=i+1
    n=n-1
