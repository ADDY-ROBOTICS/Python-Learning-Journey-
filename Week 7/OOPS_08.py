#Multilevel inheritance 
class Animal:
    def eat(self):
        print("Animal is eating")

class Mammal(Animal):
    def breathe(self):
        print("Mammal is breathing air")

class Dog(Mammal):
    def bark(self):
        print("Dog says: Woof!")

if __name__ == "__main__":
    d = Dog()
    d.eat()      # from Animal
    d.breathe()  # from Mammal
    d.bark()     # from Dog