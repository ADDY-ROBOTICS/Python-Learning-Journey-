def main():
    User_input = ''
    # Initialize User_input to an empty string
    while User_input != 'quit':
        User_input = input("Enter here (Type quit to end the loop):")
        # This will keep asking for input until 'quit' is entered
    print(f"You entered: {User_input}")  # Final output after loop ends
if __name__ == "__main__":
    main()
    