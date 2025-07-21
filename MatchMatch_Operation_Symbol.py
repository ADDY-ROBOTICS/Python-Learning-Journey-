def main():
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    num1 = float(input("Enter first number: "))
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                result = "Error! Division by zero."
            else:
                result = num1 / num2
        case _:
            result = "Invalid operator!"

    print(f"The result is: {result}")
    
    

if __name__ == "__main__":
    main()