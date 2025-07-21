#user_input = ''
#    while user_input != 'stop':
 ##      print(f"You Entered : {user_input}")
#
#i#f __name__ == "__main__":
 #   main()
    
# This code will keep asking for user input until the user types 'stop'.
# It will print the input each time, and when 'stop' is entered, it will break the loop and stop asking for input.



# CORRECTED AND ROBUST CODE:
def main():
    print("Type 'stop' to end the program.\n")
    while True:
        user_input = input("Enter a value: ").strip().lower()
        print(f"\n→ You entered: {user_input}\n")
        if user_input == 'stop':
            break

if __name__ == "__main__":
    main()