def calculate_sum_upto(num):
    print(f"Calculating sum from 1 to {num}:")
    total = 0
    numbers = []  # Store numbers here
    
    for i in range(1, num + 1):
        total += i
        numbers.append(i)  # Add current number to the list
    
    # Convert list to "1 + 2 + 3 + 4" format
    equation = " + ".join(map(str, numbers))
    print(f"{equation} = {total}")  # Final output

# Test
calculate_sum_upto(4)