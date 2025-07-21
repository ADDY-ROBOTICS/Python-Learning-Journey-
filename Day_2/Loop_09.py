def count_even_numbers(n):
    # Code Starts
    count = 0
    for number in range(1, n ):
        if number % 2 == 0:    
            count += 1
    print(count)
        
        
     

    # Code Ends

# Predefined inputs
n = 10

# Function call
count_even_numbers(n)