# Very simple examples of map() and filter()

def main():
    numbers = [1, 2, 3, 4, 5]

    # map: apply a function to every item (square each number)
    squares = list(map(lambda x: x * x, numbers))

    # filter: keep only items that match the predicate (even numbers)
    evens = list(filter(lambda x: x % 2 == 0, numbers))

    print("numbers:", numbers)
    print("squares (map):", squares)
    print("evens (filter):", evens)

if __name__ == "__main__":
    main()