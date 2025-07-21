def main():
    
    for _ in range(1,6):
        num = int(input("Enter your number here (negative number will be skipped):"))
        
        # If the number is negative, skip to the next iteration      
        if num < 0:
            continue
        print("You entered:", num)

if __name__ == "__main__":
    main()
    
