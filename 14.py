def main():
    num = int(input("Enter your number here:"))
    match num:
        case n if n > 0:
            print('Positive Number')
        case _:
            print('Non-Positive')    
if __name__ == "__main__":
    main()