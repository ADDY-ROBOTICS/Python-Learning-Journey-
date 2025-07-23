 #to create a 
def main():
    n = 3
    num = 1
    for i in range(n):
        for j in range(n):
            print(num , end = " ")
            num += 1 
        print()    
if __name__ == "__main__":
    main()
    
# This code prints a 3x3 grid of numbers starting from 1
# It uses nested loops to iterate through rows and columns, printing numbers sequentially.

#After modificattion the real question is as follows 
#Write a Python program using nested for loops to print a 3x3 square where each position in a row contains the row number (1-based indexing).
def main():
    
    
    for row  in range(1,4):
        for cols in range(3):
            print(row , end = " ")
            
        print()    
if __name__ == "__main__":
    main()  