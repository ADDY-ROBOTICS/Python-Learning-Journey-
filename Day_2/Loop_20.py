def main():
    num = 789
    reverse = 0
    while num > 0:
        digit  = num % 10  #Gets the last digit of the num 
        reverse = reverse * 10 + digit  #Builds the reverse number

        num //= 10 #Remove the last digit
    print(reverse)    
    if __name__ == "__main__":
        main()
    
