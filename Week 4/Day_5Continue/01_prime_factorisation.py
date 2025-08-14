def get_prime_factor(n):

    factors = []

    p = 2

    while n > 1:

        if n % p == 0:
            factors.append(p)
            n //= p
        else:
            p += 1
    return factors 

print(f"The factors of the number 120 are {get_prime_factor(120)}")    
