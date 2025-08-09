#Write a Python Program that performs various mathematical operations on a number using built-in math functions. The function should return the absolute value, rounded value, and whether the number is positive or negative.
def math_operations(n):
    # Code Starts

    # Write your code here 
    absolute_val = abs(n)
    rounded_val = round(n)
    
    if n < 0:
        sign = "negative"
    else:
        sign = "positive"
        
    # Combine everything into one string with newlines (\n)
    return f"Absolute: {absolute_val}\nRounded: {rounded_val}\nSign: {sign}"

    # Code Ends

# Predefined inputs
number = -7.8

# Function call
print(math_operations(number))