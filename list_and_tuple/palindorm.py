#write a program to check if a list contain a palindrome of elements
# name=str(input("Enter a string:"))

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")