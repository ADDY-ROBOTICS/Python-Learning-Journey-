#Write a Python program called greet that takes a name and an optional message with default value 'Hello'. Print the message followed by the name.
def greet(name , message = "Hello"):
    print(f"{message}, {name}")

greet("ADDY")
greet("ADDY", "Welcome")
    