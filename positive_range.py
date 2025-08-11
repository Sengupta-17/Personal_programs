#declaring empy list
list1=[]
#taking input from user for list size
n=int(input("Enter the size of the list:"))
#accepting integers into the list
for i in range(n):
    x=int(input("Enter any positive or negative integer value:"))
    #appending value to list1
    list1.append(x)
#creating empty output list
list2=[]
#extracting positive integers from list1 to output list2
for i in list1:
    if i>=0:
        list2.append(i)

print(list2)