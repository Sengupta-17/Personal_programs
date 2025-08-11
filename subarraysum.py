L=[]
n=int(input("Enter the size of the list: "))
for i in range(0,n):
    x=int(input("Enter an element: "))
    L.append(x)
f=0
sum_inp=int(input("Enter the sum to be checked: "))
sum1=0
index_1=0
index_2=0
for i in range(0,n):
    sum1=0
    for j in range(i,n):
        sum1=sum1+L[j]
        if sum1==sum_inp:
            index_1=i+1
            index_2=j+1
            f=1
            break
    if f==1:
        break
if f==1:
    print(index_1,index_2)
else:
    print("-1")