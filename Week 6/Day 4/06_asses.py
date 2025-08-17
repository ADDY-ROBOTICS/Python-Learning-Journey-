def count_vowels_and_consonants(text):
    # Code Starts

    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    # Loop through each character in the original string
    for char in text:
        # First, check if the character is an alphabet letter
        if char.isalpha():
            # If it is a letter, then check if it's a vowel
            if char in vowels:
                vowel_count += 1
            else:
                # If it's a letter and not a vowel, it must be a consonant
                consonant_count += 1
    
    # Return a tuple of the counts, not a string
    return (vowel_count, consonant_count)

    # Code Ends

# Predefined inputs
str = "hello world"

# Function call
print(count_vowels_and_consonants(str))

# Example with non-alphabetic characters
str2 = "Python123"
print(count_vowels_and_consonants(str2))