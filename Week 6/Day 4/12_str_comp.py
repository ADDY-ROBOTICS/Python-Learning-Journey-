#Write a Python program to sort and print two strings 'zebra' and 'lion' in alphabetical order.

def main():
    a = "zebra"
    b = "lion"
    word_list = [a,b]
    sorted_list = sorted(word_list)
    print(sorted_list)


if __name__ == "__main__":
    main()