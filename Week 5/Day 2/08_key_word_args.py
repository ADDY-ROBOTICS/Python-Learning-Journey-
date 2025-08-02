#Write a Python function that accepts any number of keyword arguments and returns them as a dictionary.
def fruits(**fruit_info):

    for key , value in fruit_info.items():
     print(f"{key}:{value}")

fruits(name = "mango",color = "yellow" , more = "known as King of Fruits") 