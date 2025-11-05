def decorator(func):
    def wrapper():
        print("Hey how are you do you remmeber the date ..??")
        func()
        print("May god bless you with lots of happiness and success")
    return wrapper
    
    
@decorator
def greeting():
    print("Happy Birthday to you!")

greeting()