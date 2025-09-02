#Exercise 2.2: Find the Target Number
#Task: Use a while loop to find how many times you need to double the number 2 to exceed 1000. 
# Expected Output: 
# Starting with: 2 
# After 1 doubles: 4 
# After 2 doubles: 8 
# After 3 doubles: 16 
# ... 
# After 9 doubles: 1024 
# It took 9 doubles to exceed 1000,
# Your solution here: # Initialize number = 2, count = 0 
# While number <= 1000, multiply by 2 and increment


number = 2
count = 0

print(f"Starting with: {number}")

while number <= 1000:
    count += 1
    number = number * 2
    print(f"After {count} doubles: {number}")

print(f"It took {count} doubles to exceed 1000")
  