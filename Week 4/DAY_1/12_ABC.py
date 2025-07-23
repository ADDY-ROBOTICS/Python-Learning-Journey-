def main():
    rows = 3
    for i in  range(rows):
        for j in range(rows):
            if i == 0:
                print("A", end = " ")
            elif i ==1:
                print("B", end = " ")
            elif i ==2:
                print("C", end = " ")
        print()       



if __name__ == "__main__":
    main()
    
