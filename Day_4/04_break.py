def main():
    print('Input numbers(Negative number will break the loop)')
    number = int(input("Enter your number here :"))
    count = 1
    while count < 5:
        print("You entered:", number)
        number = int(input("Enter your number here :"))
        count += 1
        if number < 0:
            break
        
if __name__ == "__main__":
    main()
    