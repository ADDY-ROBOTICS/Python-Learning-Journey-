x = 10

def changing_global():
    
    global x 
    print(f"The value of x before updating using the global keyword {x}")
    # Using the global keyword to change the value of x
    x = 100
    print(f"The value of x after updating using the global keyword {x}")
    
changing_global()