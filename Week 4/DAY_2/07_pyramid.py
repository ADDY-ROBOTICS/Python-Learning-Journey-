def main():
    rows = 5 
    for i in range(1, rows + 1):
        print(" "* (rows - i), end = "")
        # Concatenate numbers as a single string
        num_str = ''.join(str(j) for j in range(1, i + 1))
        print(num_str)

if __name__ == "__main__":
    main()

