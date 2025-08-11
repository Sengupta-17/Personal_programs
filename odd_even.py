L=[]
n=int(input("Enter the size of the list: "))
for i in range(0,n):
    x=int(input("Enter an element: "))
    L.append(x)
L_pos=[]
L_neg=[]
for i in L:
    if i>0:
        L_pos.append(i)
    else:
        L_neg.append(i)
print("List with positive integers:",L_pos)
print("List with negative numbers:",L_neg)