def count_common_divisors(x, y):
    # Code Starts
    # Calculate GCD using Euclidean algorithm
    a, b = x, y
    while b:
        a, b = b, a % b
    gcd = a
    
    # Count divisors of the GCD
    if gcd == 0:
        return 0
    
    count = 0
    i = 1
    while i*i <= gcd:
        if gcd % i == 0:
            if i == gcd // i:
                count += 1
            else:
                count += 2
        i += 1
    return count
    # Code Ends

# Predefined inputs
a = 12
b = 18

# Function call
print(count_common_divisors(a, b))