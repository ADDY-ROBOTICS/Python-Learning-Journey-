def get_prime_factors(n):
    # This list will hold our "pile of bricks"
    factors = []
    
    # Start with our smallest tool (divisor), which is 2
    d = 2
    
    # Keep going as long as our number is bigger than 1
    while n > 1:
        # Check if we can divide our number by the current tool 'd'
        if n % d == 0:
            # If yes, we found a prime factor!
            factors.append(d)
            # Make our number smaller by dividing it
            n = n / d
        else:
            # If not, try the next tool
            d = d + 1
            
    return factors

# Example Usage:
print(f"The prime factors of 56 are: {get_prime_factors(56)}")
# Output: The prime factors of 56 are: [2, 2, 2, 7]