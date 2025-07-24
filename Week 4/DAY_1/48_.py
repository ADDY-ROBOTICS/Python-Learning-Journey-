def main():
    count = 0 
    i = 10
    while i <= 20:
        if i % 2 == 0:
            count += 1
        i += 1
    print("The total no of even numbers from 10 to 20 are", count)

if __name__ == "__main__":
    main()

