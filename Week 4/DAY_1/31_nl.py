def main():
    rows = 2 
    cols = 4
    num = 1 
    for i in range(rows):
        for j in range(cols):
            print(f"{num:2d}", end = " ")
            num += 1 
        print()    
if __name__ == "__main__":
    main()
    
    #Write a Python program using nested for loops to print a rectangle of 2 rows and 4 columns, where numbers increment from 1 and are printed with a fixed width of 2 characters (e.g., " 1", " 2").