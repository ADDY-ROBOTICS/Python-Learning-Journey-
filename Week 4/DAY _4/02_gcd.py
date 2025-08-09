def main():
    a , b = 84, 18
    
    a , b = b , a % b 


    print(f"after one iteration Values of a & b are ({a}, {b})")

if __name__ == "__main__":
    main()
    
# This code demonstrates a single iteration of the Euclidean algorithm for calculating the GCD of two numbers.