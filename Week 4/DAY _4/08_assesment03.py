def are_coprime(x, y):
    # Code Starts
    while y != 0:
        x , y = y , x % y 
    if x == 1:
        return True
    else :
        return False 

    

    # Code Ends

# Predefined inputs
a = 8
b = 15

# Function call
print(are_coprime(a, b))