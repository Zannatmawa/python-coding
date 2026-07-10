n = int(input("Enter the number of elements: "))

total = 0

for i in range(n):
    num = int(input("Enter a number: "))
    total += num

average = total / n

print("Average =", average)