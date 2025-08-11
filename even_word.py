str1=input("Enter a sentence: ")
z=str1.split()
print("The even length words are: ")
for i in z:
    if len(i)%2==0:
        print(i,end=" ")