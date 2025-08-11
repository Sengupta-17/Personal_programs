str1=input("Enter a word :")
l=len(str1)
if l%2!=0:
    print("It is not a symmetric word")
else:
    str2=str1[:l//2]
    str3=str1[l//2:l]
    if str2==str3:
        print("It is a symmetric word")
    else:
        print("It is not a symmetric word")
str4=""
for i in str1:
    str4=i+str4
if str4==str1:
    print("It is a palindrome word")
else:
    print("It is not a palindrome word")