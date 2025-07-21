#Write Python code to access and print the second item of the first nested tuple in a tuple named points containing (5, 6), (7, 8).

def main():
    nested_tuple = ( (5, 6), (7, 8))
    first_nest = nested_tuple[0]
    print(first_nest[1])
   

if __name__ == "__main__":
    main()
    
