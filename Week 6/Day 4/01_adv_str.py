#Write a Python program to left justify the string 'Python' to 10 characters using hyphens.
def main():
    text = "Python"
    print(text.ljust(10, "-"))

if __name__ == "__main__":
    main()