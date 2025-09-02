#Exercise 1.1: Print Even Numbers 
#Task: Write a for loop that prints all even numbers from 2 to 20. 
#Expected Output: 2 4 6 8 10 12 14 16 18 20,
# Your solution here: 
# # Hint: Use range(start, stop, step) or check if number % 2 == 0

#Solution 1: Using range() with step
for i in range(2,22,2):
    print(i,end=' ')
    
print("-------")    
#Solution 2: Using if condition
for i in range(2,21):
    if i%2==0:
        print(i,end=' ')
    

