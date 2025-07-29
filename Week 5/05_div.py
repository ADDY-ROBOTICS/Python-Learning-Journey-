#Print the divisors of 5 with text like: 5 is divisible by 1
def main():
    print("5 is divisible by")
    for i in range(1,6):
        if 5 % i == 0:
            print(i, end = " ")         
    

if __name__ == "__main__":
    main()
    
