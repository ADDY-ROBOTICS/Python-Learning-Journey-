#Write a Python program that calculates both the area and perimeter of a rectangle. The function should take length and width as keyword arguments. Return a formatted string showing both calculations.
def rectangle_metrics( l, w):
    # Code Starts

    # Write your code here 

    return f"Area: {l*w} , Perimeter: {2*(l+w)}"

    # Code Ends

# Predefined inputs
length = 5
width = 3

# Function call
print(rectangle_metrics(length, width))