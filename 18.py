def main():
   value = 3
   match value:
    case n if n == 0:
        print('Zero')
    case n if n > 0 and n % 2 ==0:
        print("Positive even")
    case  n if n > 0 and n % 2 !=0:
        print(("Positive odd"))
    case n if n < 0:
        print('Negative')            

if __name__ == "__main__":
    main()