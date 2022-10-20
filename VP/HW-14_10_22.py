import random
n = int(input("Enter a number:"))
print(n)
digits = []
for i in range (len(str(n))):
    digit = n % 10
    digits.insert(i, digit)
    n = n // 10
print(digits)
print("Here`s the sum of it`s digits:", sum(digits))