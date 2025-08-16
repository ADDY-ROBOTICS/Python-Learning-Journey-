def count_vowels(str):
    # Code Starts

    # Write your code here 
    vowels = "aeiouAEIOU"
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count

    # Code Ends

# Predefined inputs
input = "Hello World"

# Function call
print(count_vowels(input))