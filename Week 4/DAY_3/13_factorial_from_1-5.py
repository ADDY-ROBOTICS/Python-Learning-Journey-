def main():
    for num in range(1, 6):
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}")
if __name__ == "__main__":
    main()
# This code calculates the factorial of numbers from 1 to 5 using a for loop.