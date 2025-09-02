# Problem 03: Write a program using a for loop that calculates the sum of even numbers between 1 and 100.

total = 0
for num in range(1, 101):   
    if num % 2 == 0:        
        total += num        

print("Sum of even numbers between 1 and 100 is:", total)
