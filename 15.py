def main():
    value = -2
    match value:
        case n if n < 0:
            print('Negative')
        case n if n >= 0:
            print('Zero or Positive')    
    

if __name__ == "__main__":
    main()
    