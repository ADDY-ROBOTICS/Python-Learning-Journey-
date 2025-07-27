def is_factorial(n):
    # Code Starts
    factorial  = 1 
    num_1 = 1 
    while factorial < n:
        num_1 += 1
        factorial *= num_1
    if factorial == n:
        return True
    else:
        return False

    # Code Ends

# Predefined inputs
num = 24

# Function call
print(is_factorial(num))