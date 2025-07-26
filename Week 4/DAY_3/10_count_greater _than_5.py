def count_digits_greater_than_five(n):
    # Code Starts
    count = 0
    while n > 0:
        digit = n % 10
        if digit > 5:
            count += 1 
        n = n // 10
    return count
    

    # Code Ends

# Predefined inputs
num = 12789

# Function call
print(count_digits_greater_than_five(num))