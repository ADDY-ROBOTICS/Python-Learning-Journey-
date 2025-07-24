def main():
    row = 2 
    column = 4
    num = 2
    for i in range(row):
        for j in range(column):
            print(f"{num:2d}", end = " ")
            num += 2
        print()    

if __name__ == "__main__":
    main()
    
