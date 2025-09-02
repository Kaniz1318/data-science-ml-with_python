#Exercise 5.1: Grade Calculator
#Task: Calculate the average grade and determine letter grade.
#Given:
#grades = [85, 92, 78, 96, 88]
#Grading Scale:
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: Below 60
#Expected Output:
#Grades: [85, 92, 78, 96, 88]
#Average: 87.8
#Letter Grade: B
# Your solution here:
# Calculate sum, then divide by length for average
# Use if-elif statements for letter grade

grades = [85, 92, 78, 96, 88]

total = sum(grades)
avg = total / len(grades)

print(f"Grades: {grades}")
print(f"Average: {avg:.1f}") 

if avg >= 90:
    letter = "A"
elif avg >= 80:
    letter = "B"
elif avg >= 70:
    letter = "C"
elif avg >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Letter Grade: {letter}")

    