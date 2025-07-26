def count_digits(n):
    # Code Starts
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

    # Code Ends

# Predefined inputs
num = 12345

# Function call
print(count_digits(num))