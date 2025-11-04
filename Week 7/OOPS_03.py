class Fish:
    a = "Salmon" #Class Attribute

    def __init__(self, name, color):
        self.name = name  # Instance Attribute
        self.color = color  # Instance Attribute
    
    def swim(self):  # Instance Method
        return f"{self.name} is swimming!"
    
    def get_color(self):  # Instance Method
        return f"{self.name} is {self.color} in color"

# Creating objects and calling instance methods
nemo = Fish("Nemo", "orange")
print(nemo.swim())        # Output: Nemo is swimming!
print(nemo.get_color())   # Output: Nemo is orange in color