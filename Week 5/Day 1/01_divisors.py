def main():
    number = 10 
    print("The numbers that divide 10 completely are:")

    for i in range(1, number + 1 ):
        if number % i == 0:
            print(i)
if __name__ == "__main__":
    main()
    
