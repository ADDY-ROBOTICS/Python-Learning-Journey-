def main():
    """Checks if a number is positive, negative, or zero."""
    try:
        num = int(input("Enter your number: "))
        match num:
            case n if n > 0:
                print("\nThe number is positive")
            case n if n < 0:
                print("\nThe number is negative")
            case _:
                print("\nThe number entered is Zero")
    except ValueError:
        print("\nInvalid input! Please enter an integer.")

if __name__ == "__main__":
    main()