def main():
    number = 123
    digits = 0
    while number > 0:
        number //= 10
        digits += 1
    print(f"Total digits: {digits}")  # Final count of digits
if __name__ == "__main__":
    main()