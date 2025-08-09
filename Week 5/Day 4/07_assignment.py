def get_first_nonzero_digit(num):
    # Code Starts

    # Write your code here 
    s = str(num)
    for char in s:
        if char.isdigit() and char != '0':
            return int(char)


    # Code Ends

# Predefined inputs
n = 0.00123

# Function call
print(get_first_nonzero_digit(n))