#Write a program that prints “GCD is:” followed by the result for a = 66 and b = 22.
def main():
    a , b = 66 , 22 
    while b != 0:
        a , b = b , a % b 

    print("GCD is", a )

if __name__ == "__main__":
    main()
    
# This code calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.