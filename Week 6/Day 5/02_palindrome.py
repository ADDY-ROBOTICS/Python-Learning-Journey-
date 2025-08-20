#Check if the first and last characters of the string "radar" are the same.


def main():
    s = "radar"
    start = 0
    end = len(s) - 1

    while  start < end:
        if s[start] != s[end]:
            print("First and Last characters are not same")
        start += 1
        end -= 1
    print("first and last characters are equal ")


if __name__ == "__main__":
    main()