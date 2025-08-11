str1=input("Enter a string consisting of only valid parenthesis: ")
r=False
for i in str1:
    if i=='(' or i==')':
        if i=='(':
            if ')' in str1:
                r==True
            else:
                r=False
        if i==')':
             if '(' in str1:
                r==True
    if i=='{' or i=='}':
        if i=='{':
            if '}' in str1:
                r==True
            else:
                r=False
        if i=='}':
             if '{' in str1:
                r==True
    if i=='[' or i==']':
        if i=='[':
            if ']' in str1:
                r==True
            else:
                r=False
        if i==']':
             if '[' in str1:
                r==True
if r==True:
    print(r)  
else:
    print(r)