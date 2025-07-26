def factorial(n):
    # Code Starts
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
    # Code Ends

# Predefined inputs
num = 5

# Function call
print(factorial(num))