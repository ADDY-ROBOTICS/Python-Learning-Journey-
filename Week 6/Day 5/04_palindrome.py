def main():
    s = "noon"
    start = 0
    end = len(s) - 1
    
    is_a_palindrome = True # Flag starts as True

    while start < end:
        if s[start] != s[end]:
            is_a_palindrome = False # Change flag on mismatch
            break
            
        start += 1
        end -= 1
    
    # This is the only part that changes.
    # We check the flag and print the desired string.
    if is_a_palindrome:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()