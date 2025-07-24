#Write a Python program using nested for loops to print a hollow square of 4 rows and 4 columns using asterisks (*) for the border and spaces for the interio
def main():
    n = 4
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1  or j == 0 or j == n-1:
                print("*", end = " ")
            else :
                print(" ", end = " ")    
        print()
if __name__ == "__main__":
    main()
    