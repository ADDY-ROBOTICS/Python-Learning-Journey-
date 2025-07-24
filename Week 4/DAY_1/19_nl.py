def main():
    
    coulmn = 4
    num = 1
    for i in range(1,4):
        num = i 
        for j in range(coulmn):
            print(num ,  end = " ")
            num += 1
        print()    

if __name__ == "__main__":
    main()
    