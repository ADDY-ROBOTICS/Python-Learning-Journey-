def main():
    rows = 3
    columns = 4 
    for i in range(1,rows + 1):
        for j in range(columns):
            
                print(i, end = " ")
            
        print()
if __name__ == "__main__":
    main()
    
#def main():# for hollow rectangle
    rows = 3
    columns = 4 
    for i in range(1,rows + 1):
        for j in range(columns):
            if i == 1 or i == rows  or j == 0 or j == columns - 1:
                print(i, end = " ")
            else :
                print(" ", end = " ")    
        print()
if __name__ == "__main__":
    main()