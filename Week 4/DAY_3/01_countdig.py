def main():
    num = 123 
    count = 0
    if num == 0:
        count = 1
    else:
        count =  0
        while num > 0:
            num = num // 10
            count += 1
    print("Number of digits:", count)    

if __name__ == "__main__":
    main()
    
