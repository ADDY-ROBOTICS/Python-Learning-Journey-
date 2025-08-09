def sum_of_lcm_pairs(x, y, z):
    # Code Starts
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b) if a and b else 0
    
    lcm_xy = lcm(x, y)
    lcm_yz = lcm(y, z)
    lcm_xz = lcm(x, z)
    
    return lcm_xy + lcm_yz + lcm_xz
    # Code Ends

# Predefined inputs
a = 2
b = 3
c = 4

# Function call
print(sum_of_lcm_pairs(a, b, c))