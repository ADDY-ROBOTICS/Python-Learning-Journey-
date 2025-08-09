def find_gcd(x, y, z):
    # Code Starts

    while y != 0:
        x , y = y , x % y 
        GCD = x 
    
    while z != 0:
        GCD, z = z, GCD % z
    return GCD

    return a

    # Code Ends

# Predefined inputs
a = 12
b = 18
c = 24

# Function call
print(find_gcd(a, b, c))