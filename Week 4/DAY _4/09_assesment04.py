def count_common_divisors(x, y):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    g = gcd(x, y)
    count = 0
    for i in range(1, int(g**0.5) + 1):
        if g % i == 0:
            if i == g // i:
                count += 1
            else:
                count += 2
    return count

# Predefined inputs
a = 12
b = 18

# Function call
print(count_common_divisors(a, b))