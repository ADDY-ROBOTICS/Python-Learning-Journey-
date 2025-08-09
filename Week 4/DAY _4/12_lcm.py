def main():
    a , b = 10 , 15 
    max_num = max(a , b)

    while True:
        if max_num % a ==0 and max_num % b == 0:
            print("The LCM is", max_num)
            break
        max_num += 1


if __name__ == "__main__":
    main()
    
# This code calculates the least common multiple (LCM) of two numbers by incrementing from the maximum of the two numbers until it finds a number that is divisible by both.