def main():
    color = "Red"
    match color:
        case 'Blue':
            print('Blue')
        case 'Green':
            print('Green')
        case _:
            print('Unknown Color')        

if __name__ == "__main__":
    main()