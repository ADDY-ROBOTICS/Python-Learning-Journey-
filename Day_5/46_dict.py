#Write Python code to check if the key "Alice" exists in a dictionary named students containing "Alice": 85, "Bob": 90 and print the boolean result
def main():
    students = {"Alice": 85, "Bob": 90}
    key_exists = "Alice" in students
    print(key_exists)

    
if __name__ == "__main__":
    main()