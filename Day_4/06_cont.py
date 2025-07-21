def main():
    vowels = "aeiou"
    string = "python"
    for char in string:
        if char in vowels:
            continue
        print(char)    
if __name__ == "__main__":
    main()
    
# This code prints characters from the string "python" that are not vowels, skipping vowels using continue.