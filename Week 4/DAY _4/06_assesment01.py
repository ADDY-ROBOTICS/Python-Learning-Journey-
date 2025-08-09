def find_gcd(x, y):
    # Code Starts

    while y != 0:
        x , y = y , x % y 

    return x

    # Code Ends

# Predefined inputs
a = 12
b = 8

# Function call
print(find_gcd(a, b))