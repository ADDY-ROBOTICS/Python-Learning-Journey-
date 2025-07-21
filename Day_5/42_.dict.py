#Write a Python program to delete the key "age" from the dictionary {"name": "Alice", "age": 30}
def main():
    profile =  {"name": "Alice", "age": 30}
    del profile["age"]
    print(profile)
    

if __name__ == "__main__":
    main()
    