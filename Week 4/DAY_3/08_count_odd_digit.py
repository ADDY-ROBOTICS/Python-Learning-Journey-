def count_odd_digits(n):
    # Code Starts

    count = 0
    while n > 0:
        digits = n % 10
        if digits % 2 != 0:
            count += 1
        n = n // 10
    return count   

    # Code Ends

# Predefined inputs
num = 12345

# Function call
print(count_odd_digits(num))