L=[]
n=int(input("Enter the size of the array: "))
for i in range(0,n):
    x=int(input("Enter an element: "))
    L.append(x)
count=0
L.sort()
f=0
maj_elm=0
for i in range(0,n):
    if i==0:
        count=L.count(L[i])
    if L[i]==L[i-1]:
        continue
    else:
        count=L.count(L[i])
    if count>n//2:
        f=1
        maj_elm=L[i]
        break
    count=0
if f==1:
    print("Majority Element:",maj_elm)
else:
    print("-1")