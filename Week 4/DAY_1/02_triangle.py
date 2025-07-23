# Number of rows for the triangle
rows = 5

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for printing stars
    for j in range(1, i + 1):
        print("*", end=" ")
    # Move to the next line after each row
    print()
# This code prints a right-angled triangle of stars