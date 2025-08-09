cool_global = 100

def global_doesnt_change():
    ''' This function tells that inside the function wiithout global keyword doesnt affect the global '''
    cool_global = 99

    print(cool_global)#This will print the global inside the function 
global_doesnt_change()
print(cool_global)# This prints the global value  which tells that without the global keyword the value isnt affected 
