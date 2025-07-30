#Write a function called 'details' that takes name, age, and occupation as parameters. Call the function using keyword arguments in any order and print the output.
def details(name , age , occupation):
    print(f"{name} is {age} years old and works as {occupation}")

details(name = "ADDY", age = "19", occupation = "Robotics engineer") #order doesn't matter
details(age = "19", occupation = "Robotics engineer", name = "ADDY")
    
