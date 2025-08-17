#Write a Python program that takes two strings as input and returns True if they are equal when compared case-insensitively, otherwise False
def are_equal_case_insensitive(s1, s2):
    # Code Starts

    # Write your code here 
    if s1.lower() == s2.lower():
        return True
    else:
        return False

    # Code Ends

# Predefined inputs
str1 = "Hello"
str2 = "hello"

# Function call
print(are_equal_case_insensitive(str1, str2))