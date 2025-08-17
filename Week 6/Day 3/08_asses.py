#Write a Python program that takes two strings as input and returns True if the first string comes before the second string in alphabetical order, otherwise False.
def alphabetical_order(s1, s2):
    # Code Starts

    # Write your code here 
    if s1 < s2:
        return True
    else:
        return False

    # Code Ends

# Predefined inputs
str1= "apple"
str2 = "banana"

# Function call
print(alphabetical_order(str1, str2))