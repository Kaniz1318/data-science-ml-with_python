#Exercise 1.3: Print Multiplication Table
#Task: Create a multiplication table for the number 7 from 1 to 10.
#Expected Output:
#7 × 1 = 7
#7 × 2 = 14
#7 × 3 = 21
#...
#7 × 10 = 70
number=7
for i in range(1,11):
    mul=number*i  
    print(f"{number} × {i} = {mul}")