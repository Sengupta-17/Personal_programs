L=[]
n=int(input("Enter the size of the array: "))
for i in range(0,n):
    x=int(input("Enter a number: "))
    L.append(x)
if L[0]==0:
    print("-1, No jumps achieved!")
else:
    k=0
    jump=0
    f=0
    t=L[0]
    for i in range(0,n):
        t=L[k]
        if t==0:
            print("-1, End not reachable")
            break
        for j in range(0,t):
            k+=1
            if k==n-1:
                jump+=1
                print(jump)
                f=1
        if f==1:
            break
        else:
            jump+=1