def main():
    for i in range(1, 4):
        for j in range(1, 4):
            if j == 2:
                print(i * (j - 1))  # Print before breaking, using last valid j
                break

if __name__ == "__main__":
    main()