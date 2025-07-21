def main():
   a_1 = 2 
   d = 3 
   n = 5
   a_n = a_1 + (n-1)*d
   print(f"{n}th term of the AP is : {a_n}")

if __name__ == "__main__":
    main()
 #sum of n terms   
    def main():
     a_1 = 3
     n = 10
     d = 2
     sum_= n*(2*a_1 + (n-1)*d)/2
     print(f"sum of {n} terms of this AP is :{sum_}")
    if __name__ == "__main__":
     main()

#Write Python code to check if 15 is a term in the arithmetic progression with the first term 2 and common difference 3.
def main():
    a_1 = 2 
    d = 3 
    a_n = 15

    if a_n >= a_1:
        if (a_n - a_1) % d == 0:
            print(f"{a_n} is the term of AP")
        else:
            print(f"{a_n} is not the term of AP")

if __name__ == "__main__":
    main()





