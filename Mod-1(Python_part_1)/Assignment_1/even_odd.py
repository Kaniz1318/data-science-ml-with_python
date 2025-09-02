# Problem 01: Write a Python program that takes a number as input and checks whether it is even or odd.

num = int(input("Please enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
