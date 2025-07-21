#Write Python code to clear all items from a set named items containing "pen", "book", "ruler" and print the empty set.
def main():
    items = {"pen", "book", "ruler"}
    items.clear()
    print(items)

if __name__ == "__main__":
    main()