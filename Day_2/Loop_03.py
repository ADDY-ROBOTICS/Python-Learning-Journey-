def main():
    start = int(input("Enter start number: "))  # Step 1: Get user input
    # Step 2: Initialize loop variable
    while start >= 0:  # Step 3: Set condition
        print(start)  # Step 4: Print current number
        start -= 1 # Step 5: Decrement counter
    print("Blast off!")  # Step 6: Final message
     
     
if __name__ == "__main__":
    main()