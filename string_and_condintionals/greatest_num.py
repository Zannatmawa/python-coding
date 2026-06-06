#write a program to find the greatest of 3 numbers entered by the user.

a = int(input("Enter first number to check "))
b = int(input("Enter second number to check "))
c = int(input("Enter third number to check "))

if(a>=b and a>=c):
       print("a is the greatest",a)

elif(b>=c):
 print("b is the greatest",b)
else:
       print("c is the greatest",c)

