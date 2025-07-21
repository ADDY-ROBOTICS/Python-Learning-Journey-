def find_largest(a, b, c):
    """Returns and prints the largest of three numbers."""
    biggest_of_three = max(a, b, c)
    print(f"The largest number is: {biggest_of_three}")
    return biggest_of_three

# Predefined inputs
a = 100
b = 10
c = 9

# Function call
find_largest(a, b, c)