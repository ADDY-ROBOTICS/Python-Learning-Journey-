def main():
    rows = 3
    columns = 5
    for i in range(rows):#Iterate through each row
        for j in range(columns):#Iterates the inner loop through each column
            print("#", end = " ")#Prints asolid rectangle
        print()    #after completing moves it tot he next line 
if __name__ == "__main__":
    main()
    
