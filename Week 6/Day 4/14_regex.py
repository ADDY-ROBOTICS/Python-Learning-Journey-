#Write a Python program to check if the word 'Python' exists in the string 'I am learning Python programming'.
import re
def main():
    text = "I am learning Python programming"

    word_to_find = "Python"

    if word_to_find in text:
        print(f"{word_to_find} exists in text")
    else:
        print(f"{word_to_find} doesn't exist in the text ")

if __name__ == "__main__":
    main()