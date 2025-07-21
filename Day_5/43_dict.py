#Write Python code to access and print the value associated with the key "Bob" from a dictionary named grades containing "Alice": 85, "Bob": 90.
def main():
    grades = {"Alice": 85, "Bob": 90}
    bob_grades = grades["Bob"]
    print(bob_grades)


if __name__ == "__main__":
    main()
    