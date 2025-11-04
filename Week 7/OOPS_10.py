#DUCK TYPING
class Animal:
    def show(self):
        print("I am showing")

class Human:
    def show(self):
        print("I am also showing")

obj1 = Animal()
obj2 = Human()

obj1.show()
obj2.show()