def main():
    row = 4
    column = 3
    for i in range(1, row+1):
        for j in range(column):
            print(f"{i:2d}", end = " ")
        print()
if __name__ == "__main__":
    main()
    
#Q Write a Python program using nested for loops to print a 4x3 rectangle where each row contains the row index, each printed with a fixed width of 2 characters.