def main():
    grade = input("Enter the grade here (A/B/C/D/F):")
    match grade:
        case 'A':
            print("Excellent work! ")
        case 'B':
            print('Well done!')  
        case 'C':
            print('Average Performance')
        case 'D':
            print('Needs improvement')
        case 'F':
            print('Failing Grade')      
        case _:
            print("Invalid grade")             
if __name__ == "__main__":
    main()