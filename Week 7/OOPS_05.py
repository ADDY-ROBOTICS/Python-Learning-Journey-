class Person:
    species = "Human"
    population = 0

    def __init__(self,name,age):
        self.name = name  #Instance variable 
        self.age = age   # Instance variable 
        Person.population += 1 # update variable

    #INSTANCE METHOD - works with object data 
    def introduce(self):  #instance method
        return f"Hi, I am {self.name} {self.age} years old "
    
    #CLASS METHOD - works with class data 
    @classmethod
    def get_population(cls):
        return f"There are {cls.population}, {cls.species}s"

    @classmethod
    def create_baby(cls,name):
        return cls(name, 0) #creates new object with default age 
    
    #STATIC METHOD - independent function 
    @staticmethod
    def is_adult(age):
        return age >= 18
    
# Creating objects
person1 = Person("Alice", 30)
person2 = Person.create_baby("Bob",17)

# Calling instance method
print(person1.introduce())  # Output: Hi, I am Alice 30 years old

# Calling class method
print(Person.get_population())  # Output: There are 2, Humans

# Calling static method
print(Person.is_adult(20))  # Output: True
print(Person.is_adult(16))  # Output: False (works with objects too )