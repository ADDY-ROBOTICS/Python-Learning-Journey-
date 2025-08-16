#Write a Python program to extract all numbers from a string using raw string and regular expressions.  
import re 
def main():
    pattern = r"\d+"
    text = "I have 2 pair of shoes "
    numbers = re.findall(pattern, text)
    print(numbers)
    

if __name__ == "__main__":
    main()