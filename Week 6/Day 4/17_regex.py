#Write a Python program to extract all digit sequences from the string 'Order 1234, shipped on 2023-05-12' using regular expressions.
import re
def main():
    string = "Order 1234, shipped on 2023-05-12"
    check_digits = re.findall(r"\d+", string)
    print(check_digits)
    

if __name__ == "__main__":
    main()