#Write a Python program to join the list ['Python', 'Java', 'C++'] into a single string with hyphens.
def main():
    my_list  = ['Python', 'Java', 'C++']
    joined_string = "-".join(my_list)
    print(joined_string)
    

if __name__ == "__main__":
    main()
    