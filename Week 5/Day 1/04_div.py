#Write code to find and print the first number that divides 9.
def main():
    divisor = 1

    while True:
        if 9 % divisor == 0:
            print(divisor)
            break
        else:
            divisor += 1 

if __name__ == "__main__":
    main()
    
