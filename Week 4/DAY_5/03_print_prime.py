def generate_primes(n):
    primes = []
    number = 2  # Starting from the first prime number

    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime * prime > number:  # No need to check beyond the square root of num
                break
            if number % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(number)
        
        number += 1  # Check the next number
    
    print(f"First {n} prime numbers:", *primes)


# Predefined inputs
num = 5

# Function call
generate_primes(num)
