def is_palindrome(s):
    # Code Starts

    # Write your code here 
    s_new = s.lower()

    start = 0
    end = len(s) - 1

    while start < end:
        if s_new[start] != s_new[end]:
            return False
            
        start += 1
        end -= 1
    return True

    # Code Ends

# Predefined inputs
str = "racecar"

# Function call
print(is_palindrome(str))