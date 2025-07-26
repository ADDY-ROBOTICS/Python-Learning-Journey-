def main():
    num = int(input("Enter Your number ="))
    factorial = 1
    if num > 0:
        for i in range(1, num + 1):
            factorial *= i
        print(factorial)
    else:
        print("Error , Enter Positive value")

if __name__ == "__main__":
    main()
    
# This code calculates the factorial of a number using a for loop, with error handling for non-positive inputs.