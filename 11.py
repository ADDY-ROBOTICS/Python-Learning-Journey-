def main():
    day = 'Saturday'
    match day:
        case 'Saturday' | 'Sunday':
            print('Weekend')
        case _:
            print('Weekday')    

if __name__ == "__main__":
    main()