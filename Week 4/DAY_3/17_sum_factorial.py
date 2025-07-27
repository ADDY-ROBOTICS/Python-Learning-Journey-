import math
def sum_of_factorials(n):
    # Code Starts
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += math.factorial(i)
    return total_sum

    # Code Ends

# Predefined inputs
num = 4

# Function call
print(sum_of_factorials(num))