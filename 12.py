def main():
    try:
        number = int(input("Enter a number: "))
        match number:
            case 1 | 2 | 3:
                print("Low Number")
            case _ if number < 1:
                print('Error.Enter positive numbers only')     
            case _:
                print("High Number")     
    except ValueError:
        print("Invalid input. Please enter a valid integer.")        
if __name__ == "__main__":
    main()