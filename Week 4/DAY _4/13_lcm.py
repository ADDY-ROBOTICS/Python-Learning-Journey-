def main():
    a , b = 5 , 20 
    while b != 0:
        # Using the Euclidean algorithm to find GCD
        a , b = b , a % b
    

    #LCM = a * b // GCD(a , b )
    LCM = a * b // a 
    print(LCM)
if __name__ == "__main__":
    main()
    