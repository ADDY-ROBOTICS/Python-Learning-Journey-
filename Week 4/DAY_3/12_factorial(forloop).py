def main():
    factorial = 1
    num = 5

    for i in range(1, num + 1):
        factorial *= i
    print(factorial)

if __name__ == "__main__":
    main()
    
# This code calculates the factorial of a number using a for loop.