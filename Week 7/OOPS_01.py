class Factory:
    a = 12 #attribute 
    def display(self): #method
        print("This is a method inside Factory class")
    print("Hello i will just get initialised nothing else ")

print(Factory.a)  # Accessing the class attribute directly
Factory().display()  # Creating an instance and calling the method