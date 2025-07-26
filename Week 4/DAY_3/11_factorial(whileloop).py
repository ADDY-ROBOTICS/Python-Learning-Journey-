def main():
    num = int(input("Enter your number here :"))
    i = 1
    factorial = 1
    while i <= num:
        factorial *= i
        i += 1
    print(factorial)



if __name__ == "__main__":
    main()
    
