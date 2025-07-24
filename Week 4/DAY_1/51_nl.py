def main():
    count = 0
    num = 1
    while count < 5:
        if num % 2 == 0:
            count += 1 
        num += 1
    print("The total number of even numbers is", count)
if __name__ == "__main__":
    main()
    #Write a Python program to count even numbers starting from 1 and print the count, stopping when 5 even numbers are found, using a while loop.