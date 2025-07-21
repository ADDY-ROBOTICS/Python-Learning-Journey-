def main():
    status = "Active"
    match status:
        case 'Active' | 'Inactive':
            print('Valid status')
        case _:
            print('Invalid status')        

if __name__ == "__main__":
    main()