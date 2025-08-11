s=input("Enter a senetence: ")
z=s.split()
l=len(z)
r=""
for i in z:
    r=r+i.capitalize()+" "
print("Modified sentence: ",r)