def main():
    num_row = 3 
    num_column = 4
    for i in range(num_row):
        for j in range(num_column):
            if i % 2 != 0:
                print("2", end = " ")
            elif i % 2 == 0:
                print("1", end = " ")    
        print()
if __name__ == "__main__":
    main()
#Write a Python program using nested for loops to print a 3x4 rectangle where odd-numbered rows print 1 and even-numbered rows print 2 (0-based indexing for rows).