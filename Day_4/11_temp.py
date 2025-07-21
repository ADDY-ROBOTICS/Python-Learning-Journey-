def convert_temperature(t, u):
    # Code Starts
    if unit == "F":
       F = (temp*9/5)+32
       return F
    elif unit == "K":
       K = (temp + 273.15)
       return K
    # Code Ends

# Predefined inputs
temp = 0
unit = "F"

# Function call
print(convert_temperature(temp, unit))