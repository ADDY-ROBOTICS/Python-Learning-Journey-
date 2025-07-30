#Write a python program called calculate_total that takes a base price and a keyword-only argument 'tax'. Return the total.
def calculate_total(base_price , * , tax = 0):

    return   base_price + tax 

total = calculate_total(100, tax = 20)
print(total)    