#Initializing the first two terms of the sequence
a,b=0,1
count=0
#iterating to print the fibonacci sequence for the first 13 terms
while count<13:
    #printing the current term
    print(a,end=" ")
    c=a+b
    #updating values of a and b
    a=b
    b=c
    count+=1