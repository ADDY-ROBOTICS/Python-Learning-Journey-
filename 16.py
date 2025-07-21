def main():
    score = 85
    match score:
        case n if n > 90:
            print("Excellent")
        case n if 70 < n < 90:
            print('Good')
        case _:
            print('Needs improvement')        

if __name__ == "__main__":
    main()
    

    