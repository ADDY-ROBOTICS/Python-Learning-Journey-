# Hollow Rectangle
def main():
    rows = 4
    columns = 5
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("*" * columns, end=" ")
        else:
            print("*", end="")
            for j in range(1, columns - 1):
                print(" ", end="")
            if columns > 1:
                print("*", end = " ")
            print()
if __name__ == "__main__":
    main()

