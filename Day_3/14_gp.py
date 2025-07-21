def main():
    a_1 = 3 
    r = 2 
    print('The first 5 terms of the geometric progression are:')
    for n in range(1,6):
        a_n = a_1*r**(n-1)
        print(a_n)
if __name__ == "__main__":
    main()
    
