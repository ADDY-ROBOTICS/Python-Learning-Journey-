#Write the same calculate_total function with a keyword-only argument 'tax'. Show that calling it without a keyword for tax raises an error.
def calculate_total(base_price , * , tax = 0):

    return   base_price + tax 

total = calculate_total(100, tax = 2)
print(f"Correct call: {total}")

# The following line will raise a TypeError because 'tax' must be a keyword argument.
error_case = calculate_total(100, 20) 
print(f"This will give an error {error_case}")
# Uncommenting the line below will raise a TypeError