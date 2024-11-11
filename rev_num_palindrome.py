n=8008
l=[]

while n>0:
    k=n%10
    l.append(k)
    n = n // 10
print(l)

c=0

for i in range(len(l)):
    if l[len(l)-1-i]==l[i]:
        c=1
    else:
        c=0

if(c==1):
    print("palindrome")
else:
    print("not palindrome")