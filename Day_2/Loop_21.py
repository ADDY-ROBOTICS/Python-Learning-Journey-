def main():
    number = 2**0  # Start with 2 raised to the power of 20

    n = 0
    while number <= 100:
        n += 1
        number = 2 ** n
    print(n)  # Output the smallest n such that 2^n > 100

if __name__ == "__main__":
    main()
    
# This code calculates the smallest power of 2 that is greater than 100.
# The loop continues until the number exceeds 100, incrementing n to find the power.