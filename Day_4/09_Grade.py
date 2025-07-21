def get_letter_grade(s):
    # Code Starts
    if score in range(90, 101):
        return 'A'
    elif score in range(80, 90):
        return 'B'
    elif score in range(70, 80):
        return 'C'
    elif score in range(60, 70):
        return 'D'
    else:
        return 'F'
    # Code Ends

# Predefined inputs
score = 85

# Function call
print(get_letter_grade(score))