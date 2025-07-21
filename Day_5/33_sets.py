#Write Python code to check if "apple" exists in a set named fruits containing "banana", "apple", "orange" and print the boolean result.
def main():
    fruits = {"banana", "apple", "orange"}
    fruit = "apple"
    print(fruit in fruits)


if __name__ == "__main__":
    main()
    
