#Write a Python program using nested for loops to print a 2x3 rectangle where numbers increment from 1 to 6 across rows.
def main():
    num = 1
    for i in range(2):
        for j in range(3):
            print(num , end = " ")
            num += 1
        print()   
if __name__ == "__main__":
    main()
