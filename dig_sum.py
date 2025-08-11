str1=input("Enter a sentence with numbers: ")
sum=0
for i in str1:
    if i.isdigit():
        sum=sum+int(i)
print("Sum of the numbers in the sentence is:",sum)