def is_palindrome(s):
    # Code Starts

    # Write your code here 
    clean_string = s.replace(" ","").lower()
    start = 0
    end = len(clean_string) - 1

    while start < end:
        if clean_string[start] != clean_string[end]:
            return False
        start += 1
        end -= 1
    return True


    # Code Ends

# Predefined inputs
str = "A man a plan a canal Panama"

# Function call
print(is_palindrome(str))