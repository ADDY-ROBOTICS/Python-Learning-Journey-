rows = 4

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for printing stars
    for j in range(1, i + 1):
        print(j, end=" ")
    # Move to the next line after each row
    print()
    
# This code prints a right-angled triangle of numbers