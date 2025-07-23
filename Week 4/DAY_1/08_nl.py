size = 3

for i in range(size):
    for j in range(size):
        if i == j:
            print(1, end = " ")
        else :
            print(0, end = " ")    
    print()  # Move to the next line after each row
# This code prints an identity matrix of size 3x3
