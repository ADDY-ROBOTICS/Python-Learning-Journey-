def decorate(func):
    def wrapper(a, b):
        print("This is the addition")
        func(a, b)
        print("This is the end of the function")
    return wrapper

@decorate
def addition(a,b):
    print(f"The sum of {a} and {b} is {a+b}")

addition(5, 7)