#Write a Python program using named placeholders in str.format() to print 'My name is Alice and I am 25 years old.'
def main():
    string = "My name is {name} and I am {age} years old.".format(name = "Alice" , age = 25)
    print(string)

if __name__ == "__main__":
    main()
    
