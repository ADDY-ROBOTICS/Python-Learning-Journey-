def main():
    day = "Monday"
    match day:
        case "Monday" | 'Friday':
            print("Workday")
        case _:
            print("Other day")    

if __name__ == "__main__":
    main()