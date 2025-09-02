#Exercise 3.2: Skip Multiples of 5 
# Task: Print numbers from 1 to 25, but skip (don't print) any number that is a multiple of 5. 
# Expected Output: 1 2 3 4 6 7 8 9 11 12 13 14 16 17 18 19 21 22 23 24,
# Your solution here: 
# Use continue when number % 5 == 0,
for i in range(1, 26):
    if i % 5 == 0:
        continue
    print(i, end=' ')
