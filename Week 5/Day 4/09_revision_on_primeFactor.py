def prime_factors(n):
    factors = []
    # Divide out all 2s first
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd factors from 3 onwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # If n is still greater than 2, it is a prime
    if n > 2:
        factors.append(n)

    return factors

# Example usage
number = 84
print(f"Prime factors of {number} are: {prime_factors(number)}")