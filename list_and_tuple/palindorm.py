#write a program to check if a list contain a palindrome of elements
# name=str(input("Enter a string:"))

li=[1,2,4]
copy_li = li.copy()
copy_li.reverse()
if(copy_li==li):
    print("palindorm")
else:
    print("not")