colors = ['red', 'blue', 'green']
print(colors) #method one to create this list 

colors = list(('red', 'blue', 'green')) #method two to create this list
print(colors) # Output: ['red', 'blue', 'green']

colors = "red, blue, green".split(', ') #method three to create this list
print(colors) # Output: ['red', 'blue', 'green']\

colors = [color for color in ['red', 'blue', 'green']] #method four to create this list
print(colors) # Output: ['red', 'blue', 'green']