#Write a Python function that prints a description of itself using a docstring. Define the function with a docstring and then print the docstring.

def describe():
    '''This function prints it's own documentation string'''
    print(describe.__doc__)

describe()