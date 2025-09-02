#Exercise 6.2: Height of a Building
#Task: Calculate the height of a building using trigonometry.
#Problem: You're standing 50 meters away from a building. The angle of elevation to the top of the building is 30 degrees. Calculate the height of the building.
#Formula: height = distance × tan(angle)
#Expected Output:
#Distance from building: 50 meters
#Angle of elevation: 30 degrees
#Height of building: 28.87 meters
#distance = 50  # meters
#angle_degrees = 30
# Your solution here:
# Convert degrees to radians: math.radians()
# Use math.tan() to calculate height
import math

distance = 50  # meters
angle_degrees = 30

# Degrees to radians
angle_radians = math.radians(angle_degrees)

# Height calculation
height = distance * math.tan(angle_radians)

print(f"Distance from building: {distance} meters")
print(f"Angle of elevation: {angle_degrees} degrees")
print(f"Height of building: {height:.2f} meters")
