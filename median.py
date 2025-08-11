L=[]
n=int(input("Enter size of the array: "))
for i in range(0,n):
    x=int(input("Enter an element: "))
    L.append(x)
L.sort
med=0
if len(L)%2!=0:
    med=L[len(L)//2]
else:
    med=L[len(L)//2]+L[len(L)//2-1]
print("Median of the List=",med)