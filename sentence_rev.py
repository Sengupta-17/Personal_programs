str1=input("Enter a sentence: ")
z=str1.split()
l=len(z)
mod=""
for i in z:
    mod=i+" "+mod
print("Reversed sentence is:",mod)