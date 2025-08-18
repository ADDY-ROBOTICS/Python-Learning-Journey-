#Write a Python program to check if the word 'email' appears in the string 'Please send an email to support@example.com' using regex.
import re
def main():
    text = 'Please send an email to support@example.com'
    check_word = re.search(r"email" , text)
    print(bool(check_word))
    

if __name__ == "__main__":
    main()
    