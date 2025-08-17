#Write a Python program to replace all occurrences of 'Python' with 'Java' in the string 'Python is fun, Python is powerful'
def main():
    string = "Python is fun, Python is powerful"
    replaced_string = string.replace("Python", "Java")
    print(replaced_string)
    
if __name__ == "__main__":
    main()