#Exercise 6.1: Geometry Calculator
#Task: Calculate the area of different shapes using math functions.
#Given shapes:
#Circle with radius = 7
#Right triangle with sides a = 8, b = 6 (find hypotenuse and area)
#Square with side = 5 (find diagonal)
#Expected Output:

#Circle (radius=7):
# Area = 153.94 square units

#Right Triangle (a=8, b=6):
# Hypotenuse = 10.0
# Area = 24.0 square units

#Square (side=5):
# Area = 25 square units
# Diagonal = 7.07
# Your solution here:
# Circle: area = π * r²
# Triangle: hypotenuse = √(a² + b²), area = (a * b) / 2
# Square: diagonal = side * √2

import math

# --- Circle ---
radius = 7
circle_area = math.pi * radius**2
print(f"Circle (radius={radius}):")
print(f" Area = {circle_area:.2f} square units\n")

# --- Right Triangle ---
a = 8
b = 6
hypotenuse = math.sqrt(a**2 + b**2)
triangle_area = (a * b) / 2
print(f"Right Triangle (a={a}, b={b}):")
print(f" Hypotenuse = {hypotenuse:.1f}")
print(f" Area = {triangle_area:.1f} square units\n")

# --- Square ---
side = 5
square_area = side**2
diagonal = side * math.sqrt(2)
print(f"Square (side={side}):")
print(f" Area = {square_area} square units")
print(f" Diagonal = {diagonal:.2f}")
