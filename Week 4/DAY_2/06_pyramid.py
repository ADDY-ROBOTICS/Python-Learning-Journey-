def main():
    rows = 5 
    for i in range(1, rows + 1):
        print(" "* (rows - i), end = "")
        print("*"*(2*i-1))

if __name__ == "__main__":
    main()
    
