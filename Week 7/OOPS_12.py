class Student:
    def __init__(self, name, roll_no, age):
        self.name = name        # public attribute
        self._roll_no = roll_no # protected attribute (single underscore)
        self.__age = age        # private attribute (double underscore)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self._roll_no}")
        print(f"Age: {self.__age}")
    
    # Getter method for private attribute
    def get_age(self):
        return self.__age
    
    # Setter method for private attribute
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative")

# Creating student object
student = Student("John", 101, 20)

# Accessing attributes
print(student.name)      # Public - works fine
print(student._roll_no)  # Protected - accessible but convention says not to
# print(student.__age)   # Private - will raise error

# Using methods
student.display_info()
print("Age:", student.get_age())
student.set_age(21)
print("New age:", student.get_age())