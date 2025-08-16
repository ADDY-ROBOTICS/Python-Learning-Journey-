#Write a Python program that takes a sentence as input and returns the number of words in the sentence.
def count_words(str):
    # Code Starts

    # Write your code here 
    return len(str.split())

    # Code Ends

# Predefined inputs
sentence = "Hello world from Python"

# Function call
print(count_words(sentence))