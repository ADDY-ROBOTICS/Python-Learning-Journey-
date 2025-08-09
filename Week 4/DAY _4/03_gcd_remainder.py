def main():
    a , b = 120 , 45 
    print("The remainder obtained by each iteration of the GCD loop is:")
    while b != 0:
        remainder = a % b 
        print(remainder)
        a , b = b , remainder

if __name__ == "__main__":
    main()
    
    
# This code demonstrates the process of finding the GCD of two numbers using the Euclidean algorithm, printing the remainder at each step