#Write a Python program that takes an integer as input and returns True if the number is even, and False if the number is odd. The function should use the modulo operator (%) to determine if a number is divisible by 2.
def is_even(n):
    # Code Starts

    # Write your code here 
    if n % 2 == 0:
        return True
    else:
        return False

    # Code Ends

# Predefined input
num = 8

# Function call
print(is_even(num))