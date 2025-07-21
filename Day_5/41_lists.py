#Write a Python program to add a new key "email" with value "bob@example.com" to the dictionary {"name": "Bob", "age": 30}.
def main():
    profile =  {"name": "Bob", "age": 30}
    profile["email"] = "bob@example.com"
    print(profile)

if __name__ == "__main__":
    main()
    