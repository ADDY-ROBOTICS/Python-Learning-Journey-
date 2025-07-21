def main():
    print('Menu :')
    print('1. Start')
    print('2. Stop')    
    print('3. Exit')    

    choice = int(input("Enter from (1-3):"))
    match choice:
        case 1:
            print('Start')
        case 2:
            print('Stop')
        case 3:
            print('Exit')
        case _:
            print("Inavlid user Input.Please enter (1-3)")            

if __name__ == "__main__":
    main()
    
