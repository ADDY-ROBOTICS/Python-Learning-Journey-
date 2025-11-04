#Method Overriding in Python OOPs
class Animal:
    def show(self):
        print("I am an animal")
class Dog(Animal):
    def show(self):
        print("I was overridden method from Animal class and I am a dog now ")
    
obj = Dog()
obj.show() #OUTPUT = "I was overridden method from Animal class and I am a dog now "