rows = 5
current_num = 1  # Tracks the next number to print

for i in range(1, rows + 1):
    # Print leading spaces for alignment
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print increasing numbers in the row
    for k in range(i):
        print(current_num, end=" ")
        current_num += 1  # Increment for the next number
    
    print()  # Move to the next line