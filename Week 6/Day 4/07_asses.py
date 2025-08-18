#Write a Python program that removes duplicate characters from a string while preserving the order of first occurrence. The function should return the string without duplicates.
def remove_duplicates(s):
    # Code Starts

    # Write your code here 
    seen_characters = set()
    result_string = ""

    for char in s:
        if char not in seen_characters:
            seen_characters.add(char)
            result_string += char
    return result_string
    # Code Ends

# Predefined inputs
str = "programming"

# Function call
print(remove_duplicates(str))

#Try Again 
