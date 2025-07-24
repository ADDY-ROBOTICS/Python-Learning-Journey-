def main():
    rows = 1
    cols = 5
    while rows <= 5:
        for j in range(cols):
            print("*", end="")
        print()  # New line after each row
        rows += 1  # Increment after printing

if __name__ == "__main__":
    main()
#Write a Python program to print a 5x5 square of stars (*) using a while loop for the outer loop and a for loop for the inner loop.

