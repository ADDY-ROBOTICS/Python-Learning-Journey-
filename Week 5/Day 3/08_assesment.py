def get_value_info(val, min, max):
    # Code Starts

    # Write your code here 
    type_n = type(val).__name__
    if val in range(min,max+1):
        boolean = "True"
    else:
        boolean = "False"

    return  f"Type: {type_n}, In Range({min}-{max}): {boolean}"

    # Code Ends

# Predefined inputs
value = 25
min_val = 10
max_val = 50

# Function call
print(get_value_info(value, min_val, max_val))