def main():
    print("Enter numbers to echo. Type '0' to stop:")  # Initial prompt
    number = int(input("Enter your number here: "))
    while number != 0:
        print("You entered:", number)
        number = int(input("Enter your number here: "))

if __name__ == "__main__":
    main()