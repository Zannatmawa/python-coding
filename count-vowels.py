# Write a Python program to count the number of vowels in a given string.
text = "Programming"

count = 0
vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)