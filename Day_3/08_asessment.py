def print_multiplication_table(n):
    # Code Starts
    print(f"Multiplication Table for {num}:")
    for i in range(1,11):
        product = num * i
        print(f"{num} x {i} = {product}")
    # Code Ends

# Predefined inputs
num = 5

# Function call
print_multiplication_table(num)