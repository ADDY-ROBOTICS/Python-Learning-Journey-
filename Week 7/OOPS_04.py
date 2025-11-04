# python
class Fish:
    species = "Salmon"            # class attribute

    def __init__(self, name, color):
        self.name = name         # instance attribute
        self.color = color

    def swim(self):             # instance method
        return f"{self.name} is swimming"

    @classmethod
    def from_string(cls, data): # class method (alternative constructor)
        name, color = data.split(",")
        return cls(name.strip(), color.strip())

    @staticmethod
    def is_freshwater(species_name):  # static method (utility)
        return species_name.lower() in ("trout", "carp", "bass")

# Usage
n = Fish.from_string("Nemo, orange")   # calls classmethod -> returns Fish instance
print(n.swim())                         # instance method
print(Fish.is_freshwater("trout"))      # staticmethod can be called on class or instance
print(n.is_freshwater("trout"))