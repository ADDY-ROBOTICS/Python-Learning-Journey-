#Write a Python program to update the value of key "age" to 35 in the dictionary {"name": "Bob", "age": 30}.
def main():
    profile = {"name": "Bob", "age": 30}
    profile.update({"age" : 35})
    print(profile)

if __name__ == "__main__":
    main()
    