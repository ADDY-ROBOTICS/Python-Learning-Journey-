def main():
    rows = 5 
    cols = 7 
    for i in range(rows): 
        for j in range(cols):
            if i % 2 != 0:
                print(" ", end = " ")
            else:
                print("*", end = " ")
        print()

if __name__ == "__main__":
    main()
    

    
#Write a Python program to print a 5-row by 7-column rectangle where odd-numbered rows (1st, 3rd, 5th) contain stars (*) and even-numbered rows contain spaces, using nested for loops.
