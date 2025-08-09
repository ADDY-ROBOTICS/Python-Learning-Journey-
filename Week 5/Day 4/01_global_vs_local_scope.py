#Write a Python program where a variable x is defined globally and another x is defined locally inside a function. Print both global and local values appropriately.
x = 10
def main():
    
    
    local_x = 7 
    print(f"This is the local x: {local_x}") 

if __name__ == "__main__":
    main()

print(f"This is the global x: {x}")
    

    
