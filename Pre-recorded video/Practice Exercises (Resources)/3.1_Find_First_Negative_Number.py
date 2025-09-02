#Exercise 3.1: Find First Negative Number 
# Task: Find and print the first negative number in a list. Stop searching once you find it. 
# Given: numbers = [5, 12, -3, 8, -7, 15, -2] 
# Expected Output: 
# Checking: 5 
# Checking: 12 
# Checking: -3 
# Found first negative number: -3,
# Your solution here: 
# Use a for loop and break when you find a negative number,
numbers = [5, 12, -3, 8, -7, 15, -2]

for i in numbers:
    print(f"Checking: {i}")
    if i < 0:
        print(f"Found first negative number: {i}")
        break

        