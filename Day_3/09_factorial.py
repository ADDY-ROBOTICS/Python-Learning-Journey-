'''def calculate_factorial(n):
    # Code Starts
    print(f"Calculating factorial of {num}:")
    print(f"{num}! =")
    factorial = 1
    counter = 1
    for counter  in range(1,num + 1):
     factorial *= counter 
     print(f"{counter}", 'x',end=' ')

     counter += 1 
     
    print(factorial) 

    # Code Ends

# Predefined inputs
num = 5

# Function call
calculate_factorial(num)'''

def calculate_factorial(n):
    # Code Starts
    print(f"Calculating factorial of {n}:")
    
    factorial = 1
    factors_string = ""

    for counter in range(n, 0, -1):  # Loop from n down to 1
        factorial *= counter
        if counter == n:
            factors_string += str(counter)  # Start the string with the first number
        else:
            factors_string += " x " + str(counter)  # Append other numbers

    print(f"{n}! = {factors_string} = {factorial}")  # Final output
    # Code Ends

# Predefined inputs
num = 5

# Function call 
calculate_factorial(num)
