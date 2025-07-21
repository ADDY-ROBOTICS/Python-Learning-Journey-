def main():
    for num in range(1,11):
        if num % 2 != 0:
            continue
        print(num)    

if __name__ == "__main__":
    main()
    
# This code prints even numbers from 1 to 10, skipping odd numbers using continue.