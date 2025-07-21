def get_life_stage(a):
    # Code Starts
    if age in range(0,13):
     return "Child"
    elif age in range(13,20):
     return "Teen"
    elif age in range(20,60):
     return "Adult"
    else :
     return  'Senior'   
    # Code Ends

# Predefined inputs
age = 25

# Function call
print(get_life_stage(age))