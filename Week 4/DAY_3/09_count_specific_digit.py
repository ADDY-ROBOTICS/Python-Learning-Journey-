def count_specific_digit(n,d):
    # Code Starts

    count = 0 
    while n  > 0:
        digits = n % 10
        if digits == d:
            count += 1
        n = n // 10
    return count       

    # Code Ends

# Predefined inputs
num = 555
digit = 5

# Function call
print(count_specific_digit(num, digit))