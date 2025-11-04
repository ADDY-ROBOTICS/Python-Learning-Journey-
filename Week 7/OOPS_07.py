# multiple inheritance 
class Parent1:
    def __init__(self):
        print("Parent1.__init__")
        super().__init__()

    def who(self):
        print("Parent1")

class Parent2:
    def __init__(self):
        print("Parent2.__init__")
        super().__init__()

    def who(self):
        print("Parent2")

class Child(Parent1, Parent2):
    def __init__(self):
        print("Child.__init__")
        super().__init__()

    def who(self):
        print("Child")
        print("-> calling super().who():", end=" ")
        super().who()

if __name__ == "__main__":
    obj = Child()
    print()
    obj.who()
    print()
    # direct call to Parent2's method
    print("Direct Parent2.who(obj):", end=" ")
    Parent2.who(obj)
    print()
    # show method resolution order
    print("MRO:", [cls.__name__ for cls in Child.mro()])