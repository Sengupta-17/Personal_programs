t=()
n=int(input("Enter the size of the tuple: "))
i=1
while i<=n:
    x=input("Enter an element: ")
    t=t+(x,)
    i+=1
print("Created Tuple:",t)