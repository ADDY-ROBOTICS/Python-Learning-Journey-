def calculate_sum_upto(num):
    # Code Starts
    print(f"Calculating sum from 1 to {num}:")
    total = 0
    for i in range(1,num + 1):  
        total += i
        print(total)  # Print the current sum
        
    # Code Ends

# Predefined inputs
num = 4

# Function call
calculate_sum_upto(num)