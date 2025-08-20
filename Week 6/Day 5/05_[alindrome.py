def main():
    s = "Racecar"
    s_new = s.lower()

    start = 0
    end = len(s_new) - 1

    while start < end:
        if s_new[start] != s_new[end]:
            print(f"{s_new} is not a palindrome")
            exit()

        start += 1
        end -= 1

    print(f"{s_new} is a palindrome")
if __name__ == "__main__":
    main()