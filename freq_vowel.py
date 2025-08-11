str1=input("Enter a sentence: ")
count=0
freq=0
str1=str1.upper()
for i in range(65,91):
    freq=0
    if chr(i)=='A' or chr(i)=='E' or chr(i)=='I' or chr(i)=='O' or chr(i)=='U':
        for j in str1:
            if chr(i)==j:
              freq=freq+1
        print("Frequency of",chr(i),"is=",freq)
    count=count+freq
print("Total number of vowels is:",count)