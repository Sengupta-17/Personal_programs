L=[]
n=int(input("Enter the size of the array:"))
for i in range(0,n):
    x=int(input('Enter an integer:'))
    L.append(x)
inv_count=0
for i in range(0,n):
    for j in range(i+1,n):
        if L[i]>L[j]:
            inv_count+=1
print("Inversion count of the array is:",inv_count)