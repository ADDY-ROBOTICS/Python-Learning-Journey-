def main():
    total_sum = 0
    num = 1
    while num <= 10:
        if num % 4 == 0:
            num += 1#ONLY increments when the num is divisible by 4 
            continue
        total_sum += num 
        num += 1 # increments no matter what 
    print(total_sum)     
            

if __name__ == "__main__":
    main()
    
