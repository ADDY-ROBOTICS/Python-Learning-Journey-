#args 
def addition(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

addition(12,12,12,12)

#kwargs 
def information(**kwargs):
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(name = "ADDY", age = 19, designation = "Robotics and Ai engineer")