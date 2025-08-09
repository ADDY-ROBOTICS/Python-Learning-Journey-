def main():
    a , b = 50 , 20 

    temp = b 
    b = a % b 
    a = temp
      
    print(f"after on swap values of a & b are : ({a}, {b})")

if __name__ == "__main__":
    main()
    