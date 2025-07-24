#Write a Python program to print a 6-row by 4-column rectangle with a checkerboard pattern of stars (*) and spaces, using nested for loops.
def main():
    rows = 6
    columns = 4 
    for i in range(rows):
        for j in range(columns):
            if (i+j) % 2 == 0:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
if __name__ == "__main__":
    main()
    