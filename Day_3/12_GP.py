def main():#WRONG METHOD
    a_1 = 2 
    r = 3 
    a_n = 54 
    if (a_n/a_1) % r == 0:
        print(f"{a_n} is a term in the geometric progression")
    else :
        print(f"{a_n} is not a  term in the geometric progression")    
if __name__ == "__main__":
    main()
    
#CORRECT METHOD
import math

def main():
    first_term = 2
    common_ratio = 3
    target_term = 54

    # Check if (target_term / first_term) is a power of common_ratio
    if target_term % first_term != 0:
        print(f"{target_term} is not a term in the geometric progression")
        return

    quotient = target_term / first_term
    # Compute the exponent n where common_ratio^n = quotient
    exponent = math.log(quotient, common_ratio)
    
    if exponent.is_integer():
        print(f"{target_term} is a term in the geometric progression")
    else:
        print(f"{target_term} is not a term in the geometric progression")

if __name__ == "__main__":
    main()