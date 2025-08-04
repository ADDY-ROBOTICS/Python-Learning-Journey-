#Write a Python program that takes a string and returns information about it using predefined string functions. The function should return the length of the string, its uppercase version, and its lowercase version.
def analyze_string(str):
    # Code Starts

    # Write your code here 
    return f"Length: {len(str)}, Upper: {str.upper()}, Lower: {str.lower()}"

    # Code Ends

# Predefined inputs
text = "Hello World"

# Function call
print(analyze_string(text))