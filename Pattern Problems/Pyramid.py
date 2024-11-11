#   *  
#  * *
# * * *

for i in range(4):
    if i==1:
        print(" "*(4-i-1),end="")
        print("*")
    else:
        print(" "*(4-i-1),end="")
        print("* "*i,end=" ")
        print()
        
    