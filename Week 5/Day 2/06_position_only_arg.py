#Write a function that multiplies two numbers and adds a third one. Make the first two parameters positional-only using '/' in the function definition.
def fun(a,b,/,c):
    ''' This Function takes two positional Arguments and one key word argument using '/'  positional only arguments'''

    return ((a*b) + c)

fun(2,5,c = 9)