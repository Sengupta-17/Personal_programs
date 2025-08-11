str1=input("Enter a senetence:")
count=0
l=len(str1)
for i in str1:
    if i.isspace():
        count=count+1
noc=l-count
print("Number of characters in the sentence is:",noc)