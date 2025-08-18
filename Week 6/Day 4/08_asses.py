#Write a Python program that converts a string to title case, where the first letter of each word is capitalized and the rest are lowercase. The function should handle multiple spaces between words and preserve the original spacing.
def to_title_case(s):
    # Code Starts

    # Write your code here 
    lowercase_string = s.lower()

    titled_string = lowercase_string.title()
    return titled_string

    # Code Ends

# Predefined inputs
str = "hello world python"

# Function call
print(to_title_case(str))