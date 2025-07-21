def main():
    count = 0          # Initialize counter
    current_num = 2    # Start from the first even number
    
    while current_num <= 10:
        count += 1          # Increment counter
        current_num += 2    # Move to the next even number
    
    print(count)  # Final count

if __name__ == "__main__":
    main()
    