from networkx import reverse


def main():
   num = 121
   original_num = num
   reverse = 0
   while num > 0:
     digit = num % 10 
     reverse = reverse* 10 + digit
     num //= 10   

     # Check if the number is a palindrome
   if  reverse == original_num :
        print("True")
   else:
        print('False')    


         
if __name__ == "__main__":
    main()  