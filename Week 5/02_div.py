#Write a loop from 1 to 6 and print i if it divides 6.
def main():
    num = 6 

    for i in range(1 , num +1 ):
        if num % i == 0:
            print(i)
if __name__ == "__main__":
    main()
    
