#Write a Python program that calculates the area of a circle. The function should take a radius as a parameter with a default value of 1. Use the formula: Area = π × radius² Use 3.14159 as the value of π.

def calculate_circle_area(r):
    # Code Starts

    # Write your code here 
    return 3.14159 * (r**2)

    # Code Ends

# Predefined inputs
radius = int(input("Enter the radius of the circle (default is 1): ") or 1)

# Function call
print(calculate_circle_area(radius))