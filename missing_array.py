L=[]
n=int(input("Enter a natural number n such that the size of the array is n-1 and there is a missing number between 1 to n(input cannot be 1 and cannot be greater than 10^6): "))
for i in range(0,n-1):
    x=int(input("Enter a number: "))
    L.append(x)
L.sort()
print("The missing number is:",end=" ")
f=0
k=0
i=1
while i<n:
    if L[k]!=i:
        f=1
        break
    k+=1
    i+=1
if f==0:
    print(n)
else:
    print(i)