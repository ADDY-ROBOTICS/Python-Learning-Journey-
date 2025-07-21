def main():
    total_sum = 0
    for num in range(1,8):
        if num % 5 == 0:
            continue
        total_sum += num 
    print(total_sum)        

if __name__ == "__main__":
    main()
    
# This code calculates the sum of numbers from 1 to 7, skipping those that are multiples of 5.