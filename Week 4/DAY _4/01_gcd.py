def main():
    a , b = 45 , 30 
    while b != 0:
        a , b = b , a % b 
        # OR 
      #  temp = a 
       # b = a % b
        #a = temp

    print("The gcd of these two numbers is :", a )

if __name__ == "__main__":
    main()
    
# This code calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.