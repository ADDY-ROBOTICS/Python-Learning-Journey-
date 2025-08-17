#Write a Python program that takes two strings as input and returns which string is longer. Return "first" if the first string is longer, "second" if the second string is longer, or "equal" if they have the same length.
def compare_string_length(s1, s2):
    # Code Starts

    # Write your code here 
    length_1 = len(s1)
    length_2 = len(s2)
    if length_1 > length_2:
        return "first"
    elif length_2 > length_1:
        return "second"
    elif length_1 == length_2:
        return "equal"
    # Code Ends

# Predefined inputs
str1 = "Hello"
str2 = "Hi"

# Function call
print(compare_string_length(str1, str2))