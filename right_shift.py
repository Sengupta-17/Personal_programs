L=[]
n=int(input("Enter the size of the list: "))
for i in range(0,n):
    x=input("Enter an element: ")
    L.append(x)
t=L[n-1]
for i in range(n-1,0,-1):
    L[i]=L[i-1]
L[0]=t
print('RIght shifted list:',L)