#Write Python code to pop an item from a set named numbers containing 1, 2, 3, store it in a variable popped_item, and print it.
def main():
    numbers = {1, 2, 3}
    popped_item = numbers.pop()
    print(popped_item)
    
if __name__ == "__main__":
    main()