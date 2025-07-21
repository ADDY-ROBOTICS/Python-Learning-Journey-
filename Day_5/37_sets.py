#Write Python code to add a tuple (1, 2) to a set named coordinates containing (3, 4) and print the updated set.

def main():
    numbers = (1,2)
    coordinates = {(3,4)}
    coordinates.add(numbers)
    print(coordinates)
if __name__ == "__main__":
    main()
    