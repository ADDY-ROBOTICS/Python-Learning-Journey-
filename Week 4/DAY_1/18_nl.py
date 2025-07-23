#Q Write a Python program using nested for loops to print a 3x3 square where numbers increment from 1 to 9, each printed with a fixed width of 2 characters.
def main():
    num = 1
    row, col = 3, 3
    for i in range(row):
        for j in range(col):
            print(f"{num:2d}", end = " ")
            num += 1
        print()    
if __name__ == "__main__":
    main()
    