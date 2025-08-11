L=[]
n=int(input("Enter the size of the list: "))
for i in range(0,n):
    x=int(input("Enter an element: "))
    L.append(x)
f=0
sum1=0
sum2=0
for i in range(0,n):
    sum1=0
    for j in range(i,n):
        if sum1+L[j]<=sum2:
            break
        else:
            sum1=sum1+L[j]
    if sum1>sum2:
        sum2=sum1
if sum2==0:
    sum2=max(L)
print("Largest sum of contigious subarray=",sum2)