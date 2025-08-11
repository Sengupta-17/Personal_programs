L=[]
n=int(input("Enter the size of the list: "))
for i in range(0,n):
    x=int(input("Enter an element: "))
    L.append(x)
L2=[]
for i in L:
    if i not in L2:
        L2.append(i)
print("New list with duplicates remoced:",L2)