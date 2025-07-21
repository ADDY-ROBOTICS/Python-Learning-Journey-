def main():
    n = int(input("Enter positive number :"))
    total_sum = 0
    if n > 0:
        for num in range(1,n+1):
            total_sum += num
        print(total_sum)   
    else :
        print(0) 

    

if __name__ == "__main__":
    main()
    
